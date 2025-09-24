from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Tạo dictionary để lưu vị trí (index) của các phần tử trong nums1
        # Ví dụ: nums1 = [4,1,2] => nums1Idx = {4:0, 1:1, 2:2}
        nums1Idx = {num: i for i, num in enumerate(nums1)}

        # Kết quả mặc định là -1 (nếu không tìm thấy phần tử lớn hơn)
        res = [-1] * len(nums1)

        # Stack dùng để lưu các phần tử trong nums2 đang chờ tìm "next greater"
        stack = []

        # Duyệt qua từng phần tử trong nums2
        for i in range(len(nums2)):
            cur = nums2[i]

            # Nếu cur lớn hơn phần tử ở cuối stack => tìm được "next greater"
            while stack and cur > stack[-1]:
                val = stack.pop()  # Lấy phần tử nhỏ hơn ra
                idx = nums1Idx[val]  # Tìm vị trí của val trong nums1
                res[idx] = cur  # Gán giá trị lớn hơn tiếp theo cho vị trí tương ứng

            # Nếu cur có trong nums1 thì đưa vào stack để chờ tìm "next greater"
            if cur in nums1Idx:
                stack.append(cur)

        # Trả về kết quả
        return res


# --- Test thử ---
if __name__ == "__main__":
    s = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(s.nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(s.nextGreaterElement(nums1, nums2))  # Output: [3, -1]
