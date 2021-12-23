import pytest
from yaml_util import YamlUtil
from request import request
import requests

class TestApi:

    # @pytest.mark.parametrize(argnames="arg",argvalues=[1,2,3])
    # def test_02(self,arg):
    #     print(arg)


    @pytest.mark.parametrize("args", YamlUtil("api_test.yaml").read_yaml())
    def test_01(self, args):
        # requests.get(args["request"]["url"])
        request(args)
        TestApi.data = args

    # def test_02(self):
    #     # requests.get(args["request"]["url"])
    #     print(TestApi.data)

if __name__ == '__main__':
    pytest.main()