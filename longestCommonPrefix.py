from typing import List  # cần import để dùng List[str]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Lấy từ đầu tiên làm prefix ban đầu
        prefix = strs[0]
        
        # Duyệt qua từng chuỗi còn lại trong danh sách
        for string in strs[1:]:
            # Trong khi prefix không khớp với phần đầu của string hiện tại
            # thì cắt bớt prefix từ cuối (mỗi lần bớt 1 ký tự)
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
            
            # Nếu prefix rỗng thì không có prefix chung -> thoát sớm
            if not prefix:
                break
        
        return prefix

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    print("Longest Common Prefix:", result)  # Kết quả mong đợi: "fl"
