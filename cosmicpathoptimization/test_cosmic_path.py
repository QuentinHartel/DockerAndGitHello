import unittest
import cosmic_path

class test_cosmic_path(unittest.TestCase):
    def test_calculate_mean_case1(self):
        test_temps = [10, 11, 12]
        self.assertEqual(cosmic_path.calculate_mean(test_temps, 3), 11)


    def test_calculate_mean_case2(self):
        test_temps = [100, 130 , 150]
        self.assertEqual(cosmic_path.calculate_mean(test_temps, 3), 126)


    def test_calculate_mean_case3(self):
        test_temps = [10]
        self.assertEqual(cosmic_path.calculate_mean(test_temps, 1), 10)


    def test_calculate_mean_case4(self):
        test_temps = [12, 15, 14, 16, 20]
        self.assertEqual(cosmic_path.calculate_mean(test_temps, 5), 15)


    def test_calculate_mean_case5(self):
        test_temps = [3, 5, 8]
        self.assertEqual(cosmic_path.calculate_mean(test_temps, 3), 5)


    def test_calculate_mean_case6(self):
        test_temps = [152, 143, 165, 170, 132, 166, 147]
        self.assertEqual(cosmic_path.calculate_mean(test_temps, 7), 153)