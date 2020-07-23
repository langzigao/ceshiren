from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAdd:
    """
    课后作业1：
    将课上的添加联系人，自己编写一条用例
    使用参数化，添加多条用例
    注意：添加联系人的姓名以固定字符开头，例如：测试name1，测试name2，测试name3
    """

    def setup_class(self):
        desired_caps = {
            'platformName': 'android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.WwMainActivity',
            'noReset': True,
            'autoGrantPermissions': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(6)
        # 进入通讯录
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("通讯录")').click()
        # 滑动查找添加成员并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable('
                                                              'new UiSelector().scrollable(true)'
                                                              '.instance(0)).scrollIntoView(new UiSelector()'
                                                              '.text("添加成员").instance(0));').click()

    @pytest.mark.parametrize('name, sex, phone', [
        ('测试成员1', '女', '13500000001'),
        ('测试成员2', '男', '13500000002'),
        ('测试成员3', '女', '13500000003')
    ])