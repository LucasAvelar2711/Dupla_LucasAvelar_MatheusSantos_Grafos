from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        full_mask = (1 << n) - 1
        queue = deque()
        visited = [[False] * (1 << n) for _ in range(n)]
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited[i][mask] = True
        while queue:
            node, mask, dist = queue.popleft()
            for neigh in graph[node]:
                new_mask = mask | (1 << neigh)
                if new_mask == full_mask:
                    return dist + 1
                if not visited[neigh][new_mask]:
                    visited[neigh][new_mask] = True
                    queue.append((neigh, new_mask, dist + 1))
        return -1
