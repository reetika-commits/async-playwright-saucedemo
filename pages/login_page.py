from playwright.async_api import Page, expect
from utilities.logger import logger


class LoginPage:
   def __init__(self, page: Page):
       self.page = page
       self.username_input =  page.get_by_placeholder("Username")
       self.password_input =  page.get_by_placeholder("Password")
       self.login_button = page.get_by_text("Login")

       self.error_msg=page.get_by_text("Epic sadface: Sorry, this user has been locked out.")

   async def navigate(self, url: str):
       await self.page.goto(url)

   async def login(self, username: str, password: str):
       await self.username_input.fill(username)
       await self.password_input.fill(password)

       await expect(self.login_button).to_be_enabled()
       logger.info("Clicking login for %s", username)

       await self.login_button.click(timeout=10000)
       logger.info("Login button clicked for %s", username)

       if username=="locked_out_user":
           await expect(self.error_msg).to_be_visible()
           logger.exception(f"Expected error for {username}")

           return False
       return True
