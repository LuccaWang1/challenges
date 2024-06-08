"""Challege Problems"""


#1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dict = {} #initialize the dictionary 

        for i, num in enumerate(nums): #iterating through the list of nums
            compliment = target - num #calculate the compliment, the difference, or the number complimenting the num to reach the target 

            if compliment in dict: #o(1) look up variable num as key in dictionary
                return [dict[compliment], i] #return the indices of the compliment and the current number
            
            dict[num] = i #add the current number and its index to the dictionary