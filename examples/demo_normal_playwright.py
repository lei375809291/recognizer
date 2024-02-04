from __future__ import annotations

import asyncio

from playwright.async_api import async_playwright

from recognizer.agents.playwright import AsyncChallenger


async def bytedance():
    # playwright install chromium
    # playwright install-deps chromium
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(locale="en-US")
        page = await context.new_page()
        challenger = AsyncChallenger(page)

        await page.goto("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox-explicit.php")
        await challenger.solve_recaptcha()


if __name__ == "__main__":
    asyncio.run(bytedance())
