from typing import Optional

# Định nghĩa node trong linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Tìm middle bằng slow & fast pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Đảo ngược nửa sau
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # 3. Trộn xen kẽ 2 nửa
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

# Hàm tiện ích để in linked list
def printList(head: Optional[ListNode]):
    nodes = []
    while head:
        nodes.append(str(head.val))
        head = head.next
    print(" → ".join(nodes))

# --- Chương trình chính ---
if __name__ == "__main__":
    n = int(input("Nhập số node: "))
    values = list(map(int, input("Nhập các giá trị node (cách nhau bởi khoảng trắng): ").split()))

    # Tạo linked list
    head = ListNode(values[0])
    temp = head
    for v in values[1:]:
        temp.next = ListNode(v)
        temp = temp.next

    print("Danh sách ban đầu:")
    printList(head)

    # Gọi hàm reorderList
    sol = Solution()
    sol.reorderList(head)

    print("Danh sách sau khi reorder:")
    printList(head)
