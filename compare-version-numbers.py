class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int

        The original problem can be found here: 
        https://leetcode.com/problems/compare-version-numbers

        The question asks to compare whether two version numbers are the same
        given two strings. 

        My implementation to the standard case assuming a regular number simply
        compares each revision number until the end is reached. If both version
        strings are not of equal length, zeroes are appended such that they are
        of equal length. 

        Special consideration needs to be paid when there are trailing zeroes, 
        which need to be stripped off. 
        """

        # handle special cases where there are trailing zeroes (at beginning and end)
        version1_strip_zeroes = version1.lstrip("0").rstrip("0")
        version2_strip_zeroes = version2.lstrip("0").rstrip("0")

        # split up the two strings by dot into two arrays
        version1_nums = version1.split(".")
        version2_nums = version2.split(".")

        # record length of two arrays
        version1_len = len(version1_nums)	
        version2_len = len(version2_nums)

        # for the shorter array, append zeroes at the end (non foreach loops are considered "non-pythonic"?)
        if version1_len < version2_len:
        	for _placeholder in range(version2_len - version1_len):
        		version1_nums.append("0")
        elif version2_len < version1_len:
        	for _placeholder in range(version1_len - version2_len):
        		version2_nums.append("0")

        print version1_nums
        print version2_nums

        # take the lower bound of the two arrays as the for loop limit
        loop_limit = min(version1_len, version2_len)

        # compare each digit in each position to see which one is greater
        for num1, num2 in zip(version1_nums, version2_nums):

        	# if version1 > version2, return 1
        	if int(num1) > int(num2):
        		return 1

        	# if version2 > version1, return -1
        	elif int(num2) > int(num1):
        		return -1

        # last iteration of array and they're both the same (exited loop)
        return 0

solution = Solution()

print solution.compareVersion("1", "01")
print solution.compareVersion("2.1.53.6", "2.1.53.6")
print solution.compareVersion("2.1.53.6", "2.1.48.2.6")
print solution.compareVersion("2.1.53.6", "2.1.53.5")
print solution.compareVersion("2.1.53.6", "2.1.53.6.6")