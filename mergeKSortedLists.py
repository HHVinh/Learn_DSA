from typing import Optional
# Định nghĩa node trong danh sách liên kết
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Hàm gộp 2 danh sách liên kết đã sắp xếp
def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()  # node giả để giữ gốc (không chứa giá trị thực sự)
    tail = dummy        # con trỏ chạy, dùng để nối các node mới vào
    
    # So sánh từng phần tử ở l1 và l2 rồi nối vào tail
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1   # nối node nhỏ hơn vào danh sách kết quả
            l1 = l1.next     # tiến con trỏ l1 lên
        else:
            tail.next = l2   # nối node nhỏ hơn vào danh sách kết quả
            l2 = l2.next     # tiến con trỏ l2 lên
        tail = tail.next     # tail luôn trỏ về node cuối cùng

    # Nếu một trong hai list còn node dư thì nối thẳng vào
    tail.next = l1 if l1 else l2

    return dummy.next   # bỏ node giả đi, trả về list kết quả

# Hàm gộp K danh sách
def mergeKLists(lists):
    if not lists:         # nếu mảng rỗng thì trả về None
        return None
    while len(lists) > 1:  # khi còn nhiều hơn 1 list thì tiếp tục gộp
        mergedLists = []
        # Ghép các list theo cặp: (0,1), (2,3), ...
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None  # nếu lẻ thì l2=None
            mergedLists.append(mergeTwoLists(l1, l2))      # gộp 2 list lại
        lists = mergedLists  # cập nhật danh sách sau khi gộp
    return lists[0]          # chỉ còn 1 list duy nhất là kết quả

# Hàm tiện ích: chuyển list Python thành linked list
def buildLinkedList(nums):
    dummy = ListNode()
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

# Hàm tiện ích: in linked list ra màn hình
def printLinkedList(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) if vals else "Empty List")

# --- Chạy chương trình ---
if __name__ == "__main__":
    k = int(input("Nhập số lượng danh sách liên kết: "))
    lists = []
    for i in range(k):
        arr = input(f"Nhập các số cho list {i+1} (cách nhau bởi dấu cách): ").split()
        nums = list(map(int, arr)) if arr else []
        lists.append(buildLinkedList(nums))
    
    result = mergeKLists(lists)
    print("Danh sách sau khi gộp:")
    printLinkedList(result)
