from selenium import webdriver
import time

parameter = '&' + input('請輸入網址').split('&', maxsplit=1)[1]
row = input('請輸入課程在第幾列') # 比實際的列數多一

# webdriver執行檔的位置
path = "C:/Users/user/Downloads/edgedriver_win64/msedgedriver.exe"
driver = webdriver.Edge(path)

# 選課登陸頁面
login_url = 'https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/login.php?m=0'

while True:
    driver.get(login_url)
    id = driver.find_element_by_name('id')
    password = driver.find_element_by_name('password')

    # 輸入學號、密碼
    id.send_keys("409410015")
    password.send_keys("Jerry1122@")
    password.submit()

    add_course_url = driver.find_element_by_link_text('加選及加簽').get_attribute('href')
    session_id = add_course_url.split('=')[1]

    front = 'https://kiki.ccu.edu.tw/~ccmisp06/cgi-bin/class_new/Add_Course01.cgi?session_id='
    url = (front + session_id + parameter)
    driver.get(url)

    for i in range(30):
        driver.refresh()
        course_name = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[' + row + ']/th[4]').text
        remaining = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[' + row + ']/th[3]').text
        print(course_name, remaining) # 確認有沒有選對課程
        if (int(remaining) > 0):
            check_box = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr['+ row +']/th[1]/input')
            check_box.click()
            check_box.submit()
            driver.quit()
            break
        else:
            time.sleep(10)
    

# time.sleep(10)
# driver.quit()

# /html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[3]/th[3]
# /html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[2]/th[3]
# /html/body/center/form/table/tbody/tr[1]/th/table/tbody/tr[2]/th[1]/input
# /html/body/center/form/table/tbody/tr[2]/th/input
