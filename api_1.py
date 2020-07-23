import json
import pytest
import requests


class TestDepartment:
    ID = 'wwb1ddeb81fc3c9d4b'
    SECRETE = 'BlNz4PGgNN_mZ81AixmbAj-eYnPek2jGa9Hs4bOqtqw'

    def setup(self):
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.ID}&corpsecret={self.SECRETE}')
        self.access_token = r.json()['access_token']
        print(r.json()['access_token'])

    @pytest.mark.parametrize('name, parentid',
                             [('技术中心', 1), ('财务中心', 2)])
    def test_create_department(self, name, parentid):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}'
        data = {
            'name': name,
            'parentid': parentid
        }

        r = requests.post(url=url, data=json.dumps(data))
        assert r.json()['errcode'] == 0

    def test_get_department(self, userid=None):
        url = r'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}}'
        if userid is not None:
            url = url + f'userid={userid}'
        r = requests.get(url=url)
        print(r.json())
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("id, name, name_en",
                             [(1, "技术中心", None), (2, "财务中心", "caiwu")])
    def test_update_department(self, id, name, name_en):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}'
        data = {'id': id}
        if name is not None:
            data['name'] = name
        if name_en is not None:
            data['name_en'] = name_en

        r = requests.post(url=url, json=data)
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("id", [2, 3])
    def test_delete_department(self, id):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id={id}'

        r = requests.get(url=url)
        assert r.json()['errcode'] == 0


if __name__ == '__main__':
    pytest.main()