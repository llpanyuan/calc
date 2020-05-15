import pytest
import yaml

from python_code.calc import Calc


class TestCalc:
    def setup_class(self):
        print("测试用例执行开始！")
        self.calc = Calc()

    def teardown_class(self):
        print("测试用例执行结束！")

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("./test_add_data.yml", encoding="utf-8")))
    def test_add(self, a, b, expect):
        result = self.calc.calc_add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',yaml.safe_load(open("./test_div_data.yml",encoding="utf-8")))
    def test_div(self,a,b,expect):
        result = self.calc.calc_div(a,b)
        assert result == expect


if __name__ == '__main__':
    pytest.main()

