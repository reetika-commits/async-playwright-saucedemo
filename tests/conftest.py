import pytest_asyncio
from playwright.async_api import async_playwright
import logging

logger = logging.getLogger(__name__)


@pytest_asyncio.fixture()
async def browser_asyn():
   async with async_playwright() as p:
       browser = await p.firefox.launch(headless=True)
       yield browser
       try:
            await browser.close()
       except Exception as e:
            logger.exception(f"Cleanup error closing browser {e}")


