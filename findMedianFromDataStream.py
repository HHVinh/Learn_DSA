import heapq  # thư viện hỗ trợ min heap trong Python

class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []  # small = max heap giả (dùng số âm), large = min heap thật

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:  # nếu num lớn hơn min của large
            heapq.heappush(self.large, num)  # đẩy vào large (min heap)
        else:
            heapq.heappush(self.small, -1 * num)  # đẩy vào small (max heap giả → lưu âm)

        if len(self.small) > len(self.large) + 1:  # nếu small nhiều hơn large > 1
            val = -1 * heapq.heappop(self.small)  # lấy max từ small (đổi lại dấu dương)
            heapq.heappush(self.large, val)  # đẩy sang large
        if len(self.large) > len(self.small) + 1:  # nếu large nhiều hơn small > 1
            val = heapq.heappop(self.large)  # lấy min từ large
            heapq.heappush(self.small, -1 * val)  # đẩy sang small (đổi sang âm)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):  # nếu small nhiều hơn
            return -1 * self.small[0]  # trung vị = max của small
        elif len(self.large) > len(self.small):  # nếu large nhiều hơn
            return self.large[0]  # trung vị = min của large
        return (-1 * self.small[0] + self.large[0]) / 2.0  # nếu bằng nhau, lấy trung bình 2 giá trị

# ---- Test chương trình ----
if __name__ == "__main__":
    mf = MedianFinder()
    nums = [5, 2, 8, 10]
    for n in nums:
        mf.addNum(n)
        print(f"Thêm {n}, median = {mf.findMedian()}")
