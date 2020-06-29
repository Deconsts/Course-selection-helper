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
schools=input("选择学院编号：\n（数学910、物理911、天文957、化学912、材料928、生命913、地球914、资环921、计算机951、电子952、工程958、经管917、公共管理945、人文927、马克思主义964、外语系915、中丹954、国际955、存济医学院959、体育教研室946、微电子961、未来技术962、网络空间安全963、心理学968、人工智能969、纳米970、艺术中心971、光电972、创新创业967、核学院973、农业974、化学工程975、海洋976、航空宇航977）\n")
schools=schools.split(' ')
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
    for school in schools:
        try:
            path="//form[@id='regfrm2']//input[@id='id_"+school+"']"
            elem=driver.find_element_by_xpath(path)
            elem.click()
        except:
            print('学院编号'+school+'有误！\n')
    try:
        elem=driver.find_element_by_xpath("//form[@id='regfrm2']//button")
        driver.execute_script('arguments[0].scrollIntoView();', elem)
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
