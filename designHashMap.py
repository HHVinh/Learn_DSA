class MyHashMap:

    def __init__(self):
        # Tạo mảng có 1_000_001 phần tử
        # Mỗi vị trí đại diện cho 1 key
        # Giá trị mặc định là -1 (coi như key chưa tồn tại)
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # Gán trực tiếp value vào vị trí key
        # Thao tác O(1)
        self.map[key] = value

    def get(self, key: int) -> int:
        # Trả về giá trị tại vị trí key
        # Nếu chưa từng put thì sẽ là -1
        return self.map[key]

    def remove(self, key: int) -> None:
        # Đặt lại giá trị về -1
        # Tương đương với việc xóa key
        self.map[key] = -1


# =========================
# Code chạy thử trong VS Code
# =========================
if __name__ == "__main__":
    hashMap = MyHashMap()

    hashMap.put(1, 10)
    hashMap.put(2, 20)

    print(hashMap.get(1))   # 10
    print(hashMap.get(3))   # -1 (chưa tồn tại)

    hashMap.put(2, 30)
    print(hashMap.get(2))   # 30

    hashMap.remove(2)
    print(hashMap.get(2))   # -1
