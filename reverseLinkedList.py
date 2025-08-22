from typing import Optional

class ListNode: # Định nghĩa node trong linked list
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:                  # nếu danh sách rỗng thì trả về None
            return None
        prev, curr = None, head       # prev trỏ None, curr bắt đầu từ head
        while curr:                   # duyệt đến khi curr = None
            temp = curr.next          # lưu node kế tiếp
            curr.next = prev          # đảo chiều liên kết
            prev = curr               # dời prev sang curr
            curr = temp               # dời curr sang node tiếp theo
        return prev                   # prev là node đầu mới sau khi đảo ngược

def printList(head: Optional[ListNode]): # Hàm in danh sách liên kết
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

def createLinkedList(arr: list[int]) -> Optional[ListNode]: # Hàm tạo linked list từ list Python
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head
if __name__ == "__main__":
    arr = list(map(int, input("Nhập các số của linked list (cách nhau bởi dấu cách): ").split()))
    head = createLinkedList(arr)
    print("Danh sách gốc:")
    printList(head)
    sol = Solution()
    new_head = sol.reverseList(head)
    print("Danh sách sau khi đảo ngược:")
    printList(new_head)
