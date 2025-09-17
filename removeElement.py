from typing import List  # để khai báo kiểu dữ liệu List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # biến i sẽ là vị trí ghi đè phần tử mới

        # duyệt qua từng phần tử trong mảng nums
        for num in nums:
            if num != val:      # nếu phần tử khác val thì giữ lại
                nums[i] = num   # ghi đè phần tử đó vào vị trí i
                i += 1          # tăng i để chuẩn bị cho lần ghi tiếp theo

        return i  # trả về số lượng phần tử không bằng val


# ====== Chương trình chính để chạy ======
if __name__ == "__main__":
    # nhập mảng từ bàn phím, ví dụ: 3 2 2 3
    nums = list(map(int, input("Nhập mảng (cách nhau bởi khoảng trắng): ").split()))

    # nhập giá trị cần xóa
    val = int(input("Nhập giá trị val cần xóa: "))

    # tạo đối tượng Solution
    sol = Solution()

    # gọi hàm removeElement
    k = sol.removeElement(nums, val)

    # in kết quả
    print("Số phần tử sau khi xóa:", k)
    print("Mảng sau khi xóa (chỉ tính đến k phần tử):", nums[:k])
