"""
	AI Assignment 1
	Author: Ben Russell
	Date:1/14/2017
"""
"""
	Class that represents a node.
	The node will be used by various search algorithms
	to find the best path to a success state for the problem
"""


class Node(object):
    def __init__(self, state, depth):
        self.state = state
        self.depth = depth
    def get_depth(self):
        return self.depth