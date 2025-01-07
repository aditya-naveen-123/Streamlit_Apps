from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
import time

#service_obj = Service("C:\Testautomation\chromedriver-win32\chromedriver.exe")
#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10)
driver.find_element(By.XPATH,"//input[@name = 'username']").send_keys("Admin")
driver.find_element(By.NAME, 'password').send_keys("admin123")
driver.find_element(By.XPATH, "//button[text() = ' Login ']").click()
time.sleep(5)
title = driver.title
if title == "OrangeHRM":
    print("Title matched")
else:
    print("Title Mismatched")