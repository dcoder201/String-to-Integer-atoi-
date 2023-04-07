class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
    # check for sign character
        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
         sign = -1 if s[0] == '-' else 1
         s = s[1:]
    # read digits
        digits = []
        for c in s:
         if c.isdigit():
            digits.append(c)
         else:
            break
        if digits:
         num = int(''.join(digits)) * sign
        else:
         num = 0
       # clamp to 32-bit signed integer range
        if num < -2**31:
         num = -2**31
        elif num > 2**31 - 1:
         num = 2**31 - 1
        return num
