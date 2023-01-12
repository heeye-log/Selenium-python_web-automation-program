from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("인생이란 뭘까?")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

driver.find_element_by_xpath("//*[@id='hdtb-msb']/div[1]/div/div[4]/a").click()
