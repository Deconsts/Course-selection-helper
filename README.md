# Course-selection-helper
Designed for UCAS course selection system
UCAS抢课程序

## 环境要求
可执行文件（\exe\dist\course.exe）可以在Windows系统下执行  
Python版本为3.7.2（注意，代码无法在解释器中正确运行，必须在命令行中才能输入密码）  
需要Google Chrome浏览器（优先）或者Microsoft Edge浏览器才能运行

## 可执行文件使用说明
按照提示依次输入账号、密码、选课编号以及选课学院  
其中选课编号和学院可以输入多个，以空格隔开，以回车结束  
建议在选课前三分钟内打开  
选课过程由软件自动控制浏览器完成，直到最后的提交确认按钮结束，提交确认按钮需要手动点击

## 注意事项
1、软件控制的浏览器被打开以后，请将其最大化，避免因为窗口过小导致错误操作  
2、程序会在运行界面给出选课结果，如果课程编号或者选课学院不存在会给出报错信息，将其忽略并继续完成其他选课  
3、浏览器自动控制期间，随时可以将其打断，变为手动操作，打断方式包括但不限于关闭程序界面、将网页窗口拉到最小、点击其他链接，如果你希望软件正确运行，请不要做这些事情

## 版本更新记录
v1.1 修复了课程编号输入错误闪退的问题 2019.7.18  
v1.2 优化了选课时间未到的逻辑 2019.7.22  
v1.3 优化了密码输入效果 2019.8.19  
v1.4 优化了课程较多时的选课速度，并增加了出错时的提示 2019.8.25  
v1.5 整合程序，并支持edge浏览器 2019.8.26  
v1.6 添加对学院的选择 2020.6.29
v1.7 修复了在个别浏览器中因显示问题导致的报错，并且通过了实际使用的测试 2020.6.30

## 备注
此程序不计划继续更新，一年前的代码风格比较差，而且浏览器、网络等条件会导致很多不确定性因素。后续计划调研选课程序的web版。
2020.6.30

## 联系方式
deconst720@gmail.com
