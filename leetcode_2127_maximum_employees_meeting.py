from collections import deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        for v in favorite:
            indegree[v] += 1

        dist = [1] * n
        queue = deque([i for i in range(n) if indegree[i] == 0])

        while queue:
            u = queue.popleft()
            v = favorite[u]
            dist[v] = max(dist[v], dist[u] + 1)
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

        max_cycle = 0
        seen = [False] * n

        for i in range(n):
            if indegree[i] > 0 and not seen[i]:
                cur = i
                size = 0
                while not seen[cur]:
                    seen[cur] = True
                    cur = favorite[cur]
                    size += 1
                max_cycle = max(max_cycle, size)

        pair_sum = 0
        for i in range(n):
            j = favorite[i]
            if favorite[j] == i and i < j:
                pair_sum += dist[i] + dist[j]

        return max(max_cycle, pair_sum)
