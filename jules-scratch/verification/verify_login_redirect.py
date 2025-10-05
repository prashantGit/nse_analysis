from playwright.sync_api import sync_playwright, expect
import re

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Go to the application's root URL.
    page.goto("http://127.0.0.1:5000/")

    # Expect the page to redirect to the ICICI login page using a regex.
    expect(page).to_have_url(re.compile(".*api.icicidirect.com.*"))

    # Take a screenshot of the login page.
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)