from unittest import TestCase
from src.py_ecef.conversions import LLA_to_ECEF
from src.py_ecef.conversions import ECEF_to_LLA

class TestConversions(TestCase):

    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails_sike(self):
        self.assertFalse(False)

    def test_LLA_to_ECEF_washington_dc(self):
        result = LLA_to_ECEF(38.895, -77.0366, 7)
        expected = [1114.845*1000, -4843.976*1000, 3984.31*1000]
        print(result)
        for i in range(len(result)):
            self.assertAlmostEqual(first = result[i], 
                                   second = expected[i],
                                   delta = 1500)
            
    def test_LLA_to_ECEF_lima_peru(self):
        result = LLA_to_ECEF(-12.0454483, -77.0308636, 160)
        expected = [1400.144 * 1000, -6079.627 * 1000, -1322.353 * 1000]

        print(result)

        for i in range(len(result)):
            self.assertAlmostEqual(first = result[i], 
                                   second = expected[i],
                                   delta = 1500) 
            
    def test_ECEF_to_LLA_washington_dc(self):
        result = ECEF_to_LLA(1115061.187564614, -4843975.748654286, 3983255.8837187868)
        expected = [38.895, -77.0366, 7] 
        print(result)
        for i in range(len(result)):
            self.assertAlmostEqual(first = result[i], 
                                   second = expected[i],
                                   delta = 2) 
