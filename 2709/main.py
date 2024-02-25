"""
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can
traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest
common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of
traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.
"""

from icecream import ic
from math import gcd
from collections import defaultdict


class Graph:
  def __init__(self, nodes: list | set):
    self.nodes = set(nodes)
    self.edges: dict[int, set] = defaultdict(set)  # list of edges not useful for dfs

  def add_node(self, node):
    self.nodes.add(node)

  def add_edge(self, node1, node2):
    # if node1 not in self.nodes or node2 not in self.nodes:
    #   raise ValueError("Both nodes must be in the graph")
    self.edges[node1].add(node2)
    self.edges[node2].add(node1)

  def has_node(self, node):
    return node in self.nodes

  def has_edge(self, node1, node2):
    return node1 in self.edges and node2 in self.edges[node1]

  def get_edges(self):
    return [(node, edge) for node, edges in self.edges.items() for edge in edges]

  def depth_first_transverse(self):
    visited = set()

    def traverse(n):
      if n in visited:
        return
      visited.add(n)
      for edge in self.edges[n]:
        traverse(edge)

    traverse(self.nodes.copy().pop())
    return visited

  def is_complete(self):
    return len(self.depth_first_transverse()) == len(self.nodes)

  def __str__(self):
    # edge list like
    # 1 2 3 4
    # | | | |
    # 4 2 1 3
    # to represent (1, 4), (2, 2), (3, 1), (4, 3)
    above_line = ""
    middle_line = ""
    below_line = ""
    for edge in self.get_edges():
      above_line += f"{edge[0]} "
      middle_line += "| "
      below_line += f"{edge[1]} "
    return f"{above_line}\n{middle_line}\n{below_line}"


class Solution:
  def canTraverseAllPairs(self, nums: list[int]) -> bool:
    if len(nums) == 1:  # nowhere to transverse
      return True
    ret = Graph(nodes=nums)
    if 1 in ret.nodes:  # gcd(1, n) = 1, testing on ret.nodes because it's a set
      return False
    # build edges
    for a in ret.nodes:
      for b in ret.nodes:
        if a != b and gcd(a, b) > 1:
          ret.add_edge(a, b)
    return ret.is_complete()

  def test(self):
    assert ic(self.canTraverseAllPairs(ic([2, 3, 6]))) is True
    assert ic(self.canTraverseAllPairs(ic([3, 9, 5]))) is False
    assert ic(self.canTraverseAllPairs(ic([4, 3, 12, 8]))) is True
    assert ic(self.canTraverseAllPairs(ic([3, 25]))) is False
    assert ic(self.canTraverseAllPairs(ic([30, 25]))) is True
    assert ic(self.canTraverseAllPairs(ic([1, 1]))) is False


if __name__ == "__main__":
  sol = Solution()
  sol.test()
  print("All tests passed!")
