class MyHashSet:

    def __init__(self):
        self.table = [[] for i in range(100)]  
        # Tạo 100 bucket (ngăn)
        # Mỗi bucket là một list để chứa các key bị trùng hash (collision)

    def add(self, key: int) -> None:
        lst = self.table[key % 100]  
        # key % 100: xác định bucket mà key sẽ rơi vào

        if key not in lst:  
            # Kiểm tra key đã tồn tại trong bucket chưa
            lst.append(key)  
            # Nếu chưa tồn tại thì thêm key vào bucket

    def remove(self, key: int) -> None:
        lst = self.table[key % 100]  
        # Xác định bucket chứa key cần xóa

        if key in lst:  
            # Nếu key tồn tại trong bucket
            lst.remove(key)  
            # Xóa key khỏi bucket

    def contains(self, key: int) -> bool:
        lst = self.table[key % 100]  
        # Xác định bucket cần kiểm tra

        return key in lst  
        # Trả về True nếu key tồn tại, False nếu không


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
