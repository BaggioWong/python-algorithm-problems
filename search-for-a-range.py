class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        The original problem can be found here: 
        https://leetcode.com/problems/search-for-a-range/

        The problem asks to locate the index range of a target element in an integer 
        array sorted in ascending order. 

        The intuition behind the solution is simply to start on both ends of the array
        and to stop when one of the conditions are met: 
        - If the left_pointer == target AND right_pointer == target (range is found)
        - If there is a match from the left_pointer AND left_pointer == right_pointer
        OR there is a match from right_pointer AND left_pointer == right_pointer
        - If no match is identified from the left or the right, and 
        right_pointer < left_pointer (entire array traversed)

        Cases with empty and single element arrays are treated separately as seen below. 
        """
        # set two indicies to traverse array
        arr_len = len(nums)

        # special case: if array has no elements
        if arr_len == 0:
        	return [-1, -1]

        # special case: if array has one element
        if arr_len == 1:
        	curr_num = nums[0]
        	if target == curr_num:
        		return [0, 0]
        	else:
        		return [-1, -1]

        left_index = 0				# current left, right indicies in for loop
        right_index = arr_len - 1

        left_match_index = 0 	# record matched left and right indicies
        right_match_index = 0

        left_value = 0 	# for debugging, record values
        right_value = 0

        left_hit = False # invariants to control left and right index processing
        right_hit = False

        for index, num in enumerate(nums):        	
        	left_index = index
        	right_index = arr_len - index - 1

        	# if right_index < left_index, return [-1, -1]
    		if not left_hit and not right_hit and right_index < left_index:
    			return [-1, -1]

        	if not left_hit:
	        	left_value = num

	        	# if a pointer matches target, record value
	        	if left_value == target:
	        		left_hit = True
	        		left_match_index = left_index
	        else:
	        	# if two pointer indicies are the same, then return [index, index]
	        	if left_match_index == right_index:
	        		return [left_match_index, left_match_index]

	        if not right_hit:
	        	right_value = nums[right_index]

	        	if right_value == target:
	        		right_hit = True
	        		right_match_index = right_index
	        else:
	        	# if two pointer indicies are the same, then return [index, index]
	        	if right_match_index == left_index:
	        		return [right_match_index, right_match_index]

			# if both values are recorded, return [left_index, right_index]
        	if left_hit and right_hit:
        		return [left_match_index, right_match_index]

solution = Solution()

print solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
print solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=9)
print solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=5)
print solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=10)


	        