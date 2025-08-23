# Định nghĩa lớp ListNode (nút trong danh sách liên kết đơn)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # giá trị của node
        self.next = next      # con trỏ tới node tiếp theo


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Tạo node giả để bắt đầu (dummy), node là con trỏ để nối
        dummy = node = ListNode()

        # Lặp khi cả 2 danh sách đều còn phần tử
        while list1 and list2:
            if list1.val < list2.val:    # nếu giá trị list1 nhỏ hơn list2
                node.next = list1        # nối node hiện tại với list1
                list1 = list1.next       # dịch list1 sang phần tử tiếp theo
            else:                        # ngược lại nối list2
                node.next = list2
                list2 = list2.next
            node = node.next             # dịch con trỏ node sang node mới nối

        # Nếu còn phần dư (1 trong 2 danh sách chưa hết) thì nối thẳng vào
        node.next = list1 or list2

        # Kết quả là danh sách bắt đầu từ dummy.next (bỏ qua node giả)
        return dummy.next


# Hàm hỗ trợ: chuyển list Python thành Linked List
def build_linked_list(values):
    dummy = ListNode()   # node giả
    curr = dummy
    for v in values:
        curr.next = ListNode(v)  # tạo node mới cho từng giá trị
        curr = curr.next
    return dummy.next   # trả về node gốc (bỏ node giả)


# Hàm hỗ trợ: in danh sách liên kết ra màn hình
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()


# =========================
# CHẠY THỬ
# =========================

# Nhập 2 danh sách đã sắp xếp
list1_values = list(map(int, input("Nhập list1 (các số cách nhau bởi dấu cách): ").split()))
list2_values = list(map(int, input("Nhập list2 (các số cách nhau bởi dấu cách): ").split()))

# Chuyển list Python sang Linked List
list1 = build_linked_list(list1_values)
list2 = build_linked_list(list2_values)

# Gọi hàm gộp
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# In kết quả
print("Kết quả sau khi gộp:")
print_linked_list(merged_list)
