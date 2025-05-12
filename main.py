from selenium import webdriver
from selenium.webdriver.common.by import By
import time

user_email = input("What is your email?\n")
user_password = input("What is your password?\n")

driver = webdriver.Chrome()

driver.get("https://monkeytype.com/login")

acceptCookies = driver.find_element(By.CLASS_NAME,"acceptAll")
acceptCookies.click()

email = driver.find_element(By.NAME, "current-email")
password = driver.find_element(By.NAME, "current-password")
signIn = driver.find_element(By.CLASS_NAME, "signIn")

email.send_keys(user_email)
password.send_keys(user_password)
signIn.click()

print("Done.")

driver.quit()