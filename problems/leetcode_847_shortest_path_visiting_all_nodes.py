"""
LeetCode 847 - Shortest Path Visiting All Nodes

You have an undirected, connected graph of n nodes labeled from 0 to n - 1. 
You are given an array graph where graph[i] is a list of all the nodes 
connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start 
and stop at any node, you may revisit nodes multiple times, and you may reuse 
edges.

Approach: BFS with Bitmask State
- Use bitmask to track which nodes have been visited
- State = (current_node, visited_mask)
- BFS explores states level by level, guaranteeing shortest path
- Goal: visited_mask has all n bits set (all nodes visited)

Time Complexity: O(2^n * n^2)
Space Complexity: O(2^n * n)
"""

from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        # Handle edge case: single node
        if n == 1:
            return 0
        
        # Target mask: all n nodes visited (all bits set)
        target_mask = (1 << n) - 1
        
        # BFS queue: (node, visited_mask, distance)
        # Start BFS from all nodes simultaneously
        queue = deque()
        visited = set()
        
        for i in range(n):
            initial_mask = 1 << i
            queue.append((i, initial_mask, 0))
            visited.add((i, initial_mask))
        
        while queue:
            node, mask, dist = queue.popleft()
            
            # Explore neighbors
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                
                # Check if we've visited all nodes
                if new_mask == target_mask:
                    return dist + 1
                
                # Add new state if not visited
                state = (neighbor, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, new_mask, dist + 1))
        
        return 0


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: graph = [[1,2,3],[0],[0],[0]]
    # Output: 4 (path: 1->0->2->0->3 or similar)
    graph1 = [[1, 2, 3], [0], [0], [0]]
    print(f"Example 1: {solution.shortestPathLength(graph1)}")
    
    # Example 2: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    # Output: 4
    graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    print(f"Example 2: {solution.shortestPathLength(graph2)}")
    
    # Example 3: Single node
    graph3 = [[]]
    print(f"Example 3: {solution.shortestPathLength(graph3)}")
