from typing import Optional

# Định nghĩa node trong linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  # fast đi 2 bước
            if fast == slow:
                return True
        return False

# --- Chạy chương trình ---
if __name__ == "__main__":
    n = int(input("Nhập số node: "))  # số lượng node
    values = list(map(int, input("Nhập các giá trị node, cách nhau bởi khoảng trắng: ").split()))

    # Tạo linked list
    head = ListNode(values[0])
    temp = head
    nodes = [head]  # lưu lại các node để tạo vòng nếu cần
    for v in values[1:]:
        temp.next = ListNode(v)
        temp = temp.next
        nodes.append(temp)

    # Hỏi người dùng có tạo vòng lặp không
    cycle_pos = int(input("Nhập vị trí để tạo vòng lặp (-1 nếu không tạo): "))
    if cycle_pos != -1 and 0 <= cycle_pos < n:
        temp.next = nodes[cycle_pos]  # tạo vòng lặp

    # Gọi hàm kiểm tra
    sol = Solution()
    result = sol.hasCycle(head)
    print("Danh sách có vòng lặp:", result)
