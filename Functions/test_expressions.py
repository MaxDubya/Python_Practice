import pytest
import expressions as ex


class TestClass_Sleep_In():

    def test_sleep_in_a(self):
        assert ex.sleep_in(False, False) == True

    def test_sleep_in_b(self):
        assert ex.sleep_in(True, False) == False

    def test_sleep_in_c(self):
        assert ex.sleep_in(False, True) == True


class TestClass_Monkey_Trouble():

    def test_one(self):
        assert ex.monkey_trouble(True, True) == True

    def test_two(self):
        assert ex.monkey_trouble(False, False) == True

    def test_three(self):
        assert ex.monkey_trouble(True, False) == False


class TestClass_In_1020():

    def test_one(self):
        assert ex.in_1020(12, 99) == True

    def test_two(self):
        assert ex.in_1020(21, 12) == True

    def test_three(self):
        assert ex.in_1020(8, 99) == False


class TestClass_Max_End_Three():

    def test_one(self):
        assert ex.max_end_three([1, 2, 3]) == [3, 3, 3]

    def test_two(self):
        assert ex.max_end_three([11, 5, 9]) == [11, 11, 11]

    def test_three(self):
        assert ex.max_end_three([2, 11, 3]) == [3, 3, 3]


class TestClass_Phone_Number():

    def test_one(self):
        assert ex.make_phone_number(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"

    def test_two(self):
        assert ex.make_phone_number(
            [5, 4, 6, 3, 7, 4, 9, 8, 7, 6]) == "(546) 374-9876"

    def test_three(self):
        assert ex.make_phone_number([1087658471]) == "(108) 765-8471"


class TestClass_3_or_5():

    def test_one(self):
        assert ex.multiple_of_3_or_5(5) == True

    def test_two(self):
        assert ex.multiple_of_3_or_5(10) == True

    def test_three(self):
        assert ex.multiple_of_3_or_5(22) == False
