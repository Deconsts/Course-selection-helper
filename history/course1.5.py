from selenium import webdriver
import msvcrt,sys,os
import time
from selenium.webdriver.common.action_chains import ActionChains

def password():
    li = []

    while 1:
        ch = msvcrt.getch()
        #回车
        if ch == b'\r':
            msvcrt.putch(b'\n')
            p=('%s' % b''.join(li).decode())
            break
        #退格
        elif ch == b'\x08':
            if li:
                li.pop()
                msvcrt.putch(b'\b')
                msvcrt.putch(b' ')
                msvcrt.putch(b'\b')
        #Esc
        elif ch == b'\x1b':
            break
        else:
            li.append(ch)
            msvcrt.putch(b'*')
    return p


username=input("账号：\n")
print('密码：')
password=password()
subjects=input("所选课程编号：\n")
subjects=subjects.split(' ')
subjects.sort()
try:
    driver = webdriver.Chrome()
except:
    driver = webdriver.Edge()
url = 'http://onestop.ucas.ac.cn/'
driver.get(url)
elem=driver.find_element_by_xpath("//input[@id='menhuusername']")
elem.send_keys(username)
elem=driver.find_element_by_xpath("//input[@id='menhupassword']")
elem.send_keys(password)
elem=driver.find_element_by_xpath("//div[@class='loginbtn']")
elem.click()
time.sleep(1)
try:
    elem=driver.find_element_by_xpath("//a[@title='选课系统']/h5/i")
except:
    print('账号或密码有误！\n')
    exit()
elem.click()
elem=driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]//span")
elem.click()
time.sleep(1)
elem=driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/ul//li[1]/a")
elem.click()
time.sleep(1)
while True:
    try:
        elem=driver.find_element_by_xpath("//form[@id='regfrm2']/div/button")
        elem.click()
        time.sleep(1)
        elem=driver.find_element_by_xpath("//thead/tr/th[13]")
    except:
        elem=driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/ul//li[2]/a")
        elem.click()
        time.sleep(0.5)
        elem=driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/ul//li[1]/a")
        elem.click()
        time.sleep(0.5)
    else:
        break
i=0
for subject in subjects:
    ii=i
    j=0
    while True:
        ii+=1
        path='//tr['+str(ii)+']/td[5]/a/span'
        try:
            elem=driver.find_element_by_xpath(path)
            driver.execute_script('arguments[0].scrollIntoView();', elem)
        except:
            j=1
            print('课程编号'+subject+'有误！\n')
            break
        if elem.text==subject:
            i=ii
            break
    if j==0:
        path='//tr['+str(ii)+']/td[1]/input'
        elem=driver.find_element_by_xpath(path)
        driver.execute_script("$(arguments[0]).click()",elem)
    j=0
elem=driver.find_element_by_xpath("//button[@type='submit']")
driver.execute_script('arguments[0].scrollIntoView();', elem)
driver.execute_script("$(arguments[0]).click()",elem)
