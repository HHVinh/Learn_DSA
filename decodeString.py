# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                # Xử lý số có nhiều chữ số (Ví dụ '1' rồi '2' -> 12)
                # B1: current_num ban đầu là 0, khi gặp '1' -> current_num = 0 * 10 + 1 = 1
                # B2: khi gặp '2' tiếp theo -> current_num = 1 * 10 + 2 = 12
                current_num = current_num * 10 + int(char)
                
            elif char.isalpha():
                # Xử lý chữ cái, cộng dồn vào chuỗi của lớp hiện tại
                current_str += char
                
            elif char == '[':
                # Gặp mở ngoặc: Lưu lại trạng thái của lớp CŨ vào stack
                # Đóng gói thành tuple (số_k_của_lớp_mới, chuỗi_đã_có_trước_đó)
                stack.append((current_num, current_str))
                
                # Reset biến để bắt đầu thu thập dữ liệu cho lớp MỚI bên trong
                current_num = 0
                current_str = ""
                
            elif char == ']':
                # Gặp đóng ngoặc: Lớp hiện tại đã xong, cần lôi lớp CŨ ra để ghép nối
                prev_num, prev_str = stack.pop()
                
                # Trong Python, chuỗi nhân với số nguyên sẽ tự lặp lại
                # Ví dụ: "c" * 2 = "cc"
                # Nối chuỗi cũ với chuỗi mới vừa được nhân lên
                current_str = prev_str + (current_str * prev_num)
                
        return current_str

if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
    print(solution.decodeString("3[a2[c]]"))     # Output: "accaccacc"
    print(solution.decodeString("2[abc]3[cd]ef")) # Output: "abcabccdcdcdef"