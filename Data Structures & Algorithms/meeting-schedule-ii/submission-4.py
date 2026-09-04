"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        room=[]
        for meeting in intervals:
            if room and meeting.start>=room[0]:
                heapq.heappop(room)
            
            heapq.heappush(room,meeting.end)
        return len(room)