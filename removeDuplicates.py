# -*- coding: utf-8 -*-
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # Collect the ones that are non repetitive  
   
    
    # If the len = 0, we just return zero.   
        if len(nums) ==0:
            return 0
     
    # start the iteration:
        i = 1
    # The loop will work as follows:
    
    # steps:
    # we start comparing the first element with the second one (nums[0] with nums[1] respectively) in the list nums. 
    # If these two are not equal, then its not repetitive, so we keep the position, thus nums[0] and nums[1] remain.
    # We repeat the iteration to check if new item repeats with the previous one
    
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i+=1
        return i

"""UNCOMMENT THIS  IF YOU WISH TO TEST        
test = Solution()
x = [1,1,2]
print(test.removeDuplicates(x))
"""