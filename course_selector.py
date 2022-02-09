from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# webdriver執行黨的位置
path = "" 
driver = webdriver.Chrome(path) # or other webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 選課登陸頁面
driver.get("https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/login.php?m=0")

id = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/font/center/form/table/tbody/tr[2]/td[2]/input'))
)
password = driver.find_element_by_xpath('/html/body/font/center/form/table/tbody/tr[3]/td[2]/input')

#輸入學號、密碼
id.send_keys("")
password.send_keys("")
id.send_keys(Keys.ENTER)

# need to modify
driver.get("https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/Add_Course01.cgi?session_id=V0zYxKwgMhgYBD32tlnzWImT9fTbkQgqs926&dept=F000&grade=2&page=0")

while True:
    # driver.refresh()
    remaining = driver.find_element_by_xpath('')
    print(remaining.text)
    if (int(remaining.text) > 0):
        # 依照想上的課程修改
        check_box = driver.find_element_by_xpath('')
        check_box.click()
        submit = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[2]/th/input')
        submit.click()
        # driver.quit()
        # break
    time.sleep(30)
    

# time.sleep(10)
# driver.quit()

# /html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[3]/th[3]
# /html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[2]/th[3]
# /html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[2]/th[1]/input
# /html/body/center/form/table/tbody/tr[2]/th/input
