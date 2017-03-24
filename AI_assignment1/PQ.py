"""
	AI Assignment 1
	Author: Ben Russell
	Date:1/14/2017
"""
"""
	Priority Queue
"""


import heapq

class PQ(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
