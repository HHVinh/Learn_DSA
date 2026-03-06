# 853. Car Fleet
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Bước 1: Ghép cặp vị trí và tốc độ
        # Phải dùng list() bọc ngoài zip để tạo thành một danh sách thực sự, 
        # vì bản thân zip() trong Python chỉ tạo ra một "máy phát" (iterator)
        cars = list(zip(position, speed))
        
        # Bước 2: Sắp xếp danh sách trực tiếp (in-place)
        # Dùng lambda x: x[0] để nói rõ: "Hãy sắp xếp dựa trên phần tử index 0 (vị trí)"
        # reverse=True để xếp từ vị trí gần đích nhất lùi về xa đích nhất
        cars.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        
        # Bước 3: Duyệt qua danh sách đã sắp xếp và xử lý bằng Stack
        for pos, spd in cars:
            # Tính thời gian để xe hiện tại chạm đích
            time_to_target = (target - pos) / spd
            
            # Thêm thời gian này vào stack
            stack.append(time_to_target)
            
            # Nếu có từ 2 xe trở lên trong stack
            # và thời gian xe phía sau (đỉnh stack) <= xe phía trước (kế đỉnh)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Xe phía sau bắt kịp xe trước, gộp vào chung 1 đoàn
                # Loại bỏ thời gian của xe phía sau ra khỏi stack
                stack.pop()
                
        # Số lượng thời gian còn lại trong stack chính là số đoàn xe
        return len(stack)

if __name__ == "__main__":
    solution = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(solution.carFleet(target, position, speed))  # Output: 3