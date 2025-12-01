"""
LeetCode 269 - Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order 
of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, 
where the strings in words are sorted lexicographically by the rules of this 
new language.

Return a string of the unique letters in the new alien language sorted in 
lexicographically increasing order by the new language's rules. If there is 
no solution, return "". If there are multiple solutions, return any of them.

Approach: Topological Sort using Kahn's Algorithm (BFS)
- Build a directed graph where an edge from u to v means u comes before v
- Use BFS-based topological sort to find the order
- If cycle is detected (not all nodes processed), return ""

Time Complexity: O(C) where C is total length of all words
Space Complexity: O(1) since at most 26 characters
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Build adjacency list and in-degree count
        adj = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}
        
        # Compare adjacent words to find ordering
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            
            # Check for invalid case: prefix comes after longer word
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            # Find first different character
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break
        
        # BFS Topological Sort (Kahn's Algorithm)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If not all characters processed, there's a cycle
        if len(result) != len(in_degree):
            return ""
        
        return "".join(result)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: words = ["wrt","wrf","er","ett","rftt"]
    # Output: "wertf"
    words1 = ["wrt", "wrf", "er", "ett", "rftt"]
    print(f"Example 1: {solution.alienOrder(words1)}")
    
    # Example 2: words = ["z","x"]
    # Output: "zx"
    words2 = ["z", "x"]
    print(f"Example 2: {solution.alienOrder(words2)}")
    
    # Example 3: words = ["z","x","z"]
    # Output: "" (cycle detected)
    words3 = ["z", "x", "z"]
    print(f"Example 3: {solution.alienOrder(words3)}")
