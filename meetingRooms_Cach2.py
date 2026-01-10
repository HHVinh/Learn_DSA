from typing import List

# Định nghĩa class Interval giống đề bài
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)

        # Nếu có 0 hoặc 1 cuộc họp → luôn tham gia được
        if n < 2:
            return True

        # Sắp xếp các cuộc họp theo thời điểm kết thúc (end)
        intervals.sort(key=lambda x: x.end)

        # prev lưu thời điểm kết thúc của cuộc họp trước đó
        prev = intervals[0].end

        # Duyệt các cuộc họp còn lại
        for i in range(1, n):
            # Nếu cuộc họp hiện tại bắt đầu trước khi cuộc trước kết thúc
            if prev > intervals[i].start:
                return False  # bị chồng chéo
            else:
                # Không chồng → cập nhật mốc kết thúc
                prev = intervals[i].end

        return True


# ================== TEST VS CODE ==================
if __name__ == "__main__":
    sol = Solution()

    meetings = [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20)
    ]

    print("Cách 1 - Sort theo end:")
    print(sol.canAttendMeetings(meetings))
