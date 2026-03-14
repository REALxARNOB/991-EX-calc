import os
from playwright.sync_api import Page, expect, sync_playwright

def test_calculator_functionality(page: Page):
    # Construct an absolute path to index.html
    filepath = f"file://{os.path.abspath('index.html')}"
    page.goto(filepath)

    # Calculate 7 + 8 =
    page.get_by_text("7", exact=True).click()
    page.get_by_text("+", exact=True).click()
    page.get_by_text("8", exact=True).click()
    page.get_by_text("=", exact=True).click()

    # The result should be 15
    # For <input>, the content is its value, use expect(locator).to_have_value()
    # or get_by_label("Calculator Result").input_value() == "15"
    result_input = page.get_by_label("Calculator Result")
    expect(result_input).to_have_value("15")

    # Check that input is focused visually by focusing it
    result_input.focus()

    # Check the attribute change
    expect(result_input).not_to_have_attribute("disabled", "")
    expect(result_input).to_have_attribute("readonly", "")

    page.screenshot(path="verification.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_calculator_functionality(page)
            print("Tests passed successfully.")
        finally:
            browser.close()
