import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int (top)
        :type divisor: int (bottom)
        :rtype: int

        The original problem can be found here: 
        https://leetcode.com/problems/divide-two-integers/

        The question asks to divide two numbers without using the 
        multiplication, division or mod operators. 

        To do so, I implemented a solution using bitwise operators
        to imitate long division as done by hand. 

        This implementation assumes operating on a 32-bit machine
        and handles overflows according, as per the following 
        situations: 
        - If either the dividend or the divisor is greater than the
        maxint or smaller than the minint, return maxint 
        - If we have minint / -1, this overflows

        Negative numbers are rendered positive first for processing, 
        and are turned negative if either the dividend or divisor is
        negative.         

        The algorithm mimicks binary long division done by hand: 
        - Iterating bit_difference times (between divisor and divident)
        - For every turn, we define shift_places that starts at 
        bit_difference, and decrements to 0
        - We also define the subtrahend as the divisor * 2 (decimal) ^ 
        shift_places, which is implemented with a left shift
        - We iterate until the current turn observes a subtrahend that
        is smaller than the remainder, in which case we add the 
        appropriate power of 2 to the quotient

        Note: 
        - Subtrahend is the number that is subtracted away from another
        - Quotient is long division's answer
        """
        # overflow cases
        maxint = sys.maxint
        minint = -sys.maxint - 1

        # maxint = pow(2, 31) - 1
        # minint = -pow(2, 31)

        if dividend > maxint or divisor > maxint or dividend < minint or divisor < minint:
        	return maxint

        # if the answer yields an overflow
        if dividend == minint and divisor == -1:
        	return maxint

        # handle negative numbers
        turn_negative = 0

        if dividend < 0 and divisor > 0:
        	dividend = -dividend
        	turn_negative = 1

        if dividend > 0 and divisor < 0:
        	divisor = -divisor
        	turn_negative = 1

        if dividend < 0 and divisor < 0: 
        	divisor = -divisor
        	dividend = -dividend

        # special case: divisor > dividend
        if divisor > dividend: 
        	return 0

        # special case: divisor == dividend
        if divisor == dividend:
        	if turn_negative == 1:
        		return -1 
        	else: 
        		return 1

        # figure out bit place difference between two bit strings
        dividend_str = bin(dividend)
        divisor_str = bin(divisor)

        divisor_len = len(divisor_str) - 2 # 0b is appended to binary strings
        bit_diff = len(dividend_str) - len(divisor_str)

        # number of iterations = bit_difference, 
        remainder = dividend
        quotient = 0

        for incr_index in range(0, bit_diff + 1):
        	shift_places =  bit_diff - incr_index

        	subtrahend = divisor << shift_places

        	if subtrahend <= remainder:
        		remainder = remainder - subtrahend
        		quotient += 1 << shift_places
        	else: 
        		quotient += 0

        if turn_negative == 1:
        	return -quotient
        else:
        	return quotient
        


solution = Solution()

print solution.divide(dividend=15, divisor=3)
print solution.divide(dividend=15, divisor=2)
print solution.divide(dividend=10291, divisor=738)
print solution.divide(dividend=469, divisor=7)

# remember the diff between 32-bit and 64-bit overflow
print solution.divide(dividend=sys.maxint, divisor=sys.maxint-1)
print solution.divide(dividend=sys.maxint-1, divisor=sys.maxint)
print solution.divide(dividend=sys.maxint, divisor=sys.maxint)
print solution.divide(dividend=sys.maxint+1, divisor=sys.maxint)
print solution.divide(dividend=sys.maxint, divisor=sys.maxint+1)
print solution.divide(dividend=(-sys.maxint)-1, divisor=sys.maxint)
print solution.divide(dividend=sys.maxint, divisor=(-sys.maxint)-1)

# print solution.divide(dividend=-1006986286, divisor=-2145851451)


