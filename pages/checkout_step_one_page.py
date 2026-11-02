from playwright.async_api import Page, expect
from utilities.logger import logger


class CheckoutStepOnePage:
    def __init__(self, page:Page):
        self.page=page
        self.first_name=page.get_by_placeholder("First Name")
        self.last_name=page.get_by_placeholder("Last Name")
        self.zip_code=page.get_by_placeholder("Zip/Postal Code")
        self.cancel_btn=page.get_by_text("cancel")
        self.continue_btn=page.get_by_role(role='button',name="continue")
        self.error_msg=page.get_by_text("Error: Last Name is required")

    async def first_name_fill(self, firstname):
        await self.first_name.fill(firstname)

    async def last_name_fill(self, lastname):
        await self.last_name.fill(lastname)

    async def zip_code_fill(self, zipcode):
        await self.zip_code.fill(zipcode)

    #async def concel_btn_click(self):
    #     await self.cancel_btn.click()

    async def continue_btn_click(self,username):
        await self.continue_btn.click()
        if username=="problem_user":
            await expect(self.error_msg).to_be_visible()
            logger.exception(f"Expected error for {username}")
            return False
        return True
    