# 81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            
            # TRƯỜNG HỢP 1: Nửa TRÁI đang tăng dần hoàn hảo (từ l đến m)
            # Ví dụ: [3, 4, 5, 6, 1, 2], m đang trỏ vào số 5. Trái (3) < Giữa (5).
            if nums[l] < nums[m]:  
                # Vì nửa trái tăng dần đều, ta kiểm tra xem target có lọt thỏm vào khoảng này không
                # Khoảng này bắt đầu từ nums[l] đến sát nums[m]
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Có lọt vào -> Chắc chắn nằm bên trái, bỏ nửa phải
                else:
                    l = m + 1  # Không lọt vào -> Bắt buộc phải nằm bên phải
                    
            # TRƯỜNG HỢP 2: Nửa PHẢI đang tăng dần hoàn hảo (từ m đến r)
            # Ví dụ: [5, 6, 1, 2, 3, 4], m đang trỏ vào số 1. Trái (5) > Giữa (1).
            elif nums[l] > nums[m]:  
                # Vì nửa phải tăng dần đều, ta kiểm tra xem target có lọt thỏm vào khoảng này không
                # Khoảng này bắt đầu từ sau nums[m] đến nums[r]
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Có lọt vào -> Chắc chắn nằm bên phải, bỏ nửa trái
                else:
                    r = m - 1  # Không lọt vào -> Bắt buộc phải nằm bên trái
                    
            # TRƯỜNG HỢP 3: nums[l] == nums[m] (Không biết nửa nào tăng dần)
            # Xảy ra do mảng có số trùng lặp. Ví dụ: [1, 0, 1, 1, 1] hoặc [1, 1, 1, 0, 1]
            # Vì lúc nãy ta đã check `if nums[m] == target` và nó sai, 
            # nên nums[l] cũng chắc chắn KHÔNG PHẢI target. Ta tự tin loại bỏ l.
            else:
                l += 1
                
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.search([2,5,6,0,0,1,2], 0))  # True
    print(s.search([2,5,6,0,0,1,2], 3))  # False
    print(s.search([1,0,1,1,1], 0))      # True
    print(s.search([1,1,1,0,1], 0))      # True
    print(s.search([1,1,1,1,1], 0))      # False