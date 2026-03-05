# 150. Evaluate Reverse Polish Notation
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []     
        operators = {"+", "-", "*", "/"} # Dùng Set để tra cứu toán tử với tốc độ O(1), cực kỳ nhanh
        
        for token in tokens:
            if token not in operators:
                # Nếu không phải toán tử, chắc chắn nó là số
                stack.append(int(token))
            else:
                # Lấy 2 toán hạng ra (chú ý b lấy trước, a lấy sau)
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # Phép chia: dùng int(a / b) thay vì a // b
                    # Điều này đảm bảo số âm luôn được làm tròn về 0 (VD: int(-1/2) = 0)
                    stack.append(int(a / b))
                    
        return stack[0]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9