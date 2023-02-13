from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
user_account = "輸入您的蝦皮使用者帳號"
user_password = "輸入您的蝦皮使用者密碼"
options = Options()
options.chrome_executable_path = "./chromedriver.exe"
driver = webdriver.Chrome(options=options)
driver.get("https://shopee.tw/buyer/login?next=https%3A%2F%2Fshopee.tw%2F")
time.sleep(0.8)
userid = driver.find_element(By.XPATH, "//input[@type='text']")
userid.send_keys(user_account)
pw = driver.find_element(By.XPATH, "//input[@type='password']")
pw.send_keys(user_password)
login_button = driver.find_elements(By.CSS_SELECTOR, "button")[2]
time.sleep(1)
login_button.send_keys(Keys.ENTER)
time.sleep(3)
driver.get("https://shopee.tw/shopee-coins")
getcoins = driver.find_element(By.CSS_SELECTOR, "button[class^='pcmall-dailycheckin']").click()
time.sleep(2)
driver.close()
