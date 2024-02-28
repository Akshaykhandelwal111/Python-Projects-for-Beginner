from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)

# username
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input").send_keys("username")
# password
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_keys("password")
time.sleep(1)
# sign
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()


