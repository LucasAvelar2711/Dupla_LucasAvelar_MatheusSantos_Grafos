from collections import defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        parents = defaultdict(set)
        layer = {beginWord}
        found = False

        while layer and not found:
            next_layer = defaultdict(set)
            for w in layer:
                word_set.discard(w)
            for w in layer:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nw = w[:i] + c + w[i+1:]
                        if nw in word_set:
                            next_layer[nw].add(w)
                            if nw == endWord:
                                found = True
            layer = set(next_layer.keys())
            for k, v in next_layer.items():
                parents[k].update(v)

        if not found:
            return []

        res = []
        def backtrack(w, path):
            if w == beginWord:
                res.append(path[::-1])
                return
            for p in parents[w]:
                backtrack(p, path + [p])

        backtrack(endWord, [endWord])
        return res
