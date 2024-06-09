"""Challege Problems"""

#2. Given an integer x, return true if x is a palindrom, and false otherwise. 

# example: input: x = 121, output: true

def isPalindrome(x): 
    """x is an int, and the outcome is a boolean. a palindrome is the same left to right, as right to left."""

    #x = 121
    #x is a aplindrome, bc it reads the same right to left, as left to right. 
    
    #change int to str as an iterable 
    #go backwards on the iterable and see if it is equivalent to the string of x

    str_x = str(x) #change data type of x from integer (int) to string (str)

    return str_x == str_x[::-1] #we can go directly to the return, because if we set it up this way to check equivalency, it'll return a boolean value, which is our target for the outcome. in this return statement, we are checking the string data type of x to the string data type of x backward to see if they are the same, since that's the definition of a palindrome. [::-1] is no start or stop identified, but then the step is by 1 and going from the last item of the data type that's iterable to the front -- so if we have 121 as the int, it's "121" as a string, and we check the value at index 2, then the value at index 1, then the value at index 0 as the value checked by equivalency on the right side of the equation in the return statement.  


#1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def twoSum(nums, target):
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