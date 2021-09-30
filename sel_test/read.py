
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver= webdriver.Firefox(executable_path="D:\geckodriver-v0.29.1-win64\geckodriver.exe")
driver.get("https://www.khulnamedicalcollege.org/search-report")
print(driver.title)
time.sleep(10)
phone = driver.find_element_by_css_selector("#mobile")
phone.send_keys("01714759148")
driver.find_element_by_xpath("//*[@id='date']").send_keys("08092021")
time.sleep(13)
driver.find_element_by_xpath("/html/body/section/div/div/div/form/button").click()
print(phone)
time.sleep(29)
print(driver.page_source)

driver.quit()