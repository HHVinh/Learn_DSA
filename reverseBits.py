class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Số kết quả, ban đầu = 0

        for _ in range(32): # Luôn lặp 32 lần vì số là 32-bit

            # 1️⃣ n & 1: Lấy bit cuối của n
            # - Nếu bit cuối là 1 -> kết quả = 1
            # - Nếu bit cuối là 0 -> kết quả = 0
            last_bit = n & 1

            # 2️⃣ res << 1: Dịch res sang trái 1 bit
            # - Nhân res với 2
            # - Tạo 1 chỗ trống bên phải
            res = res << 1

            # 3️⃣ | (OR): Nhét bit vừa lấy vào bên phải của res
            # - 0 | 1 = 1
            # - 0 | 0 = 0
            res = res | last_bit

            # 4️⃣ n >> 1: Dịch n sang phải để bỏ bit vừa dùng
            n = n >> 1

            # res = (res << 1) | (n & 1) => bằng với bước 1,2,3
            # n >>= 1 => bằng với bước 4
            
        return res

def main():
    n = int(input("Nhập số nguyên không âm: "))

    sol1 = Solution()

    print("Cách tối ưu:", sol1.reverseBits(n))


if __name__ == "__main__":
    main()
