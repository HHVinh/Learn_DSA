class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        countMax = 0                  # Độ dài dãy liên tiếp dài nhất tìm được tới hiện tại

        setNum = set(nums)            # Dùng set để tra cứu O(1) và loại trùng

        for num in setNum:            # Duyệt từng số (không bị lặp vì đã là set)
            if (num - 1) not in setNum:   # Chỉ bắt đầu đếm khi 'num' là ĐẦU CHUỖI (không có num-1)
                count = 1                 # Tính luôn chính 'num'
                while (num + count) in setNum:  # Mở rộng sang phải: num+1, num+2, ...
                    count += 1
                countMax = max(count, countMax) # Cập nhật kỷ lục dài nhất
        return countMax                 # Trả về độ dài dãy liên tiếp dài nhất
    
# Nhập dữ liệu: các số cách nhau bởi khoảng trắng, chuyển sang int
nums = list(map(int, input("Nhập dãy số cách nhau bởi khoảng trắng: ").split()))
s = Solution()
print(s.longestConsecutive(nums))

