from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDelete:
    """
    课后作业2：
    将名称为 “测试name”开头的所有联系人删除
    循环删除所有 "测试name"开头的联系人
    删除联系人之后，判断删除成功
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
        # 点击管理图标
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gup').click()

    def test_delete(self):
        sleep(3)
        elements = self.driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("测试成员")')
        if len(elements) > 0:
            # 直接循环删除elements，测试成员2总是找不到，所以先把名称保存到数组
            names = []
            for element in elements:
                text = element.text
                print(f"获取到的名字为：{text}")
                names.append(text)

            # 循环要删除的成员名称数组，进行删除操作
            for name in names:
                print(f"执行删除的名字为：{text}")
                # 点击要删除成员所在行的编辑图标
                locator_edit = (MobileBy.XPATH, f'//*[@text="{name}"]/../../../..//*[@resource-id="com.tencent.wework:id/fcq"]')
                self.driver.find_element(*locator_edit).click()

                # 点击删除按钮
                self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/duq').click()

                # 删除弹窗，点击确定删除
                locator_delete = (MobileBy.ID, 'com.tencent.wework:id/b_4')
                WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator_delete))
                self.driver.find_element(*locator_delete).click()

                # 删除需要时间，等待3秒
                sleep(3)

            # 判断是否删除成功
            if len(elements) == 0:
                print("删除成功")

    def teardown_class(self):
        self.driver.quit()