from selenium import webdriver
driver = webdriver.Chrome("chromedriver")
driver.get("https://the-internet.herokuapp.com/upload")

#내 고정폴더 위치 지정
driver.find_element_by_id("file-upload").send_keys("/Users/heayeonkim/Desktop/auto/data/test.png")
