# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API 
# demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping 
# any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is 
# written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

# Examples
# RomanNumerals.to_roman(1000) # should return 'M'
# RomanNumerals.from_roman('M') # should return 1000
# Help
# Symbol	Value
#   I	      1
#  IV	      4
#   V	      5
#   X	     10
#   L    	 50
#   C	    100
#   D   	500
#   M	   1000

class RomanNumerals:

    @classmethod
    def to_roman(self, val):
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        num = ''
        for key, values in roman.items():
            if 1<=val < 4000:
                num += values * (val//key)
                val = val%key
            else: break
        return num

    @classmethod
    def from_roman(self, roman_num):
        roman = {900: 'CM', 1000: 'M', 400: 'CD', 500: 'D', 90: 'XC', 100: 'C', 40: 'XL', 50: 'L', 9: 'IX', 10: 'X', 4: 'IV', 5: 'V', 1: 'I'}
        num = 0
        for key, value in roman.items():
            if value in roman_num:
                num += key * roman_num.count(value)
                roman_num = roman_num.replace(value, '')
        return num

print(RomanNumerals.to_roman(1990))
print(RomanNumerals.from_roman('MMMCXXII'))

    
