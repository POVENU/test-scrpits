from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# GitHub credentials and repository details
GITHUB_USERNAME = os.getenv('PAT_USERNAME')
GITHUB_PASSWORD = os.getenv('PAT_PASSWORD')
REPOSITORY = os.getenv('PAT_REPOSITORY')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def login_to_github(username, password):
    driver.get("https://github.com/login")
    time.sleep(2)  # Wait for the page to load

    username_input = driver.find_element(By.ID, "login_field")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for login to complete

def navigate_to_secret_scanning(repo):
    driver.get(f"https://github.com/{repo}/security/secret-scanning")
    time.sleep(5)  # Wait for the page to load

def capture_screenshot(filename):
    driver.save_screenshot(filename)
    print(f"Screenshot saved as {filename}")

if __name__ == "__main__":
    try:
        login_to_github(PAT_USERNAME, PAT_PASSWORD)
        navigate_to_secret_scanning(REPOSITORY)
        capture_screenshot("secret_scanning.png")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
