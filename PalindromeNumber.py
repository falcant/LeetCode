# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:25:06 2018
Challenge Problem from LeetCode: Palindrome Number

Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, 
it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
@author: Felix A
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x =str(x) #first we change out integer to a string.
        # check if the first item on the string is a negative sign
        # OR if the reversed dont look the same, then return False. Otherwise
        # return True.
        if x[0] == '-' or x[::-1]!= x[:]:
            return False
        else:
            return True
        
 #UNCOMMENT THIS  IF YOU WISH TO TEST        
"""
test = Solution()
Three Different cases:
x = -123
y = 101
z = 10021
print(test.isPalindrome(x))
print(test.isPalindrome(y))
print(test.isPalindrome(z))
"""
