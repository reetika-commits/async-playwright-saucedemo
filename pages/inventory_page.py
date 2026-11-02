from playwright.async_api import Page, expect

class InventoryPage:
    def __init__(self, page:Page, item:str):
        self.page=page
        self.add_item_button=page.locator(f'[data-test="add-to-cart-{item}"]')
        self.remove_item_button=page.locator(f'[data-test="remove-{item}"]')
        self.cart_icon= page.locator('//div[@id="shopping_cart_container"]/a')
        self.cart_badge=page.locator('//div[@id="shopping_cart_container"]/a/span[contains(@class,"shopping_cart_badge")]')
        

    async def add_item_button_click(self):
        await self.add_item_button.click()

    async def remove_item_button_click(self):
        await self.remove_item_button.click()

    async def check_items_in_cart(self, expected):
        await expect(self.cart_badge).to_have_text(expected)

    async def cart_icon_click(self):
        await self.cart_icon.click()