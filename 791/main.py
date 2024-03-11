from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = defaultdict(lambda: 27)
        for i in range(len(order)):
            d[order[i]] = i
        return "".join(sorted(s, key=lambda x: d[x]))