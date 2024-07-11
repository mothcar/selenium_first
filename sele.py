from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

for number in range(150):
  options = Options()
  options.add_argument("--start-maximized")
  options.add_experimental_option("detach", True)

  driver = webdriver.Chrome(options=options)
  url = "https://coupon-egg.netlify.app"

  driver.get(url)
  time.sleep(10)
  driver.find_element(By.ID, "login").click()
  time.sleep(800)
  driver.quit()
  print("Number : ", number)