from playwright.async_api import Page, expect

class CartPage:
    def __init__(self, page:Page, item:str):
        self.page=page
        self.remove_btn=page.locator(f'[data-test="remove-{item}"]')
        self.cart_items=page.locator('//div[@class="cart_item_label"]')
        self.checkout_btn=page.locator('[data-test="checkout"]')

    async def checkout_btn_click(self):
        await self.checkout_btn.click()

    async def remove_btn_click(self):
       await self.remove_btn.click()

    async def items_in_cart(self):
        await expect(self.cart_items).not_to_be_empty()

    async def no_items_in_cart(self):
        await expect(self.cart_items).to_have_count(0)