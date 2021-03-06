#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given an array and a value, remove all instances of that value in-place and return the new length.

	Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

	The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
	Given nums = [3,2,2,3], val = 3,

	Your function should return length = 2, with the first two elements of nums being 2.

'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, total = 0, len(nums)
        while i < total:
            if nums[i] == val:
                nums.pop(i)
                total -= 1
            else:
                i += 1
        return len(nums)
    