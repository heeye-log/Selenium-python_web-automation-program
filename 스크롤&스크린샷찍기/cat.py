from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver")

driver.get("https://www.google.com/search?q=cat&tbm=isch&tbs=il:ol&rlz=1C5CHFA_enKR1002KR1002&hl=ko&sa=X&ved=0CAAQ1vwEahcKEwigo_e7_Mb8AhUAAAAAHQAAAAAQAw&biw=2232&bih=1945")

driver.get_screenshot_as_file("data/test.png")

driver.execute_script("window.scrollTo(0,1000)")

for i in range(1,5) :

    scroll_index = i * 1000
    # 0, 1000, 2000, 3000, 4000

    # 스크롤
    driver.execute_script("window.scrollTo(0," + str(scroll_index) + ")")
    # driver.execute_script("window.scrollTo(0,0)")

    # 대기
    time.sleep(3)

    driver.get_screenshot_as_file("data/test"+ str(scroll_index) + ".png")


driver.close()
