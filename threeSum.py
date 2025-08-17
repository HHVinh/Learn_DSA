from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # Duyệt từng phần tử enumerat(index, value)
        for i, a in enumerate(nums):
            if a > 0:
                # Vì mảng đã sắp xếp tăng dần, nếu số đầu tiên > 0 thì không thể có tổng = 0 nữa
                break
            if i > 0 and a == nums[i - 1]:
                # Bỏ qua nếu phần tử này trùng với phần tử trước đó
                continue
            # Hai con trỏ: trái (l) và phải (r)
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: # Tổng lớn hơn 0 => cần giảm => dịch con trỏ phải sang trái
                    r -= 1 
                elif threeSum < 0: # Tổng nhỏ hơn 0 => cần tăng => dịch con trỏ trái sang phải
                    l += 1 
                else: # Tìm được bộ ba hợp lệ
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Bỏ qua các số trùng lặp ở con trỏ trái
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

if __name__ == "__main__":
    nums = list(map(int, input("Nhập mảng số nguyên (cách nhau bằng khoảng trắng): ").split()))
    solution = Solution()
    ket_qua = solution.threeSum(nums)
    print("Các bộ ba có tổng bằng 0 là:")
    print(ket_qua)
