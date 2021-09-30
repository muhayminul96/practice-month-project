from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

f = open('hello.txt', 'w')
driver= webdriver.Firefox(executable_path="D:\geckodriver-v0.29.1-win64\geckodriver.exe")
driver.get("https://www.spotify.com/in-en/signup/")
print(driver.title)
se = driver.find_elements_by_css_selector( "div.Radio-fatlcr-0:nth-child(1) > label:nth-child(2) > span:nth-child(2)").click()
print(se.is_displayed())
print(se.is_enabled())
print(se.is_selected())

time.sleep(2)
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)

f.write(str(driver.title))
time.sleep(1)
driver.quit()