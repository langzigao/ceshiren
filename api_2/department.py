from api.base_api import BaseApi


class Department(BaseApi):

    def __init__(self):
        self.token = self.get_token("Du2nvVZHl_gbjePd6NgbfQgBbP4GxXEBMJXr6F0CiUg")['access_token']

        # 获取部门列表

    def get_demprt_list(self, **data):
        # data = {
        #     "method": "get",
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
        #     "params": {
        #         "access_token": self.token
        #     }
        # }
        # 如果传进来的data有值，可以和后面的进行拼接。
        data.update({"token": self.token})
        data = self.template('../api/depart_all.yaml', data, sub='get')
        return self.send_url(data)

    # 增加部门
    def add_demprt(self, **data):
        # data = {
        #     "method": "post",
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
        #     "params": {
        #         "access_token": self.token,
        #
        #     },
        #     "json" : {
        #         "name": name,
        #         "parentid": 1,
        #         "order": 2,
        #         "id": num
        #     }
        # }

        data.update({"token": self.token})
        data = self.template('../api/depart_all.yaml', data, sub='add')
        return self.send_url(data)

    # 修改部门
    def edit_demprt(self, **data):
        # data = {
        #     "method": "post",
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update",
        #     "params": {
        #         "access_token": self.token,
        #     },
        #     "json" : {
        #         "id": num,
        #         "name": name
        #     }
        # }
        data.update({"token": self.token})
        data = self.template('../api/depart_all.yaml', data, sub='update')
        return self.send_url(data)

        # 删除部门

    def del_demprt(self, **data):
        # data = {
        #     "method": "get",
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
        #     "params": {
        #         "access_token": self.token,
        #         "id": num
        #
        #     }
        # }
        data.update({"token": self.token})
        data = self.template('../api/depart_all.yaml', data, sub='delete')
        return self.send_url(data)