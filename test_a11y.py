import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8000")

        # Check if the result input is readonly
        is_readonly = await page.locator("#result").evaluate("el => el.hasAttribute('readonly')")
        print(f"Is readonly: {is_readonly}")

        # Check if the result input has aria-label
        aria_label = await page.locator("#result").get_attribute("aria-label")
        print(f"Result aria-label: {aria_label}")

        # Check backspace button aria-label
        backspace_aria = await page.locator("button.op:has-text('⌫')").get_attribute("aria-label")
        print(f"Backspace aria-label: {backspace_aria}")

        # Check clear button aria-label
        clear_aria = await page.locator("button.op:has-text('C')").get_attribute("aria-label")
        print(f"Clear aria-label: {clear_aria}")

        # Check if focusing the input adds the focus-visible styling
        await page.focus("#result")
        box_shadow = await page.locator("#result").evaluate("el => window.getComputedStyle(el).boxShadow")
        print(f"Focus box-shadow: {box_shadow}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())