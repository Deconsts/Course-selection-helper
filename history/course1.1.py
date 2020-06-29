from selenium import webdriver
import time
username=input("账号：")
password=input("密码：")
subjects=input("所选课程编号：")
subjects=subjects.split(' ')
driver = webdriver.Chrome()
url = 'http://onestop.ucas.ac.cn/'
driver.get(url)
elem=driver.find_element_by_xpath("//input[@id='menhuusername']")
elem.send_keys(username)
elem=driver.find_element_by_xpath("//input[@id='menhupassword']")
elem.send_keys(password)
elem=driver.find_element_by_xpath("//div[@class='loginbtn']")
elem.click()
time.sleep(1)
elem=driver.find_element_by_xpath("//a[@title='选课系统']/h5/i")
elem.click()
elem=driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]//span")
elem.click()
time.sleep(1)
elem=driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/ul//li[1]/a")
elem.click()
time.sleep(1)
elem=driver.find_element_by_xpath("//form[@id='regfrm2']/div/button")
elem.click()
time.sleep(1)
for subject in subjects:
    i=0
    j=0
    while True:
        i+=1
        path='//tr['+str(i)+']/td[5]/a/span'
        try:
            elem=driver.find_element_by_xpath(path)
            driver.execute_script('arguments[0].scrollIntoView();', elem)
        except:
            j=1
            break
        if elem.text==subject:
            break
    if j==0:
        path='//tr['+str(i)+']/td[1]/input'
        elem=driver.find_element_by_xpath(path)
        driver.execute_script("$(arguments[0]).click()",elem)
    j=0
elem=driver.find_element_by_xpath("//button[@type='submit']")
driver.execute_script('arguments[0].scrollIntoView();', elem)
driver.execute_script("$(arguments[0]).click()",elem)
