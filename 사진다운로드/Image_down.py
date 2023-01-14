from selenium import webdriver
driver = webdriver.Chrome("chromedriver")
driver.get("https://www.daum.net/")

driver.find_element_by_xpath("//*[@id='daumHead']/div[1]/div/h1/a/img").screenshot("img/daum_logo.png")
