import os
from playwright.sync_api import sync_playwright, expect

def test_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        print(f"Loading {file_path}")
        page.goto(file_path)

        # Test 1: Check for ARIA labels on iconic buttons (should fail initially)
        print("Checking for ARIA labels...")
        try:
            # We use a short timeout so we don't wait too long for failures
            expect(page.locator('button[onclick="backspace()"]')).to_have_attribute("aria-label", "Backspace", timeout=1000)
            print("PASS: Backspace button has aria-label")
        except Exception as e:
            print("FAIL: Backspace button missing aria-label")

        # Test 2: Test keyboard input (should fail initially)
        print("Testing keyboard input...")
        try:
            page.keyboard.press("7")
            page.keyboard.press("+")
            page.keyboard.press("3")
            page.keyboard.press("Enter")

            # Check result
            result_input = page.locator("#result")
            # We use a short timeout here too
            expect(result_input).to_have_value("10", timeout=1000)
            print("PASS: Keyboard calculation worked (7+3=10)")
        except Exception as e:
            result_val = page.locator("#result").input_value()
            print(f"FAIL: Keyboard calculation failed. Expected 10, got '{result_val}'")

        # Test 3: Test Focus Styles
        # Tab to a button and take a screenshot
        print("Testing focus styles...")
        # Reload to clear any state
        page.reload()
        # Press Tab a few times to reach a button
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")

        # Take screenshot of the page
        screenshot_path = os.path.join(cwd, "verification/verification.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    test_calculator()
