#!/cygdrive/d/python2718/python

"""
PaperTest from Navico to design a class repsenting a line segment
Version: 1.0
Author:  peter.zhang
Date:    16/07/2020
"""

import sys
import unittest

class LineSegment:
    """ A class to repsent line segment in 2-D world """

    @staticmethod
    def _validate(value, lower_range, upper_range=None): 
        """ Class static internal function to valiate input with range
            With lower range exclusive while upper range inclusive
        """
        tmpVal = float(value)
        if tmpVal <= lower_range:
            raise ValueError('Input {0} must be greater '
                             'than {1}'.format(tmpVal, lower_range))
        if upper_range is not None and tmpVal > upper_range:
            raise ValueError('Input {0} must be equal or smaller '
                             'than {1}'.format(tmpVal, upper_range))
        return tmpVal

    def __init__(self, slope=1, length=1):
        self._slope = LineSegment._validate(slope, 0, 180)
        self._length = LineSegment._validate(length, 0)

    def get_slope(self):
        """ Get the slope of a segment """
        return self._slope

    def get_length(self):
        """ Get the length of a segment """
        return self._length

    def is_parallel(self, another_segment):
        """ Compare if two segments are parallel """
        return self._slope == another_segment.get_slope()

    def is_perpendicular(self, another_segment):
        """ Compare if two segments are perpendicular """
        return abs(self._slope - another_segment.get_slope()) == 90
      
class TestLineSegment(unittest.TestCase):
    """ Test Class """

    def _test_get_func(self, func, test_data_list, is_pos_test):
        for test_data in test_data_list:
            print 'Start to valiate ' + str(test_data) 
            arg_dict = {func : test_data} # construct keyword parameters
            if is_pos_test:
                self.assertEquals(getattr(LineSegment(**arg_dict), 'get_' + func)(),
                                  test_data)
            else:
                with self.assertRaises(ValueError):
                    LineSegment(**arg_dict)

    def test_slope_pos(self):
        """ Test slope value could be fetched successfully """
        #1e-323 is the smallest pos in my sys
        #180-1e-9 is the nearest pos value smaller than 180 in my sys
        self._test_get_func('slope',
                            [1, 90, 180, 1e-323, 90.00, 180-1e-9], True)

    def test_slope_neg(self):
        """ Test exception raises if slope value is not illegal """
        self._test_get_func('slope', [-1, 0, 181, sys.float_info.max], False)

    def test_length_pos(self):
        """ Test length value could be fetched successfully """
        self._test_get_func('length',
                            [1, 1e-323, sys.maxint, sys.float_info.min, sys.float_info.max],
                            True) 

    def test_length_neg(self):
        """ Test exception raises if length value is not illegal """
        self._test_get_func('length', [-1, 0], False) 

    def test_is_parallel(self):
        """ Test if two line segments could be considerd as parallel"""
        self.assertTrue(LineSegment(1, 1).is_parallel(LineSegment(1,1)))
        self.assertTrue(LineSegment(1, 1).is_parallel(LineSegment(1,100)))
        self.assertTrue(LineSegment(90, 1).is_parallel(LineSegment(90,100)))
        self.assertFalse(LineSegment(2, 1).is_parallel(LineSegment(1,1)))

    def test_is_perpendicular(self):
        """ Test if two line segments could be considerd as perpendicular"""
        self.assertTrue(LineSegment(30, 1).is_perpendicular(LineSegment(120,1)))
        self.assertTrue(LineSegment(120, 1).is_perpendicular(LineSegment(30,1000)))
        self.assertTrue(LineSegment(180, 1).is_perpendicular(LineSegment(90,100)))
        self.assertFalse(LineSegment(1, 1).is_perpendicular(LineSegment(11,1)))

if __name__ == '__main__':
    unittest.main()
