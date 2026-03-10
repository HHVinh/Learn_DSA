# 2. Add Two Numbers
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0) # Tạo một "Nút giả" (Dummy Node) để làm điểm tựa giữ lại cái đầu của danh sách kết quả.
        
        current = head # current là "Con trỏ chạy". Nó sẽ di chuyển liên tục để nối các nút mới vào đuôi danh sách.
        
        carry = 0 # carry là "Biến nhớ". Dùng để lưu phần chục khi tổng của 2 chữ số >= 10.
        
        # Vòng lặp gộp thần thánh: Tiếp tục chạy nếu l1 CÒN, l2 CÒN, HOẶC vẫn CÒN số nhớ (carry).
        while l1 or l2 or carry:
            s = carry # Khởi tạo tổng của cột hiện tại (bắt đầu bằng số nhớ của phép cộng cột trước truyền sang)
            
            if l1: # Nếu danh sách l1 chưa cạn kiệt
                s += l1.val    # Cộng giá trị của nút l1 vào tổng 's'
                l1 = l1.next   # Nhích l1 bước sang nút tiếp theo
                
            if l2: # Tương tự, nếu danh sách l2 chưa cạn kiệt
                s += l2.val    # Cộng giá trị của nút l2 vào tổng 's'
                l2 = l2.next   # Nhích l2 bước sang nút tiếp theo
                
            # Tính toán cho vòng lặp tiếp theo và tạo nút kết quả:
            carry = s // 10    # Chia lấy nguyên để tìm số nhớ. VD: s = 15 -> carry = 1
            
            # Chia lấy dư (s % 10) để lấy chữ số hàng đơn vị. VD: 15 % 10 = 5.
            # Tạo nút mới chứa số 5 này, rồi cho current.next trỏ tới nó để nối vào danh sách.
            current.next = ListNode(s % 10)
            
            # Nhích con trỏ current tiến lên 1 bước, đứng tại nút vừa tạo để chuẩn bị nối tiếp cho vòng sau.
            current = current.next
            
        return head.next # Trả về kết quả thực sự, bỏ qua cái Nút giả (head) ban đầu.

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