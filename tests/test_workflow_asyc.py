from datetime import datetime
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete import CheckoutComplete
from playwright.async_api import expect
from utilities.data_loader import read_test_data
import asyncio
from utilities.logger import logger

# Limit concurrency to 2 tasks at a time
semaphore = asyncio.Semaphore(2)

@pytest.mark.asyncio
# @pytest.mark.parametrize("data",testdata())
async def test_valid_login(browser_asyn): # 'page' is a Playwright fixture
   testdata=read_test_data()
   task_list=[]
   for data in testdata:
    
        task_list.append(workflow(data, browser_asyn))
    
   results= await asyncio.gather(*task_list, return_exceptions=True)
   errors=[result for result in results if isinstance(result,BaseException)]

   assert not errors, f"Workflow faliour(s): {errors}" 

async def workflow(data, browser):
        # Acquire semaphore before starting
    async with semaphore:
        context=None
        page=None
        try:
            context = await browser.new_context()
            page = await context.new_page()
            if await login_page_automation(page, data["Username"], data["Password"]):
                await invertory_page_automation(page)
                await cart_page_automation(page)
                if await checkout_page_one_automation(page , data["Username"]):
                    await checkout_page_two_automation(page)
                    await checkout_complete_page_automation(page)
        except Exception:
            logger.exception(
                "Workflow failed for user: %s",
                data["Username"]
            )
            raise
        finally:
            if page:
                try:
                    await page.screenshot(path=
                        f'saucedemo_automation_asyn/screenshots/{data["Username"]}-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
                    await page.close()
                except Exception as e:
                    logger.exception(f"Cleanup error closing page {e}")
            if context:
                try:
                    await context.close()
                except Exception as e:
                    logger.exception(f"Cleanup error closing context {e}")


async def login_page_automation(page, username,password ):
    login_page = LoginPage(page)
    await login_page.navigate("https://www.saucedemo.com/")
    return await login_page.login(username, password)

   # Assertion to verify successful login: url of landing page
    #await expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

async def invertory_page_automation(page):
    inventory_page=InventoryPage(page,"sauce-labs-bike-light")
    await inventory_page.add_item_button_click()
    await inventory_page.check_items_in_cart("1")
    #inventory_page.remove_item_button_click()
    #inventory_page.check_items_in_cart("0")
    await inventory_page.cart_icon_click()
   # Assertion to verify : url of landing page
    await expect(page).to_have_url("https://www.saucedemo.com/cart.html")

async def cart_page_automation(page):
    cart_page=CartPage(page,"sauce-labs-bike-light")
    await cart_page.items_in_cart()
   #  cart_page.remove_btn_click()
   #  cart_page.no_items_in_cart()
    await cart_page.checkout_btn_click()
   # Assertion to verify : url of landing page
    await expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

async def checkout_page_one_automation(page , username ):
    checkout_page_one=CheckoutStepOnePage(page)
    await checkout_page_one.first_name_fill(username)
    await checkout_page_one.last_name_fill("User")
    await checkout_page_one.zip_code_fill("135790")
    return(await checkout_page_one.continue_btn_click(username))


async def checkout_page_two_automation(page):
    checkout_page_two=CheckoutStepTwoPage(page)
    await checkout_page_two.finish_btn_click()
    await expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

async def checkout_complete_page_automation(page):
    checkout_complete=CheckoutComplete(page)
    await checkout_complete.check_checkout_complete()


   
   




    

