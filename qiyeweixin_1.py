import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
selenium使用w3c规定的webdriver协议将命令发送出去
'''


class TestWecat:
    '''
    - 通过chrome调试模式命令：chrome -remote-debugging-port=9222，启动调试浏览器
    - 新建chrome参数options, 将本机调试端口参数传入，复用已有的浏览器（调试模式），直接跳过前面的步骤，进入关键步骤
    - 新建chrome浏览器，将配置好的options参数传入浏览器对象
    - 打开浏览器并最大化，设置隐式等待3秒
    - 通过调试模式可以直接进入登录好的状态，获取到cookie=[{"domain": ".work.weixin.qq.com", "httpOnly": false, "name": "wwrtx.vid", "path": "/", "secure": true, "value": "1688850284528427"}, {"domain": ".work.weixin.qq.com", "httpOnly": true, "name": "wwrtx.refid", "path": "/", "secure": true, "value": "19475224753481799"}, {"domain": ".work.weixin.qq.com", "httpOnly": true, "name": "wwrtx.vst", "path": "/", "secure": true, "value": "BicSEKU8MEBfjOzwOqapeTdMJ8kM7CfOlgiPz75bKwjMhd7idn2Rbi-UoJ-2a6YDNVTHakno5EOpNVxEqUN1AFwj7TOvZSFUYCAK0E2n3VKeA8cL6yc4ka65yKxBFBIipTVkSQ_FPIutL5kAEOVdhWHheF_zc8JETDvXX_MvHJ1FdrL5ETaExjPKXvuIvxQlfSKTBz354SWLP7GSHDDcQrvUfDpfRtMDkGNnzeZzuWiET5x_BXiTPVKidyjnX8QcYctvTcht1319oMlGGgwZvQ"}, {"domain": ".work.weixin.qq.com", "httpOnly": false, "name": "wxpay.vid", "path": "/", "secure": true, "value": "1688850284528427"}, {"domain": ".work.weixin.qq.com", "httpOnly": false, "name": "wxpay.corpid", "path": "/", "secure": true, "value": "1970325123121219"}, {"domain": ".work.weixin.qq.com", "httpOnly": true, "name": "wwrtx.sid", "path": "/", "secure": true, "value": "wiij4h256w4FUQRhL9s5MWsHWYDk8PSPefXwgQi0F9p6R11EbJLQQ8s2Q1wG3tWD"}, {"domain": ".work.weixin.qq.com", "httpOnly": false, "name": "Hm_lvt_9364e629af24cb52acc78b43e8c9f77d", "path": "/", "secure": true, "value": "1585656932,1585657951,1585657964,1585662318"}, {"domain": ".qq.com", "httpOnly": false, "name": "_gat", "path": "/", "secure": true, "value": "1"}, {"domain": ".work.weixin.qq.com", "httpOnly": true, "name": "wwrtx.ref", "path": "/", "secure": true, "value": "sites"}, {"domain": ".qq.com", "httpOnly": false, "name": "ptui_loginuin", "path": "/", "secure": true, "value": "476045231"}, {"domain": ".qq.com", "httpOnly": false, "name": "_ga", "path": "/", "secure": true, "value": "GA1.2.1136770173.1585656932"}, {"domain": ".work.weixin.qq.com", "expiry": 1588255487.050997, "httpOnly": false, "name": "wwrtx.i18n_lan", "path": "/", "secure": false, "value": "zh"}, {"domain": ".qq.com", "httpOnly": false, "name": "_gid", "path": "/", "secure": true, "value": "GA1.2.721303322.1585656932"}, {"domain": ".qq.com", "httpOnly": false, "name": "LW_sid", "path": "/", "secure": true, "value": "Z1H5z8Y1O5Q9P889A9c1N6N0y1"}, {"domain": ".qq.com", "httpOnly": false, "name": "ptcz", "path": "/", "secure": true, "value": "88b5b82ab2de9c9bcabb07cd4ba5ff4d786dd95fb62bf38ec198dce9ec87dd9e"}, {"domain": ".qq.com", "httpOnly": false, "name": "RK", "path": "/", "secure": true, "value": "Te5FSo9zfB"}, {"domain": ".work.weixin.qq.com", "httpOnly": false, "name": "wwrtx.d2st", "path": "/", "secure": true, "value": "a8862074"}, {"domain": ".qq.com", "httpOnly": false, "name": "pgv_pvi", "path": "/", "secure": true, "value": "9316420608"}, {"domain": ".work.weixin.qq.com", "httpOnly": true, "name": "wwrtx.ltype", "path": "/", "secure": true, "value": "1"}, {"domain": ".qq.com", "httpOnly": false, "name": "pgv_pvid", "path": "/", "secure": true, "value": "5266567000"}, {"domain": ".work.weixin.qq.com", "httpOnly": false, "name": "wwrtx.logined", "path": "/", "secure": true, "value": "true"}, {"domain": ".qq.com", "httpOnly": false, "name": "eas_sid", "path": "/", "secure": true, "value": "A1w5u7a9k6U0E5H66611V2E8L5"}, {"domain": ".qq.com", "httpOnly": false, "name": "tvfe_boss_uuid", "path": "/", "secure": true, "value": "b159682f22708891"}, {"domain": ".qq.com", "httpOnly": false, "name": "LW_uid", "path": "/", "secure": true, "value": "L1N587W9x6K0I5X676K1g1G8X5"}]
    - 将cookie提取出来，通过json模块直接保存到cookies.txt文档文件中
    - 定位到添加成员按钮并点击，在下面的输入框输入内容

    - 如果在cookie生效时间内登录，那么可以直接读取cookies.txt文件，将其中的验证时间字段删掉，使用对应的cookie登录页面
    '''

    def setup(self):
        # webdriver其中一个参数
        chrome_options = webdriver.ChromeOptions()
        # 设置调试地址，需要与chromedebug地址相同
        chrome_options.debugger_address = '127.0.0.1:9222'
        # 将调试地址参数传入webdriver的参数中
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wecat(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        cookies = self.driver.get_cookies()
        # 将cookies提取出来后存到文档中
        with open('cookies.txt', 'w') as f:
            json.dump(cookies, f)
        # 从对应的文件中读出cookies
        '''
        cookie中的expiry字段保存了cookie的保存时间
        '''
        with open('cookies.txt', 'r') as f:
            cookies: list[dict] = json.load(f)
        for cookie in cookies:
            # 如果cookie验证时间字段在cookie中，则删掉
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # 在浏览器对象中依次添加取得的cookie
            self.driver.add_cookie(cookie)

        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap').click()
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('xixixi')
        self.driver.find_element(By.CSS_SELECTOR, '[name=english_name]').send_keys("xixixi")
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('xixixi')
