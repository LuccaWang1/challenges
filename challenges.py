"""Challege Problems"""

#Write a function to find the longest common prefix string amongst an array of string. 

#if there is no common prefix, return an empty string "". 

def longest_common_prefix (strs):
    """
    :type stra: List[str]
    :rtype: str
    """

    #sample strs: strs = ["flower", "flow", "flight"]

    if not strs: #edge case: if the array is empty, return an empty str
        return ""
    
    #start with the first string in the array as the initial prefix to compare to the subsequent strings in the list 
    prefix = strs[0] #set variable "prefix" as the first string in the list of strings with "strs[0]" - that uses the zero index, or first item, of the list. So, in our sample strs, the first string would be "flower". Len of "flower" is 5, b/c 6 items in the list, index starts at 0 (so: 0, 1, 2, 3, 4, 5) - we use this logic below around line 23. 
    #second loop: "flowe"
    #third loop: "flow"
    #"flo"
    #"fl"

    #iterate over the rest of the strings 
    for string in strs[1:]: #for loop, start at the second item with strs[1:] ([start:stop:step]). Second item at index 1 is the string "flow"
        while string[:len(prefix)] != prefix: #while loop, checking the length of the second item in the list doesn't equal the first item in the list ("flower" doesn't equal "flow") then: (next line)
            #second loop = string[:len(prefix)] is flow[:4] ("flowe").
            #third loop, does equal "flow", break out of while loop, and enter for loop to go to next word
            #does the whole string of "flight" match that of prefix, which is now "flow", and it doesn't 
            #"fli" (of "flight"/string) doesn't equal "flo"
            #"fl" (of "flight"/string) matches the prefix, which is now "fl", break out of the while loop, and return prefix 

            prefix = prefix[:-1] #then we remove the last char from the prefix string from the end/back of the string, and stay in the while loop to continue comparing, repeat
            #"flower" -> "flowe"
            #second loop: "flow"
            #third loop: "flo"
            #then remove "o"

            if not prefix: #so if we've removed all the letters from the first str back to front and found zero matches with the second word and then the others, then: 
                return ""
    
    return prefix #we return if there is something, otherwise we'd have already returned an empty string 



#Given an integer x, return true if x is a palindrom, and false otherwise. 

# example: input: x = 121, output: true

def isPalindrome(x): 
    """x is an int, and the outcome is a boolean. a palindrome is the same left to right, as right to left."""

    #x = 121
    #x is a aplindrome, bc it reads the same right to left, as left to right. 
    
    #change int to str as an iterable 
    #go backwards on the iterable and see if it is equivalent to the string of x

    str_x = str(x) #change data type of x from integer (int) to string (str)

    return str_x == str_x[::-1] #we can go directly to the return, because if we set it up this way to check equivalency, it'll return a boolean value, which is our target for the outcome. in this return statement, we are checking the string data type of x to the string data type of x backward to see if they are the same, since that's the definition of a palindrome. [::-1] is no start or stop identified, but then the step is by 1 and going from the last item of the data type that's iterable to the front -- so if we have 121 as the int, it's "121" as a string, and we check the value at index 2, then the value at index 1, then the value at index 0 as the value checked by equivalency on the right side of the equation in the return statement.  


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

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