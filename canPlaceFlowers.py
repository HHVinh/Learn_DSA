from typing import List  # để khai báo kiểu List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros, ans = 1, 0      # zeros = đếm số ô trống liên tiếp (giả sử trước mảng có 1 ô trống)
                               # ans = số hoa có thể trồng được

        for f in flowerbed:    # duyệt từng ô trong flowerbed
            if not f:          # nếu ô hiện tại = 0 (trống)
                zeros += 1     # cộng thêm 1 ô trống
            else:              # nếu ô hiện tại = 1 (có hoa rồi)
                ans += (zeros - 1) // 2  # tính số hoa trồng được ở chuỗi 0 trước đó
                zeros = 0                # reset về 0 vì đã gặp 1
        # kết thúc vòng lặp, xử lý chuỗi 0 cuối mảng
        ans += zeros // 2

        return ans >= n  # kiểm tra có trồng được ít nhất n hoa không


# ====== Chương trình chính để chạy ======
if __name__ == "__main__":
    # nhập flowerbed, ví dụ: 1 0 0 0 1
    flowerbed = list(map(int, input("Nhập flowerbed (0: trống, 1: có hoa), cách nhau bởi khoảng trắng: ").split()))

    # nhập n: số hoa muốn trồng
    n = int(input("Nhập số hoa n muốn trồng: "))

    sol = Solution()
    result = sol.canPlaceFlowers(flowerbed, n)

    # in kết quả
    print(f"Có thể trồng được {n} hoa hay không?", result)


"""
================= GIẢI THÍCH CHI TIẾT =================

Ý tưởng: Ta muốn kiểm tra có thể trồng thêm n bông hoa mà không vi phạm quy tắc 
(hoa không được trồng cạnh nhau).

Biến:
- zeros: đếm số ô trống liên tiếp. Ban đầu = 1, coi như ngoài biên trái có 1 ô trống.
- ans: tổng số hoa có thể trồng được.

Cách tính:
- Khi gặp số 0 → cộng vào zeros.
- Khi gặp số 1 → có hoa, nên chốt chuỗi 0 trước đó:
  + Số hoa trồng được trong chuỗi 0 = (zeros - 1) // 2
  + Reset zeros = 0
- Sau vòng lặp, cộng thêm zeros // 2 (xử lý chuỗi 0 cuối cùng).

Ví dụ: flowerbed = [1,0,0,0,1], n=1

Bước chạy:
- zeros=1, ans=0
- gặp 1 → ans+=(1-1)//2=0, zeros=0
- gặp 0 → zeros=1
- gặp 0 → zeros=2
- gặp 0 → zeros=3
- gặp 1 → ans+=(3-1)//2=1, zeros=0
Kết thúc → ans=1, zeros=0
ans + zeros//2 = 1 → >= n=1 → True
"""
