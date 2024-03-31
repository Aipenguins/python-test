import pytest
import requests

from common.yaml_util import write_yaml


class TestAPI:

    session=requests.session()  # 会话
    def test_get_token(self):
        url="http://api.weixin.qq.com/cgi-bin/token"
        params={
            "grant_type":"client_credential",
            "appid":"wx6b11b3efd1cdc290",
            "secret":"106a9c6157c4db5f6029918738f9529d"
        }
        res = TestAPI.session.request("get",url=url,params=params)

        # 把数据组合成dict字典并写入yaml文件
        extract_data={"access_token":res.json()['access_token']}
        write_yaml(extract_data)
        print(res.text)
        print("commit test")