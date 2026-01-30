from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left: List[int], right: List[int]) -> List[int]: # Hàm trộn 2 mảng đã được sắp xếp
            result = []                 # Mảng kết quả
            i, j = 0, 0                       # Con trỏ mảng left và right

            while i < len(left) and j < len(right): # So sánh từng phần tử của 2 mảng
                if left[i] < right[j]: # Nếu phần tử bên trái nhỏ hơn
                    result.append(left[i])
                    i += 1
                else:                  # Ngược lại
                    result.append(right[j])
                    j += 1

            # Thêm các phần tử còn dư (nếu có)
            result.extend(left[i:])    # Phần còn lại của left
            result.extend(right[j:])   # Phần còn lại của right

            return result              # Trả về mảng đã trộn

        def merge_sort(arr: List[int]) -> List[int]: # Hàm Merge Sort (đệ quy)
            if len(arr) <= 1:          # Mảng 0 hoặc 1 phần tử thì đã sorted
                return arr

            mid = len(arr) // 2        # Tìm vị trí chia đôi mảng

            left = merge_sort(arr[:mid])   # Sắp xếp nửa trái
            right = merge_sort(arr[mid:])  # Sắp xếp nửa phải

            return merge(left, right)  # Trộn 2 nửa đã sắp xếp

        return merge_sort(nums)        # Gọi Merge Sort


# =========================
# HÀM MAIN CHẠY VS CODE
# =========================
def main():
    nums = [8, 5, 3, 7, 6, 2]

    print("Mảng ban đầu:")
    print(nums)

    solution = Solution()
    sorted_nums = solution.sortArray(nums)

    print("Mảng sau khi sắp xếp:")
    print(sorted_nums)


# Điểm bắt đầu chương trình
if __name__ == "__main__":
    main()
