from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time

# Start Chrome browser
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

# Load cookies from saved file
with open("flipkart_cookies.pkl", "rb") as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# Refresh to apply cookies and load logged-in session
driver.refresh()
time.sleep(5)

# Go to wishlist page
driver.get("https://www.flipkart.com/wishlist?link=home_wishlist")
time.sleep(5)

# -----------------------------
# Phase 1: Load all items
# -----------------------------
print("🔄 Loading all wishlist items...")

while True:
    try:
        load_more_button = driver.find_element(By.CSS_SELECTOR, ".Ay2Trb")
        if load_more_button.is_displayed():
            load_more_button.click()
            print("🔁 Clicked 'Load More' button.")
            time.sleep(3)  # Wait for more items to load
        else:
            break
    except Exception:
        print("✅ No 'Load More' button found. All items loaded.")
        break

# -----------------------------
# Phase 2: Remove all items
# -----------------------------
print("🗑️ Starting to remove items from wishlist...")

while True:
    try:
        class_selector = ".Mj62aK"  # Remove button class
        remove_buttons = driver.find_elements(By.CSS_SELECTOR, class_selector)

        print(f"🔍 Found {len(remove_buttons)} 'Remove' buttons.")

        if not remove_buttons:
            print("✅ No more items to remove.")
            break

        for button in remove_buttons:
            try:
                button.click()
                print("🗑️ Clicked 'Remove'")
                time.sleep(1)

                # Confirm popup if needed
                confirm_selector = ".QqFHMw.AyekA8"
                yes_buttons = driver.find_elements(By.CSS_SELECTOR, confirm_selector)
                if yes_buttons:
                    yes_buttons[0].click()
                    print("✅ Confirmed remove")
                    time.sleep(1)

            except Exception as e:
                print(f"⚠️ Error removing item: {e}")
                continue

    except Exception as e:
        print(f"⚠️ Script stopped due to: {e}")
        break

driver.quit()
print("🧹 Wishlist cleared successfully.")