from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Tạo dummy node đứng trước head để dễ xử lý khi xóa node đầu tiên
        result = ListNode(0, head)
        left = result
        right = head

        # Cho con trỏ nhanh chạy trước n bước
        while n > 0:
            right = right.next
            n -= 1

        # Sau đó cho cả 2 con trỏ chạy song song đến cuối
        while right:
            left = left.next
            right = right.next

        # Lúc này left.next chính là node cần xóa → bỏ qua nó
        left.next = left.next.next

        # Trả về danh sách mới (bỏ qua dummy node)
        return result.next

# ---------------- PHẦN MAIN ĐỂ NHẬP VÀ CHẠY ----------------
def build_linked_list(values):
    """Hàm tạo danh sách liên kết từ list giá trị"""
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    """Hàm in danh sách liên kết"""
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

if __name__ == "__main__":
    # Nhập danh sách các số, ví dụ: 1 2 3 4 5
    arr = list(map(int, input("Nhập các phần tử danh sách liên kết (cách nhau bằng khoảng trắng): ").split()))
    n = int(input("Nhập n (node thứ n từ cuối cần xóa): "))

    head = build_linked_list(arr)
    print("Danh sách ban đầu:")
    print_linked_list(head)

    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)

    print("Danh sách sau khi xóa:")
    print_linked_list(new_head)
