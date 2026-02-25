from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums) # Tạo mảng tạm một lần duy nhất để tiết kiệm chi phí khởi tạo liên tục
        
        def merge(left: int, mid: int, right: int):
            # i: con trỏ cho phần bên trái, j: con trỏ cho phần bên phải, k: con trỏ cho mảng temp
            i, j, k = left, mid + 1, left
            
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            
            while i <= mid: # Sao chép phần còn lại của bên trái (nếu có)
                temp[k] = nums[i]
                i += 1
                k += 1
            
            while j <= right: # Sao chép phần còn lại của bên phải (nếu có)
                temp[k] = nums[j]
                j += 1
                k += 1
                
            # Copy từ temp ngược lại vào nums gốc dùng slicing assignment [:] nhanh hơn vòng lặp for trong Python
            nums[left:right+1] = temp[left:right+1]

        def merge_sort(left: int, right: int):
            if left >= right:
                return
            
            mid = (left + right) // 2
            
            merge_sort(left, mid) # Đệ quy sắp xếp nửa trái
            merge_sort(mid + 1, right) # Đệ quy sắp xếp nửa phải
            merge(left, mid, right) # Trộn 2 phần lại

        merge_sort(0, len(nums) - 1) # Gọi hàm sort bắt đầu từ đầu đến cuối mảng
        return nums


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
