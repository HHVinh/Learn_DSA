from typing import List   # import để dùng List cho VS Code

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []                               # Danh sách kết quả

        for s, e in intervals:                # Duyệt từng interval
            # TH1: interval nằm hoàn toàn bên trái newInterval
            if e < newInterval[0]:
                res.append([s, e])             # Giữ nguyên interval

            # TH2: interval nằm hoàn toàn bên phải newInterval
            elif s > newInterval[1]:
                res.append(newInterval)        # Chèn newInterval vào kết quả
                newInterval = [s, e]           # Đổi newInterval thành interval hiện tại

            # TH3: interval bị chồng với newInterval
            else:
                newInterval[0] = min(newInterval[0], s)  # Mở rộng đầu trái
                newInterval[1] = max(newInterval[1], e)  # Mở rộng đầu phải

        res.append(newInterval)                # Thêm interval cuối cùng
        return res


# ====== TEST CHẠY VS CODE ======
if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(sol.insert(intervals, newInterval))
