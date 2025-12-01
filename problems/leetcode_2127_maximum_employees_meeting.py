"""
LeetCode 2127 - Maximum Employees to Be Invited to a Meeting

A company is organizing a meeting and has a list of n employees, numbered from 
0 to n - 1. Each employee has a favorite person and they will attend the meeting 
only if they can sit next to their favorite person at the table. The favorite 
person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite 
person of the ith employee, return the maximum number of employees that can be 
invited to the meeting.

Approach: Graph Theory - Cycle Detection + Chain Extension
- The favorite relationship forms a functional graph (each node has exactly one outgoing edge)
- Two cases to consider:
  1. Large cycles (length > 2): All employees in the cycle can sit together
  2. Mutual pairs (cycles of length 2): Can extend with chains of fans
- Answer is max of: longest single cycle OR sum of all extended mutual pairs

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        
        # Calculate in-degree for each node
        in_degree = [0] * n
        for fav in favorite:
            in_degree[fav] += 1
        
        # Find longest chain leading to each node using topological sort
        # Process nodes not in cycles first
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        # depth[i] = longest chain ending at node i
        depth = [1] * n
        
        while queue:
            node = queue.popleft()
            fav = favorite[node]
            depth[fav] = max(depth[fav], depth[node] + 1)
            in_degree[fav] -= 1
            if in_degree[fav] == 0:
                queue.append(fav)
        
        # Now process cycles (nodes with in_degree > 0)
        longest_cycle = 0
        sum_of_pairs = 0
        
        for i in range(n):
            if in_degree[i] == 0:
                continue
            
            # Found a node in a cycle, traverse it
            cycle_length = 0
            current = i
            
            while in_degree[current] > 0:
                in_degree[current] = 0  # Mark as visited
                cycle_length += 1
                current = favorite[current]
            
            if cycle_length == 2:
                # Mutual pair: can extend with chains
                # Get the two nodes in the pair
                node1 = i
                node2 = favorite[i]
                sum_of_pairs += depth[node1] + depth[node2]
            else:
                # Large cycle: all members can sit together
                longest_cycle = max(longest_cycle, cycle_length)
        
        return max(longest_cycle, sum_of_pairs)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: favorite = [2,2,1,2]
    # Output: 3 (employees 0, 1, 2 can attend)
    favorite1 = [2, 2, 1, 2]
    print(f"Example 1: {solution.maximumInvitations(favorite1)}")
    
    # Example 2: favorite = [1,2,0]
    # Output: 3 (all employees form a cycle and can attend)
    favorite2 = [1, 2, 0]
    print(f"Example 2: {solution.maximumInvitations(favorite2)}")
    
    # Example 3: favorite = [3,0,1,4,1]
    # Output: 4
    favorite3 = [3, 0, 1, 4, 1]
    print(f"Example 3: {solution.maximumInvitations(favorite3)}")
