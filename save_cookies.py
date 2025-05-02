from selenium import webdriver
import pickle
import time

# Launch Chrome
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

# Prompt user to log in manually
print("🔐 Please log in manually in the opened browser window.")
input("✅ Press Enter after you have logged in...")

# Save cookies to file
cookies = driver.get_cookies()
with open("flipkart_cookies.pkl", "wb") as file:
    pickle.dump(cookies, file)

print("🍪 Cookies saved successfully.")
driver.quit()
