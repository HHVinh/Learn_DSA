# 2. Add Two Numbers
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Node giả để giữ cái đầu của danh sách kết quả
        cur = dummy         # Con trỏ chạy để nối các node
        carry = 0           # Biến nhớ (số dư)
        
        # Lặp chừng nào l1 còn, l2 còn, HOẶC carry vẫn còn (VD: 5 + 5 = 10, dư 1)
        while l1 or l2 or carry:
            # Lấy giá trị, nếu node đã là None (hết mảng) thì lấy số 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Tính tổng và số dư
            total = val1 + val2 + carry
            carry = total // 10    # Chia lấy nguyên để ra số nhớ (VD: 15 // 10 = 1)
            digit = total % 10     # Chia lấy dư để ra hàng đơn vị (VD: 15 % 10 = 5)

            # 2 dòng trên có thể viết gọn lại thành 1 dòng để trả về luôn cả phần nguyên và phần dư
            # => carry, digit = divmod(total, 10)
            
            # Tạo node mới và nối vào kết quả
            cur.next = ListNode(digit)
            cur = cur.next
            
            # Di chuyển l1 và l2 tới node tiếp theo nếu còn
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

if __name__ == "__main__":
    # Tạo danh sách liên kết cho l1: 2 -> 4 -> 3
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    
    # Tạo danh sách liên kết cho l2: 5 -> 6 -> 4
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    # In kết quả: 7 -> 0 -> 8
    while result:
        print(result.val, end=" ")
        result = result.next