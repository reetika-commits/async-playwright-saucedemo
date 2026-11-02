from playwright.async_api import Page, expect

class CheckoutComplete:
    def __init__(self, page:Page):
        self.page=page
        self.checkout_complete_lbl=page.get_by_text("Checkout: Complete!")

    async def check_checkout_complete(self):
        await expect(self.checkout_complete_lbl).to_have_text("Checkout: Complete!")