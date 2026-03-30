import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{os.path.abspath('index.html')}")

        # Check readonly attribute on #result
        result_input = page.locator('#result')
        assert result_input.get_attribute('readonly') is not None, "readonly attribute missing"
        assert result_input.get_attribute('aria-label') == 'Calculator Result', "aria-label missing on result input"

        # Check aria-labels on Backspace and Clear buttons
        backspace_btn = page.locator('button[aria-label="Backspace"]')
        assert backspace_btn.count() == 1, "Backspace button missing aria-label"
        clear_btn = page.locator('button[aria-label="Clear Display"]')
        assert clear_btn.count() == 1, "Clear button missing aria-label"

        # Perform a basic calculation: 7 * 8 = 56
        page.get_by_role('button', name='7').click()
        page.get_by_role('button', name='*').click()
        page.get_by_role('button', name='8').click()
        page.get_by_role('button', name='=').click()

        # Wait for value to update and check it
        page.wait_for_timeout(500)
        assert result_input.input_value() == '56', f"Calculation failed: {result_input.input_value()}"

        # Test focus visible
        result_input.focus()
        page.wait_for_timeout(500)

        # Take a screenshot
        page.screenshot(path='calculator_screenshot.png')
        print("Test passed! Screenshot saved as calculator_screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
