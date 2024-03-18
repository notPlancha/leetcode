class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort(key=lambda x: x[0])
    sets = [set(range(point[0], point[1] + 1)) for point in points]
    sets.sort()
    i = 0
    try:
        while True:
            s = sets[i]
            s_next = sets[i + 1]
            joined = s & s_next
            if len(joined) == 0:
                i += 1
            else:
                sets[i] = joined
                del sets[i + 1]
    except IndexError:
        pass
    return len(sets)