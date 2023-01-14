# 구글 dog 저작권 무료 
from selenium import webdriver
driver = webdriver.Chrome("chromedriver")
driver.get("https://www.google.com/search?q=dog&tbm=isch&tbs=il:ol&rlz=1C5CHFA_enKR1002KR1002&hl=ko&sa=X&ved=0CAAQ1vwEahcKEwjQpszCh8f8AhUAAAAAHQAAAAAQAw&biw=2232&bih=1945")

# i =1,2,3
for i in range(1,5) :
    driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+ str(i)+']/a[1]/div[1]/img').screenshot('img/'+ str(i) +'.png')
