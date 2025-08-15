from typing import List
class Solution:
    # Tìm ra đúng k phần tử xuất hiện nhiều nhất trong mảng
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary lưu số lần xuất hiện của mỗi phần tử
        count = {}
        
        # Tạo một danh sách 2 chiều (bucket) để nhóm các số theo số lần xuất hiện
        # Kích thước: len(nums) + 1 vì 1 phần tử có thể xuất hiện tối đa len(nums) lần
        freq = [[] for i in range(len(nums) + 1)]

        # Bước 1: Đếm số lần xuất hiện của từng phần tử
        # count.get(num, 0): Lấy giá trị hiện tại của num nếu tồn tại, nếu không trả về 0
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Bước 2: Đưa mỗi số vào bucket tương ứng với số lần xuất hiện của nó
        # count.items() trả về các cặp (phần tử, số lần xuất hiện)
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Bước 3: Duyệt từ bucket có số lần xuất hiện cao nhất xuống thấp nhất
        # Lấy các phần tử cho đến khi đủ k phần tử thì dừng
        res = []
        for i in range(len(freq) - 1, 0, -1):  # duyệt từ tần suất cao nhất về thấp
            for num in freq[i]:               # lấy từng số trong bucket
                res.append(num)               # thêm vào kết quả
                if len(res) == k:              # nếu đủ k phần tử thì trả về luôn
                    return res

nums = list(map(int, input("Nhập các số nguyên cách nhau khoảng trắng: ").split()))
k = int(input("Nhập số nguyên k: "))

s = Solution()

print(s.topKFrequent(nums, k))

