import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('index.html')}")
    # Focus the input to see the focus state
    page.locator("#result").focus()
    page.screenshot(path="after.png")

    # Click 7, 8, 9, * 2 =
    page.get_by_text("7", exact=True).click()
    page.get_by_text("8", exact=True).click()
    page.get_by_text("9", exact=True).click()
    page.get_by_text("*", exact=True).click()
    page.get_by_text("2", exact=True).click()
    page.get_by_text("=", exact=True).click()

    val = page.locator("#result").input_value()
    print("Value:", val)
    assert val == "1578"

    browser.close()
