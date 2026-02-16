# 682. Baseball Game
from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for op in operations:
            if op == "C":
                res.pop()
            elif op == "D":
                # Lấy phần tử cuối cùng nhân 2
                res.append(res[-1] * 2)
            elif op == "+":
                # Cộng 2 phần tử cuối cùng
                res.append(res[-1] + res[-2])
            else:
                res.append(int(op))
        
        # Trả về tổng các phần tử trong mảng
        return sum(res)

if __name__ == "__main__":
    solution = Solution()

    operations = ["5","2","C","D","+"]
    print(solution.calPoints(operations))  # 30