import pytest

@pytest.fixture(scope="",params=["asd","fgh","fg"],ids=["asd","fgh","fg"])
def my_fixture():
    pass
#     前置方法
    yield
#     后置方法

@pytest.fixture(scope="",params=["asd","fgh","fg"])
def my_fixture2(request):
    pass
    #     前置方法

    yield request.param
    #     后置方法

class TestLogin:

    def setup_class(self):
        pass
    # 在每个类执行之前执行

    def setup(self):
        pass
    # 在每个测试用例执行之前执行

    def teardown_class(self):
        pass
    # 在每个类执行之前执行

    def teardown(self):
        pass
    # 在每个测试用例执行之前执行

    @pytest.mark.smoke
    def test_01_li(self):
        print("asd")

    @pytest.mark.parametrize(argnames="arg",argvalues=[1,2,3])
    def test_02(self,arg):
        print(arg)

    @pytest.mark.parametrize(argnames="name,id", argvalues=[[1,1.2],[2,2.1]])
    def test_02(self, name,id):
        print(name,id)

if __name__ == '__main__':
    pytest.main()