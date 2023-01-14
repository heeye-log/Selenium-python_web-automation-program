from selenium import webdriver

driver = webdriver.Chrome("chromedriver")

driver.get("https://velog.io/@heehe")

driver.get_screenshot_as_file('data/test.png')

driver.close()
