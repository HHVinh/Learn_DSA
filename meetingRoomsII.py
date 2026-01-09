import heapq
from typing import List

# Định nghĩa Interval giống LeetCode
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)

        # Nếu 0 hoặc 1 cuộc họp thì không thể chồng chéo
        if n < 2:
            return n

        # 1️⃣ Sắp xếp các cuộc họp theo thời gian bắt đầu tăng dần
        intervals.sort(key=lambda x: x.start)

        # 2️⃣ Min Heap dùng để lưu thời điểm kết thúc của các phòng
        # heap[0] luôn là phòng rảnh sớm nhất
        minHeap = []

        for interval in intervals:
            # Nếu có phòng và phòng đó rảnh trước hoặc đúng lúc cuộc họp mới bắt đầu
            if minHeap and interval.start >= minHeap[0]:
                # Giải phóng phòng đó (dùng lại)
                heapq.heappop(minHeap)

            # Dù là phòng cũ hay phòng mới
            # ta đều push thời điểm kết thúc mới vào heap
            heapq.heappush(minHeap, interval.end)

        # 4️⃣ Số phần tử trong heap = số phòng cần
        return len(minHeap)


# =========================
# Code test để chạy VS Code
# =========================
if __name__ == "__main__":
    intervals = [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20)
    ]

    sol = Solution()
    result = sol.minMeetingRooms(intervals)

    print("Số phòng họp tối thiểu cần:", result)
