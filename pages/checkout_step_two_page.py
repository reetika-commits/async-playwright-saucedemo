from playwright.async_api import Page

class CheckoutStepTwoPage:
    def __init__(self, page:Page):
        self.page=page
        self.finish_btn=page.get_by_text("Finish")

    async def finish_btn_click(self):
        await self.finish_btn.click()