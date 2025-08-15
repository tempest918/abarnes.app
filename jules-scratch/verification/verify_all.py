import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the index.html file
        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')
        page.screenshot(path='jules-scratch/verification/index.png', full_page=True)

        # Get the absolute path to the contact.html file
        file_path = os.path.abspath('contact.html')
        page.goto(f'file://{file_path}')
        page.screenshot(path='jules-scratch/verification/contact.png', full_page=True)

        # Get the absolute path to the truck-loads-app.html file
        file_path = os.path.abspath('truck-loads-app.html')
        page.goto(f'file://{file_path}')
        page.screenshot(path='jules-scratch/verification/truck-loads-app.png', full_page=True)

        browser.close()

if __name__ == '__main__':
    run()
