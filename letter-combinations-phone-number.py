class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		# special case: if digits is empty
		if len(digits) == 0:
			return []

		combinations = []
		return self.letterCombinationsRecursive(digits, 0, combinations)
        
	def letterCombinationsRecursive(self, digits, current_digit_index, combinations):
		"""
		:type digits: str
		:current_digit_index: int
		:combinations: List[str]
		:rtype: List[str]
		
		The original problem can be found here: 
		https://leetcode.com/problems/letter-combinations-of-a-phone-number/

		The problem asks to create all the combinations of the strings possible 
		based on a given string representing a sequence of keys pressed on a 
		traditional 12-key mobile phone keypad. 

		An unstated assumption treats this problem ignoring the following digits: 
		- 1 (no alphabet letters)
		- * (non alphanumeric)
		- 0 (non alphanumeric)
		- # (non alphanumeric)

		The below implementation is a straightforward recursion. It starts with
		creating strings at with the letters associated with the first digit of 
		the digit string to create the first list of combinations. 

		This, in turn, calls itself to concatenate all these combinations with
		the next digit of the digit string. The base case is reached when the 
		it calls itself wth the last digit of the digit string, representing 
		all the combinations available for that digit string. 

		For an example string "23", a typical run might look something like: 

		['a', 'b', 'c']
		['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

		"""
		len_digits = len(digits)
		combinations_current = []

		_digits_letters = {
			2: ['a', 'b', 'c'],
			3: ['d', 'e', 'f'],
			4: ['g', 'h', 'i'],
			5: ['j', 'k', 'l'],
			6: ['m', 'n', 'o'],
			7: ['p', 'q', 'r', 's'],
			8: ['t', 'u', 'v'],
			9: ['w', 'x', 'y', 'z']
		}
    	
		# add individual letters if it's a single letter
		if current_digit_index == 0:
			current_key_number = int(digits[0])
			for letter in _digits_letters[current_key_number]:
				combinations_current.append(letter)
    	# append to previous iteration of string combinations
		else:
			for string in combinations:
				current_key_number = int(digits[current_digit_index])
				for letter in _digits_letters[current_key_number]:
					combinations_current.append(string + letter)

		# if it's the final number of the string, return
		if current_digit_index == len_digits - 1:
			return combinations_current
		else:
			return self.letterCombinationsRecursive(digits, current_digit_index + 1, combinations_current)


solution = Solution()

solution.letterCombinations(digits="")
solution.letterCombinations(digits="2")
solution.letterCombinations(digits="23")
solution.letterCombinations(digits="2345")
solution.letterCombinations(digits="2349")