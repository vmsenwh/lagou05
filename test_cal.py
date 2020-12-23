
import pytest
from pythoncode.calculator import Calculator
import yaml
import log


def get_datas():
    with open('./testdata.yml') as f:
        datas = yaml.safe_load(f)
        log.logger.debug(datas)
        add_datas = datas['datas']
        add_ids = datas['ids']
        return [add_datas,add_ids]


class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    def setup_method(self):
        log.logger.debug("\nsetup_module:【开始计算】")

    def teardown_method(self):
        log.logger.debug("\nsetup_module:【结束计算】")

    #  使用参数化
    @pytest.mark.parametrize("a,b,expect",get_datas()[0][0],ids=get_datas()[1][0])
    # 测试add函数
    def test_add(self,a,b,expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a,b)
        # 判断result结果是否等于期望的值
        assert result == expect
        log.logger.debug({f"预期结果：{result}"})

    # 测试sub函数
    @pytest.mark.parametrize("a,b,expect",get_datas()[0][1],ids=get_datas()[1][1])
    def test_sub(self,a,b,expect):
        # 调用sub函数，返回的结果保存在result里面
        result = self.calc.sub(a,b)
        assert result == expect
        log.logger.debug({f"预期结果：{result}"})

    # 测试mul函数
    @pytest.mark.parametrize("a,b,expect",get_datas()[0][2],ids=get_datas()[1][2])
    def test_mul(self,a,b,expect):
        # 调用mul函数，返回的结果保存在result里面
        result = self.calc.mul(a,b)
        assert result == expect
        log.logger.debug({f"预期结果：{result}"})

    # 测试div函数
    @pytest.mark.parametrize("a,b,expect",get_datas()[0][3],ids=get_datas()[1][3])
    def test_div(self,a,b,expect):
        # 调用div函数，返回的结果保存在result里面
        result = self.calc.div(a,b)
        assert result == expect
        log.logger.debug({f"预期结果：{result}"})


if __name__ == '__main__':
        pytest.main(['test_cal.py','-sq'])
