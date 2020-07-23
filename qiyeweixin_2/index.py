from selenium_3.page.add_member import AddMember
from selenium_3.page.base_page import BasePage


class Index(BasePage):
    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(".index_service_cnt_itemWrap").click()
        # 对AddMember实例化
        return AddMember(self.driver)

    def goto_import_address(self):
        pass

    def goto_member_join(self):
        pass