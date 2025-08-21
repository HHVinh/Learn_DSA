class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        # stack dùng để lưu các dấu ngoặc mở, hoạt động theo cơ chế LIFO (vào sau ra trước)

        closeToOpen = {")": "(", "]": "[", "}": "{"}
        # Đây là dictionary (dict) ánh xạ từ ngoặc đóng sang ngoặc mở tương ứng
        # Ví dụ: closeToOpen[")"] == "("
        #        closeToOpen["]"] == "["

        for c in s:  # Duyệt từng ký tự trong chuỗi
            if c in closeToOpen:
                # Nếu ký tự c là ngoặc đóng (")", "]", "}")
                
                if stack and stack[-1] == closeToOpen[c]:
                    # stack: check xem stack có phần tử không (tương đương len(stack) > 0)
                    # stack[-1]: lấy phần tử trên cùng của stack (ngoặc mở gần nhất)
                    # closeToOpen[c]: tìm ngoặc mở tương ứng với ngoặc đóng c
                    # Nếu khớp -> pop ngoặc mở ra (vì đã đóng đúng)
                    stack.pop()
                else:
                    # Nếu không khớp hoặc stack rỗng -> chuỗi không hợp lệ
                    return False
            else:
                # Nếu ký tự là ngoặc mở ("(", "[", "{") thì đưa vào stack
                stack.append(c)

        # Kết thúc vòng lặp:
        # Nếu stack rỗng -> tất cả ngoặc mở đều có cặp đóng đúng -> True
        # Nếu stack còn phần tử -> còn ngoặc chưa đóng -> False
        return True if not stack else False
    
sol = Solution()
s = input("Nhập chuỗi các dấu: ")
print(sol.isValid(s))

