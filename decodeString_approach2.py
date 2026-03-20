# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []   # Ngăn xếp chuyên để lưu các con số k (số lần lặp)
        string_stack = []  # Ngăn xếp chuyên để lưu các chuỗi chữ cái trước khi chui vào ngoặc
        current_string = "" # Biến hứng chuỗi của lớp hiện tại đang xét
        current_num = 0     # Biến hứng số của lớp hiện tại đang xét

        for char in s:
            if char.isdigit():
                # Kỹ thuật dịch trái hệ thập phân: Nhân số cũ với 10 rồi cộng thêm chữ số mới
                current_num = current_num * 10 + int(char)

            elif char == "[":
                # Gặp dấu '[' nghĩa là sắp chui vào một lớp lồng mới bên trong.
                # Ta phải cất (tạm lưu) trạng thái của lớp CŨ ở bên ngoài vào Stack.
                count_stack.append(current_num)
                string_stack.append(current_string)

                # Sau khi cất xong, phải "dọn dẹp" (reset) 2 biến này về số 0 và chuỗi rỗng
                # để bắt đầu thu thập dữ liệu mới toanh cho lớp bên trong dấu ngoặc này.
                current_num = 0
                current_string = ""

            elif char == "]":
                # Gặp dấu ']' nghĩa là đã xử lý xong lớp bên trong.
                # Ta lấy thông tin của lớp CŨ ở bên ngoài ra để tiến hành ghép nối.
                repeat = count_stack.pop()       # Lấy con số k ra
                prev_string = string_stack.pop() # Lấy chuỗi nằm trước dấu '[' ra

                # Lấy chuỗi MỚI bên trong nhân lên 'repeat' lần, 
                # sau đó dán nó vào ngay sau đuôi của chuỗi CŨ.
                # Kết quả gán ngược lại cho current_string để tiếp tục vòng lặp.
                current_string = prev_string + current_string * repeat

            else:
                # Nếu char là chữ cái bình thường (không phải số, không phải ngoặc)
                # Ta cứ việc cộng nối nó vào chuỗi đang xây dựng ở lớp hiện tại.
                current_string += char

        return current_string
    
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
    print(solution.decodeString("3[a2[c]]"))     # Output: "accaccacc"
    print(solution.decodeString("2[abc]3[cd]ef")) # Output: "abcabccdcdcdef"