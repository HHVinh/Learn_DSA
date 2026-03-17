# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Tách chuỗi path bằng dấu '/'
        # Ví dụ: "/a//b/./c/" -> ['', 'a', '', 'b', '.', 'c', '']
        components = path.split('/')
        
        for comp in components:
            # Bỏ qua nếu là chuỗi rỗng (do nhiều dấu / liên tiếp tạo ra) 
            # hoặc dấu '.' (đứng im)
            if comp == '' or comp == '.':
                continue
            
            # Nếu gặp '..', ta cần lùi lại 1 cấp (pop khỏi stack)
            elif comp == '..':
                # Chỉ pop khi stack có phần tử (tránh lỗi khi đang ở thư mục gốc)
                if stack:
                    stack.pop()
                    
            # Nếu là tên thư mục hợp lệ, đẩy vào stack
            else:
                stack.append(comp)
                
        # Ghép các phần tử trong stack lại bằng '/', thêm '/' ở đầu
        return '/' + '/'.join(stack)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.simplifyPath("/a//b/./c/"))  # Output: "/a/b/c"
    print(solution.simplifyPath("/../"))          # Output: "/"
    print(solution.simplifyPath("/home//foo/"))   # Output: "/home/foo"