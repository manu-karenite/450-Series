# https://leetcode.com/problems/design-underground-system/
class UndergroundSystem:
    def __init__(self):
        self.times = defaultdict(lambda: defaultdict(lambda: [0, 0]))
        self.transit = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.transit[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        srcName, srcTime = self.transit[id]
        count, totalTime = self.times[srcName][stationName]
        self.times[srcName][stationName] = [count+1, totalTime + t - srcTime]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, totalTime = self.times[startStation][endStation]
        return totalTime / count
