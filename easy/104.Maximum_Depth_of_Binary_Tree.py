#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given a binary tree, find its maximum depth.

	The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example:
	Given binary tree [3,9,20,null,null,15,7],

	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its depth = 3.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1 if root else 0       #递归求解即可