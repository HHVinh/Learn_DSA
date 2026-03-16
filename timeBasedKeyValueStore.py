# 981. Time Based Key-Value Store
class TimeMap:
    def __init__(self):
        # Dùng dictionary, mỗi key sẽ map với một list chứa các cặp [value, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Nối vào cuối list. Do đề bài đảm bảo timestamp tăng dần, list này luôn được sort.
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Nếu key không tồn tại, trả về chuỗi rỗng
        if key not in self.store:
            return ""
        
        values = self.store[key]
        res = ""
        
        # Tìm kiếm nhị phân (Binary Search)
        left, right = 0, len(values) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # values[mid][1] chính là timestamp tại vị trí mid
            if values[mid][1] <= timestamp:
                # Nếu timestamp hiện tại hợp lệ (nhỏ hơn hoặc bằng mục tiêu),
                # ghi nhận kết quả và thử tìm ở nửa bên PHẢI xem có cái nào gần mục tiêu hơn không.
                res = values[mid][0] 
                left = mid + 1
            else:
                # Nếu timestamp lớn hơn mục tiêu, buộc phải tìm ở nửa bên TRÁI
                right = mid - 1
                
        return res
    
if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))  # Output: "bar"
    print(timeMap.get("foo", 3))  # Output: "bar"
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))  # Output: "bar2"
    print(timeMap.get("foo", 5))  # Output: "bar2"