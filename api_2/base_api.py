from string import Template

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    # 企业id
    corpid = "ww6b880a6a2a8988f6"

    def send_url(self, data):
        return requests.request(**data).json()

    # 获取token，secret每个模块的id
    def get_token(self, secret):
        token_data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": self.corpid,
                "corpsecret": secret

            }
        }
        return self.send_url(token_data)

    # 提升为classmethod后，实例可以用，类也可以用
    @classmethod
    def jsonPath(cls, json, expr):
        return jsonpath(json, expr)

    @classmethod
    def loadyaml(cls, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    @classmethod
    def template(cls, path, data, sub=None):
        with open(path, 'r') as f:
            # 如果yaml文件中只有一个配置
            if sub is None:
                # 直接用data中的数据替换f.read读出来的内容,然后返回yaml格式的内容。yaml中"$xxx"代表匹配的内容
                return yaml.load(Template(f.read()).substitute(data))
            # 如果有多个配置
            else:
                return yaml.load(
                    Template(
                        yaml.dump(
                            # 只选取sub相关的配置
                            yaml.load(f)[sub])).substitute(data)
                )