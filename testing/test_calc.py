# 导入库
import pytest
import yaml

from python_code.calc import Calc


# 定义测试计算器类
class TestCalc:
    # 测试初始化
    def setup_class(self):
        print("测试用例执行开始！")
        self.calc = Calc()

    # 测试结束执行
    def teardown_class(self):
        print("测试用例执行结束！")

    # 参数化用例，从yaml文件中读取测试数据
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("./test_add_data.yml", encoding="utf-8")))
    # 定义加法测试方法
    def test_add(self, a, b, expect):
        # 获取被测类方法执行结果
        result = self.calc.calc_add(a, b)
        # 结果断言，看结果是否正确
        assert result == expect

    # 参数化用例，从yaml文件中读取测试数据
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("./test_div_data.yml", encoding="utf-8")))
    # 定义除法测试方法
    def test_div(self, a, b, expect):
        # 获取被测类方法执行结果
        result = self.calc.calc_div(a, b)
        # 结果断言，看结果是否正确
        assert result == expect


# 入口
if __name__ == '__main__':
    # 调用pytest执行用例
    pytest.main()
