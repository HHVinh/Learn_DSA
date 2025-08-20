from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = defaultdict(int)  # bảng đếm trong cửa sổ
        res, l, maxf = 0, 0, 0

        for r in range(len(s)):           # mở rộng cửa sổ bằng con trỏ phải
            m[s[r]] += 1                  # thêm ký tự s[r]
            maxf = max(maxf, m[s[r]])     # cập nhật tần suất lớn nhất

            while (r - l + 1) - maxf > k: # Nếu số ký tự cần thay > k, co cửa sổ
                m[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

    def characterReplacement2(self, s: str, k: int) -> int:
        count = {}
        res, l, maxf = 0, 0, 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

if __name__ == "__main__":
    print("=== Longest Repeating Character Replacement ===")
    print("Bạn sẽ nhập chuỗi s và số k (số ký tự được phép thay đổi).")
    s = input("Nhập chuỗi s: ").strip()

    while True:
        k_str = input("Nhập k (số nguyên ≥ 0): ").strip()
        try:
            k = int(k_str)
            if k < 0:
                print("⚠️  k phải ≥ 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("⚠️  k phải là số nguyên. Vui lòng nhập lại.")

    sol = Solution()
    ans1 = sol.characterReplacement(s, k)
    ans2 = sol.characterReplacement2(s, k)

    print("\n--- KẾT QUẢ ---")
    print(f"characterReplacement  (tối ưu)   => {ans1}")
    print(f"characterReplacement2 (dễ hiểu)  => {ans2}")

