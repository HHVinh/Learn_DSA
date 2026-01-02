from typing import List   # import để dùng List cho VS Code

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[List[int]]) -> List[List[int]]:
        n = len(intervals)          # Số lượng interval
        i = 0                       # Con trỏ duyệt intervals
        res = []                    # Danh sách kết quả

        # ===== PHẦN 1: interval nằm hoàn toàn bên trái =====
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])    # Thêm interval không chồng
            i += 1

        # ===== PHẦN 2: interval bị chồng với newInterval =====
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])  # Gộp đầu trái
            newInterval[1] = max(newInterval[1], intervals[i][1])  # Gộp đầu phải
            i += 1

        res.append(newInterval)     # Thêm interval đã gộp

        # ===== PHẦN 3: interval nằm bên phải =====
        while i < n:
            res.append(intervals[i])    # Thêm các interval còn lại
            i += 1

        return res


# ====== TEST CHẠY VS CODE ======
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(sol.insert(intervals, newInterval))
