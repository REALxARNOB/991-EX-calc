import sys
import time
import subprocess
from playwright.sync_api import sync_playwright

def verify_and_screenshot():
    server = subprocess.Popen([sys.executable, "-m", "http.server", "8000"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    try:
        with sync_playwright() as p:
            print("Launching browser...")
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8000/index.html")

            # Type 7 + 3
            page.keyboard.press("7")
            page.keyboard.press("+")
            page.keyboard.press("3")

            # Take screenshot before calculation
            page.screenshot(path="verification/before_calc.png")
            print("Screenshot before_calc.png saved")

            # Press Enter
            page.keyboard.press("Enter")

            # Take screenshot after calculation
            page.screenshot(path="verification/after_calc.png")
            print("Screenshot after_calc.png saved")

            # Check for result attribute
            result_input = page.locator("#result")
            readonly = result_input.get_attribute("readonly")
            aria_label = result_input.get_attribute("aria-label")

            if readonly is not None:
                print("PASS: Input is readonly")
            else:
                print("FAIL: Input is not readonly")

            if aria_label == "Calculator Result":
                print("PASS: Input has correct aria-label")
            else:
                print(f"FAIL: Input has incorrect aria-label: {aria_label}")

            browser.close()
    finally:
        server.terminate()

if __name__ == "__main__":
    verify_and_screenshot()
