import unittest

import HTMLTestRunner
import time

#构建测试套件
# suite = unittest.TestSuite()

#将测试用例加入测试套件

# suite.addTest(TestHomePage('test_001'))#手动加入测试用例
# suite.addTest(TestHomePage('test_002'))

suite = unittest.defaultTestLoader.discover('./cases/','test_clock_in.py')#构建套件，并扫描指定文件夹将符合规则的TestCase加入套件

#执行测试套件
# runner = unittest.TextTestRunner()#构造一个运行器
test_report = f'./log/test_result%s.html' % (time.strftime('%Y-%m-%d %H %M %S', time.gmtime()))
file = open(test_report, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(file,title='掌上神器',description='babab')#构建HTMLTestRunner的运行器，生成HTML报告

#执行
runner.run(suite)
file.close()#关闭运行流

