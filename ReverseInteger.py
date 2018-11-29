# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:19:28 2018

Challenge Problem from LeetCode: Reverse Integer
    
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
of this problem, assume that your function returns 0 when the reversed 
integer overflows.

@author: Felix A
"""

"""
A few Important things that allowed me to code this:
    - reverse slicing:
        [ <first element to include> : <first element to exclude> : <step> ]
    - It was easier to change the integer into a string so we can capture 
      the negative value (if there was one)
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        x =str(x) # change integer to a string in order to enumerate.
        
        # 1st case: if the string starts with '-'
        if x[0] == '-': 
            y= [x[0], x[:0:-1]] # separate the '-' and reverse the integers
            y = int(''.join(a for a in y)) #stick them all together
            # this last value of why should give us a negative value with the
            # reversed integers.
        
        # 2nd Case: if the string doesnt start with '-', all we do is
        # reverse slicing.
        else:
            y = int(x[::-1])
           
        
        # Now, this is to check if our integer is in the 32-bit range.
        # if inside, we should obtain the reverse number, otherwise our
        # answer is zero.
        if y >2**31 -1 or y<-2**31:
            return 0
        else:
            return y

""" UNCOMMENT THIS  IF YOU WISH TO TEST        
test = Solution()
x = -123
print(test.reverse(x))
"""