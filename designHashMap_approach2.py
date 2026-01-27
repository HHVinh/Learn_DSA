class MyHashMap:

    def __init__(self):
        # Sử dụng dict có sẵn của Python
        # Chỉ lưu những key thực sự được dùng
        self.dictionary = {}

    def put(self, key: int, value: int) -> None:
        # Gán value cho key
        # Nếu key đã tồn tại thì cập nhật
        self.dictionary[key] = value

    def get(self, key: int) -> int:
        # Kiểm tra key có tồn tại không
        # Nếu không có thì trả về -1
        if key not in self.dictionary:
            return -1
        else:
            return self.dictionary[key]

    def remove(self, key: int) -> None:
        # Nếu key tồn tại thì xóa
        if key in self.dictionary:
            del self.dictionary[key]


# =========================
# Code chạy thử trong VS Code
# =========================
if __name__ == "__main__":
    hashMap = MyHashMap()

    hashMap.put(1, 10)
    hashMap.put(2, 20)

    print(hashMap.get(1))   # 10
    print(hashMap.get(3))   # -1

    hashMap.put(2, 30)
    print(hashMap.get(2))   # 30

    hashMap.remove(2)
    print(hashMap.get(2))   # -1
