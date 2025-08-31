from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Hàm kiểm tra: Với tốc độ ăn k, Koko có thể ăn hết trong <= h giờ không?
        def canEatAll(k: int) -> bool:
            hours = 0
            for bananas in piles:
                # (bananas + k - 1) // k = số giờ cần để ăn hết chồng 'bananas'
                # đây chính là cách làm tròn lên (ceil) khi chia
                hours += (bananas + k - 1) // k  
            return hours <= h  # nếu tổng số giờ <= h thì tốc độ này đủ

        # Tốc độ nhỏ nhất có thể là 1 (ăn 1 quả/giờ)
        # Tốc độ lớn nhất có thể là max(piles) (ăn hết chồng to nhất trong 1 giờ)
        left, right = 1, max(piles)

        # Binary Search để tìm tốc độ nhỏ nhất thỏa mãn
        while left < right:
            mid = left + (right - left) // 2  # tốc độ thử nghiệm
            if canEatAll(mid):
                # Nếu với tốc độ mid mà ăn được trong h giờ,
                # thì thử giảm tốc độ (nhỏ hơn) -> thu hẹp về bên trái
                right = mid
            else:
                # Nếu không đủ giờ -> phải tăng tốc độ -> thu hẹp về bên phải
                left = mid + 1

        # Khi vòng lặp kết thúc, left == right = tốc độ nhỏ nhất thỏa mãn
        return left
    

if __name__ == "__main__":
    piles = [3, 6, 7, 11, 8, 5, 9]  # cho sẵn mảng
    h = int(input("Nhập số giờ h: "))  # yêu cầu nhập h
    sol = Solution()
    result = sol.minEatingSpeed(piles, h)
    print(f"\n👉 Tốc độ ăn nhỏ nhất để Koko ăn hết trong {h} giờ là: {result}")