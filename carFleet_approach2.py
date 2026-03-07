# 853. Car Fleet
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # 1. Ghép cặp (vị trí, tốc độ) cho từng xe để dữ liệu đồng bộ
        cars = list(zip(position, speed))
        
        # 2. Sắp xếp các xe theo vị trí giảm dần (từ gần đích nhất đến xa đích nhất)
        # Chiếc xe gần đích nhất sẽ đi trước và đóng vai trò "người dẫn đầu" thiết lập tốc độ cho đoàn
        cars.sort(reverse=True)  

        fleets = 0      # Biến đếm tổng số lượng đoàn xe
        max_time = 0    # Lưu thời gian về đích của đoàn xe chạy chậm nhất phía trước (nút thắt)

        # 3. Duyệt từng xe từ gần đích lùi dần về điểm xuất phát
        for pos, spd in cars:
            # Tính thời gian thực tế để chiếc xe này tự chạy về đích (nếu đường trống)
            time = (target - pos) / spd

            # 4. Quyết định xem xe này có nhập đoàn hay tạo đoàn mới
            if time > max_time:
                # Nếu thời gian xe này > thời gian của đoàn phía trước:
                # Tức là nó chạy quá chậm, vĩnh viễn không thể đuổi kịp đoàn trước.
                # Do đó, nó bị rớt lại và tự trở thành "người dẫn đầu" của một đoàn xe mới.
                fleets += 1       # Ghi nhận thêm 1 đoàn xe
                max_time = time   # Cập nhật "nút thắt" thời gian mới cho các xe chạy sau nó

            # NGƯỢC LẠI (time <= max_time):
            # Xe này chạy nhanh hơn hoặc bằng đoàn phía trước. 
            # Dù sớm hay muộn nó cũng sẽ đâm vào đuôi đoàn trước và buộc phải đi chậm lại theo đoàn.
            # Vì nó nhập chung vào đoàn cũ, ta không tăng fleets và cũng không thay đổi max_time.

        return fleets
    
if __name__ == "__main__":
    solution = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(solution.carFleet(target, position, speed))  # Output: 3