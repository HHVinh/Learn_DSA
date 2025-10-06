from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # rez: danh sách kết quả các số bị thiếu
        rez = []

        # n: độ dài mảng (cũng là số lớn nhất có thể xuất hiện)
        n = len(nums)

        # chuyển mảng nums thành set để loại bỏ trùng lặp
        # và giúp kiểm tra tồn tại nhanh hơn (O(1))
        nums_set = set(nums)

        # duyệt qua tất cả các số từ 1 -> n
        for i in range(1, n + 1):
            # nếu số i không có trong nums_set thì thêm vào kết quả
            if i not in nums_set:
                rez.append(i)

        # trả về danh sách kết quả
        return rez


# ------------------ Ví dụ chạy thử ------------------
if __name__ == "__main__":
    sol = Solution()

    # Ví dụ 1
    nums1 = [4,3,2,7,8,2,3,1]
    print("Mảng:", nums1)
    print("Các số bị thiếu:", sol.findDisappearedNumbers(nums1))
    # Kết quả mong đợi: [5,6]

    # Ví dụ 2
    nums2 = [1,1]
    print("\nMảng:", nums2)
    print("Các số bị thiếu:", sol.findDisappearedNumbers(nums2))
    # Kết quả mong đợi: [2]

    # Ví dụ 3
    nums3 = [2,2,2,2]
    print("\nMảng:", nums3)
    print("Các số bị thiếu:", sol.findDisappearedNumbers(nums3))
    # Kết quả mong đợi: [1,3,4]
