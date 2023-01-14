from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver")
driver.get("https://test-881025.tistory.com/guestbook")

# 반복문 만들기
count = 0

while count < 5 :

    driver.find_element_by_name("name").click()
    driver.find_element_by_name("name").send_keys("아무거나")

    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").send_keys("아무거나")

    driver.find_element_by_css_selector("#entry0Comment > div.comments.guest > form > div > textarea").click()
    driver.find_element_by_xpath("//*[@id='entry0Comment']/div[2]/form/div/textarea").send_keys("댓글 입력 예제")

    driver.find_element_by_xpath("//*[@id='entry0Comment']/div[2]/form/div/div[2]/button").click()
    #새로고침
    driver.refresh()

    time.sleep(3)

    count = count + 1

driver.close()
