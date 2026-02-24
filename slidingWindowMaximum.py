# 239. Sliding Window Maximum
from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # Lưu INDEX của các ứng viên, KHÔNG lưu giá trị
        l, r = 0, 0

        while r < len(nums):
            
            # Trước khi thêm số mới (nums[r]) vào, ta kiểm tra các số ở cuối hàng đợi.
            # Nếu số mới LỚN HƠN số đang ở cuối hàng (nums[q[-1]]), 
            # thì số ở cuối hàng đó trở nên vô dụng (vì nó vừa nhỏ hơn, vừa cũ hơn).
            while q and nums[r] > nums[q[-1]]:
                q.pop() # -> Đuổi nó ra (pop) để nhường chỗ cho kẻ mạnh hơn.
            
            # Sau khi dọn dẹp xong, thêm index của số mới vào cuối hàng.
            # Lúc này, q[0] luôn đảm bảo là index của số LỚN NHẤT trong cửa sổ.
            q.append(r)

            # Kiểm tra xem cái số lớn nhất (đang nằm ở q[0]) có bị trượt ra ngoài cửa sổ hay không.
            # Nếu l > q[0], nghĩa là index q[0] đã nằm bên ngoài vùng [l, r].
            if l > q[0]:
                q.popleft() # Loại bỏ ứng viên "về hưu" khỏi đầu hàng đợi
            
            # Chỉ khi cửa sổ đã mở đủ kích thước k (r + 1 >= k) thì mới bắt đầu tính.
            # Ví dụ k=3, thì khi r chạy đến index 2 (tức là đã duyệt 0,1,2) mới bắt đầu ghi.
            if (r + 1) >= k:
                
                res.append(nums[q[0]]) # nums[q[0]] luôn là max hiện tại
                # Sau khi ghi nhận xong, ta co chân trái (l) lên 1 bước để chuẩn bị cho lần lặp tiếp theo.
                l += 1
            
            r += 1 # Mở rộng chân phải (r) để tiếp tục vòng lặp
            
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
    print(solution.maxSlidingWindow([1], 1))  # Output: [1]
    print(solution.maxSlidingWindow([9,11], 2))  # Output: [11]
    print(solution.maxSlidingWindow([4,-2], 2))  # Output: [4]