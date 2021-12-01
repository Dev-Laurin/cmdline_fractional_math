from fractional_math.fractional_math import calculate

class Test_simple_whole_math():
    def test_two_nums(self):
        assert "2" == calculate("1 + 1").toString()

    def test_three_nums(self):
        assert "1" == calculate("1 * 1 * 1").toString()

    def test_order_of_ops(self):
        assert calculate("2 + 2 * 2").toString() == "6"

class Test_simple_mixed_fractional_math():
    def test_add(self):
        assert calculate("1/2 + 3_1/4").toString() == "3_3/4"

    def test_mult(self):
        assert calculate("1/2 * 5_4/7").toString() == "2_11/14"

    def test_div(self):
        fraction = calculate("1/2 / 2_3/4")
        assert fraction.toString() == "2/11"
        assert fraction.wholenum == None 
        assert fraction.numerator == 2 
        assert fraction.denominator == 11

    def test_sub(self):
        assert calculate("3/4 - 3_5/6").toString() == "-3_1/12"

    def test_example(self):
        assert calculate("1/2 * 3_3/4").toString() == "1_7/8"

    def test_example2(self):
        assert calculate("2_3/8 + 9/8").toString() == "3_1/2"

class Test_simple_fractional_math():
    def test_add_ret_whole(self):
        assert calculate("1/2 + 1/2").toString() == "1"

    def test_add_ret_mixed(self):
        assert calculate("2/2 + 1/2").toString() == "1_1/2"
    
    def test_add_ret_frac(self):
        assert calculate("3/6 + 1/6").toString() == "2/3"