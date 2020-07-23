from selenium.webdriver.common.by import By

from selenium_3.page.base_page import BasePage


class AddMember(BasePage):
    # 在添加成员页面实现输入内容并保存
    def add_member(self):
        self.driver.find_element_by_id("username").send_keys("abcde")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("fffff")
        self.driver.find_element_by_id("memberAdd_phone"). \
            send_keys("12345678910")
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    def get_first(self):
        # 获得新添加的成员
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "#member_list tr:nth-child(1) "
                                        "td:nth-child(2)").get_attribute(
            "title")