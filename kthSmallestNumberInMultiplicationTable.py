class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if k > n * m:
            return -1

        def check(mid) -> bool:
            count = 0
            # Duyệt qua từng hàng i trong bảng (1 đến m)
            for i in range(1, m + 1):
                # Trong hàng i có các số: i*1, i*2, ..., i*n
                # Ta cần đếm số lượng phần tử <= mid
                # Điều kiện: i * j <= mid  =>  j <= mid // i
                # Nhưng j không thể vượt quá n (số cột)
                # Vì vậy, số lượng phần tử thỏa mãn ở hàng i là:
                count += min(mid // i, n)
            # Nếu tổng số phần tử <= mid trong toàn bảng >= k
            # thì mid đủ lớn (hoặc thừa), trả về True
            return count >= k
        
        l, r = 1, m * n
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == "__main__":
    m = int(input("Nhập m (số hàng): "))
    n = int(input("Nhập n (số cột): "))
    k = int(input("Nhập k (thứ tự cần tìm): "))

    sol = Solution()
    result = sol.findKthNumber(m, n, k)
    print(f"Số nhỏ thứ {k} trong bảng {m}x{n} là: {result}")
