# ------------------------------------------------------
# Climbing Stairs - số cách leo cầu thang
# Bạn có thể đi 1 hoặc 2 bước tại mỗi lần.
# Trả về số cách khác nhau để đạt tới bậc thứ n.
# ------------------------------------------------------

def climbStairs(n):
    # Nếu n nhỏ hơn hoặc bằng 3 thì có đúng n cách.
    # Ví dụ:
    # n=1 → 1 cách (1)
    # n=2 → 2 cách (1+1, 2)
    # n=3 → 3 cách (1+1+1, 1+2, 2+1)
    if n <= 3:
        return n

    # a là ways[i - 2], b là ways[i - 1]
    # Khởi tạo:
    # a = ways[2] = 2
    # b = ways[3] = 3
    a = 2
    b = 3

    # Bắt đầu tính từ bậc 4 tới n
    for i in range(4, n + 1):
        # Số cách tới bậc i là tổng hai bậc trước đó
        c = a + b

        # Cập nhật 2 biến để chuẩn bị cho vòng tiếp theo
        a = b      # dịch b lên a
        b = c      # dịch c lên b

    # b lúc này là ways[n]
    return b


# Phần dưới cho phép chạy file bằng VS Code
# Khi bạn chạy: python climb_stairs.py
if __name__ == "__main__":
    print("Nhập số bậc n: ", end="")
    n = int(input())

    result = climbStairs(n)
    print(f"Số cách leo tới bậc {n} là: {result}")
