# Naomi Tesla
# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def str_list(string):
            list1 = []
            list1[:0] = string
            return list1

        def dict_replace(roman):
            buffer = 0
            last_num = 1001
            for roman_num in roman:
                number = roman_nums[roman_num]
                if number > last_num:
                    buffer -=  last_num*2
                    buffer += number
                else:
                    buffer += number
                last_num = number
            return buffer

        roman_nums = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        list_roman = str_list(s)
        result = dict_replace(list_roman)
        return result