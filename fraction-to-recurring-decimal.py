class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str

        The original problem can be found here: 
        https://leetcode.com/problems/fraction-to-recurring-decimal/

        The question states to yield a decimal answer for the division
        between two numbers, and to enclose the recurring part in 
        brackets. 

        My implementation seeks to mimick natural long division. The
        main intuition behind this is to see whether the current 
        remainder has already been divided before, which yields the
        recurrence. We simply keep track of where the recurrence 
        starts, and until the end of the list used to track the
        recurrence represents the entire recurrence sequence. 

        Special consideration is given to the following cases: 
        - The handling of negative numbers (this particular 
        implementation seeks to treat them as positive numbers 
        because it is easier to process. We can also thank the 
        symmetric nature of division and multiplication operators
        between negative and positive numbers.)

        - We also want to differentiate between three main categories
        of calculations:
        	- division that yields a non decimal answer (e.g. 2/1)
        	- division that yields a decimal answer:
        		- that is non-recurring (e.g. 1/2)
        		- that is recurring (e.g. 1/3)

        - Special consideration should be considered paid to 
        division by zero cases, but this was not explicitly stated
        by the question, and is not observed in the below treatment.

        Optimizations could be made to the process. Some ideas are 
        given as follows: 
        - Repeated conditional checks should be taken out of if 
        and stored in a variable

        - Division and modulus operations can be implemented using
        bitwise operators

        I am not familiar with how Python's interpreter works, but 
        I would assume it already does similar optimizations, so the
        actual yield might be little. 

        Another optimization might be to determine whether a pair 
        yields a recurring portion before diving into the bulk of the
        program. However, this is only worth doing if the majority
        of inputs do yield non-recurring results, which defeats the
        purpose of presenting the problem in the first place. 

        But if this could be considered, many input pairs could then
        be reduced to a simple division problem, which is efficiently
        handled by the interpreter. 
        """
        remainders = []
        quotient_digits = []
        quotient_string = ""

        # determine whether the numerator / denominator combination going to yield a recurrence
        divisor = 0
        current_remainder = 0
        current_remainder_in_remainders_index = 0
        
        recurrence_found = False
        first_time = True

        # handling negative numbers
        if numerator < 0 and denominator > 0:
        	divisor = denominator
        	numerator = -numerator
        	revert_negative = True
        	quotient_string += "-" + str(numerator / denominator)

        elif numerator > 0 and denominator < 0:
        	denominator = -denominator
        	divisor = denominator
        	revert_negative = True
        	quotient_string += "-" + str(numerator / denominator)

        elif numerator < 0 and denominator < 0: 
        	denominator = -denominator
        	divisor = denominator
        	numerator = -numerator
        	quotient_string += str(numerator / denominator)

        else:
        	divisor = denominator
        	quotient_string += str(numerator / denominator)

        print numerator, denominator

        # mimick the long division process
        while not recurrence_found: 
        	# calculate remainder and quotient
        	if first_time:
        		print numerator % divisor
        		current_remainder = numerator % divisor * 10
        	else: 
        		current_remainder = current_remainder % divisor * 10

        	current_quotient = current_remainder / divisor

        	# see if remainder has already been processed (indicates recurrence!), exit loop if so
        	try: 
        		current_remainder_in_remainders_index = remainders.index(current_remainder)
        		recurrence_found = True
        		break
        	except ValueError: 
        		None

        	# store remainder and quotient
        	remainders.append(current_remainder)
        	quotient_digits.append(current_quotient)

        	first_time = False 

        # determine whether this division yields a recurrence or not
        decimal_but_no_recurrence = False # 1 / 2

        if len(remainders) == 1 and remainders[0] == 0: # 2 / 1
        	return quotient_string
        else:
        	quotient_string += "."
        	if len(remainders) - 1 == current_remainder_in_remainders_index and remainders[len(remainders) - 1] == 0: # 1 / 2
       			decimal_but_no_recurrence = True

        # process part after the decimal, using the index found above to determine recurrence
        for index, digit in enumerate(quotient_digits):
        	if index != current_remainder_in_remainders_index:
        		quotient_string += str(digit)
        	else:
        		if not decimal_but_no_recurrence:
        			quotient_string += "(" + str(digit)

        	if not decimal_but_no_recurrence and index == len(quotient_digits) - 1:
        		quotient_string += ")"

        return quotient_string

solution = Solution()

# print solution.fractionToDecimal(numerator=0, denominator=0)

print solution.fractionToDecimal(numerator=0, denominator=1)
print solution.fractionToDecimal(numerator=1, denominator=2)
print solution.fractionToDecimal(numerator=216, denominator=3)
print solution.fractionToDecimal(numerator=1, denominator=9)
print solution.fractionToDecimal(numerator=1, denominator=3)
print solution.fractionToDecimal(numerator=1, denominator=-3)
print solution.fractionToDecimal(numerator=-50, denominator=8)
print solution.fractionToDecimal(numerator=7, denominator=-12)
print solution.fractionToDecimal(numerator=217, denominator=17)