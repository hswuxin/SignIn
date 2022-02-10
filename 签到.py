# Made By 凌昀
from selenium import webdriver
import time
import sys
import os

times = 0
print('欢迎使用签到软件v2.2 by热心市民沈先生\n\n\n\n')
while 1:

    try:
        wd = webdriver.Chrome('C://SignIn/chromedriver.exe') #./chromedriver.exe
        wd.set_window_size(1280, 10000)
        wd.implicitly_wait(5)
        wd.get('http://ehall.hytc.edu.cn/new/index.html')

        wd.find_element_by_id('ampHasNoLogin').click()  # 查找原始登陆按钮并单击
        time.sleep(3)

        wd.find_element_by_name('login').click()
        time.sleep(2)
        if os.path.exists('C://SignIn/配置数据.rin'):
            with open('C://SignIn/配置数据.rin', 'r') as File:
                Line = File.readlines()
                nm = Line[0]
                pw = Line[1]
                File.close()
        else:
            os.system('cls')
            print('首次启动需要输入账号、密码')
            print('此后如需修改只要删除同目录下“配置数据.rin”便可清除密码重新输入')
            print('')
            print('请输入账号：', end='')
            nm = input()
            print('请输入密码：', end='')
            pw = input()
            with open('C://SignIn/配置数据.rin', 'w') as f:
                f.write(nm)
                f.write('\n')
                f.write(pw)
                f.close()
        username = wd.find_element_by_id('username')  # 查找输入框
        username.send_keys(nm)
        password = wd.find_element_by_id('password')
        password.send_keys(pw)

        wd.find_element_by_name('login').click()  # 单击登陆
        time.sleep(5)  # new
        qiandao = wd.find_elements_by_class_name(
            'widget-title.appTitleFlag.style-scope.pc-card-html-4786697535230905-01')  # 进入提交页面
        qiandao[7].click()
        wd.find_element_by_id('ampDetailEnter').click()

        windows = wd.window_handles  # 切换窗口
        wd.switch_to.window(windows[-1])
        
        # time.sleep(1)  # new
        # xuesheng = wd.find_elements_by_class_name('bh-btn.bh-btn-primary.bh-btn-block.waves-effect')
        # xuesheng[-1].click()  # 学生组
        #
        # time.sleep(9)  # new
        
        wd.implicitly_wait(180) #等待最多180秒至加载完毕
        
        fillform = wd.find_elements_by_class_name('jqx-dropdownlist-content.jqx-disableselect')

        benren = fillform[6]  # 填写本人健康状态信息
        benren.click()
        time.sleep(2)
        zhengchang1 = wd.find_elements_by_css_selector('[role="option"] > span')
        zhengchang1[-2].click()
        time.sleep(2)

        jiuzhen = fillform[7]  # 填写是否就诊信息
        jiuzhen.click()
        time.sleep(2)
        zhengchang2 = wd.find_elements_by_css_selector('[role="option"] > span')
        zhengchang2[-1].click()
        time.sleep(2)

        jiating = fillform[8]  # 填写家庭成员健康情况信息
        jiating.click()
        time.sleep(2)
        zhengchang3 = wd.find_elements_by_css_selector('[role="option"] > span')
        zhengchang3[-2].click()
        time.sleep(2)

        xinli = fillform[9]  # 填写心理状况信息
        xinli.click()
        time.sleep(2)
        zhengchang4 = wd.find_elements_by_css_selector('[role="option"] > span')
        zhengchang4[-8].click()
        time.sleep(2)

        tiwen = wd.find_element_by_css_selector('[name="TW"]')  # 填写体温信息
        tiwen.send_keys('36.7')

        wd.find_element_by_id('save').click()
        time.sleep(4)
        wd.quit()
        sys.exit(0)

    except:
        ck = wd.find_elements_by_css_selector('[data-action="编辑"]')
        if len(ck) == 1:
            os.system('cls')
            print('填报已完成')
            time.sleep(5)
            wd.quit()
            sys.exit(0)
        else:
            wd.quit()
            os.system('cls')
            print('发生错误，请检查账号密码或网络')
            times += 1
            print('5秒之后进行第' + str(times) + '次重试')
            time.sleep(5)