class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Số kết quả

        # i chạy từ 0 đến 31
        for i in range(32):

            # 1️⃣ Lấy bit thứ i của n
            # n >> i: đưa bit i về cuối
            # & 1: lấy bit cuối
            bit = (n >> i) & 1

            # 2️⃣ Đưa bit đó sang vị trí đối diện
            # bit << (31 - i): đặt bit vào đúng chỗ
            res = res | (bit << (31 - i))

        return res

def main():
    n = int(input("Nhập số nguyên không âm: "))

    sol1 = Solution()

    print("Cách 2 (đảo vị trí):", sol1.reverseBits(n))


if __name__ == "__main__":
    main()
