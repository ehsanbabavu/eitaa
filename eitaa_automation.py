from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
import sys

def main(phone_number="9135621232"):
    print("Starting Eitaa automation script...")
    
    driver = None
    try:
        print("Setting up Chrome driver...")
        
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.page_load_strategy = 'eager'
        
        print("Downloading and setting up ChromeDriver...")
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(20)
        
        print("Opening Eitaa web messenger...")
        try:
            driver.get("https://web.eitaa.com/")
        except Exception as e:
            print(f"Page load timeout or error (continuing anyway): {e}")
        
        print("Waiting for page to load...")
        time.sleep(5)
        
        print(f"Page title: {driver.title}")
        print(f"Current URL: {driver.current_url}")
        
        if driver.current_url.startswith("data:") or len(driver.page_source) < 100:
            print("WARNING: Page did not load properly. Retrying...")
            driver.get("https://web.eitaa.com/")
            time.sleep(8)
            print(f"After retry - URL: {driver.current_url}")
            
            if driver.current_url.startswith("data:") or len(driver.page_source) < 100:
                raise Exception("Failed to load Eitaa website. The site may be blocking automated browsers or there is a network issue. Please try running the script again or check your internet connection.")
        
        wait = WebDriverWait(driver, 30)
        
        print("Looking for phone number input field...")
        phone_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='tel'], input[placeholder*='98']"))
        )
        
        print(f"Entering phone number: {phone_number}")
        phone_input.clear()
        phone_input.send_keys(phone_number)
        
        time.sleep(1)
        
        print("Looking for continue button...")
        continue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'ادامه')]"))
        )
        
        print("Clicking continue button...")
        continue_button.click()
        
        print("Successfully completed automation!")
        print("Waiting for next step (you may need to enter verification code manually)...")
        
        time.sleep(10)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        if driver:
            print("Keeping browser open for 30 seconds...")
            time.sleep(30)
            print("Closing browser...")
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    phone = sys.argv[1] if len(sys.argv) > 1 else "9135621232"
    main(phone)
