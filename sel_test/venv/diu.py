from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver= webdriver.Firefox(executable_path="D:\geckodriver-v0.29.1-win64\geckodriver.exe")
driver.get("https://daffodilvarsity.edu.bd/")
print(driver.title)
se = driver.find_element_by_xpath("/html/body/section[9]/div/div[2]/div/div[1]/div/div[23]/div/div/div[2]/h3/a[1]").click()



time.sleep(60)
print(driver.title)



time.sleep(1)
driver.quit()