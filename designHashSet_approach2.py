class MyHashSet:

    def __init__(self):
        # key is in the range [1, 1000000]
        # 31251 * 32 = 1000032
        self.set = [0] * 31251  
        # Mỗi phần tử là 1 số nguyên 32 bit
        # Toàn bộ mảng đại diện cho ~1 triệu bit (mỗi key = 1 bit)

    def add(self, key: int) -> None:
        self.set[key // 32] |= self.getMask(key)  
        # key // 32: xác định số nguyên chứa bit của key
        # |= (OR): bật bit lên 1 → đánh dấu key tồn tại

    def remove(self, key: int) -> None:
        if self.contains(key):  
            # Chỉ xóa nếu key đang tồn tại
            self.set[key // 32] ^= self.getMask(key)  
            # ^= (XOR): tắt bit từ 1 về 0

    def contains(self, key: int) -> bool:
        return self.set[key // 32] & self.getMask(key) != 0  
        # &: kiểm tra bit
        # ≠ 0 → bit đang bật → key tồn tại

    def getMask(self, key: int) -> int:
        return 1 << (key % 32)  
        # Tạo mask có đúng 1 bit = 1 tại vị trí (key % 32)

# ======================
# MAIN - chạy trong VS Code
# ======================
def main():
    my_set = MyHashSet()                # Tạo MyHashSet bằng bitset

    my_set.add(5)                       # Thêm 5
    my_set.add(100)                     # Thêm 100
    my_set.add(999999)                  # Thêm 999999

    print(my_set.contains(5))           # True
    print(my_set.contains(100))         # True
    print(my_set.contains(7))           # False

    my_set.remove(100)                  # Xóa 100
    print(my_set.contains(100))         # False


if __name__ == "__main__":
    main()                              # Điểm bắt đầu chương trình
