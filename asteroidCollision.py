# 735. Asteroid Collision
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # Điều kiện xảy ra va chạm: 
            # Stack có phần tử VÀ hành tinh đang xét bay sang trái (a < 0) 
            # VÀ hành tinh đỉnh Stack bay sang phải (stack[-1] > 0)
            while stack and a < 0 and stack[-1] > 0:
                
                # Trường hợp 1: Hành tinh đỉnh Stack nhỏ hơn -> nổ tung
                if stack[-1] < -a:
                    stack.pop()
                    continue # Tiếp tục vòng lặp while để xét tiếp hành tinh bên dưới
                
                # Trường hợp 2: Bằng nhau -> Cả 2 cùng nổ
                elif stack[-1] == -a:
                    stack.pop()
                
                # Trường hợp 3: Hành tinh đỉnh Stack lớn hơn -> 'a' nổ tung
                # Nếu rơi vào TH2 (cả 2 cùng nổ) hoặc TH3 ('a' nổ), 
                # thì 'a' không còn tồn tại để đi tiếp nữa, ta thoát vòng lặp while.
                break 
                
            else:
                # Khối lệnh 'else' này đi kèm với 'while' (đặc sản của Python).
                # Nó CHỈ CHẠY khi vòng lặp while kết thúc bình thường (không bị ngắt bởi lệnh 'break').
                # Tức là: Không xảy ra va chạm, HOẶC 'a' đã tông nát hết tất cả hành tinh trong Stack.
                # Khi đó, 'a' sống sót và được đưa vào Stack.
                stack.append(a)
                
        return stack
    
if __name__ == "__main__":   
    solution = Solution()
    
    # Test case 1
    asteroids1 = [5, 10, -5]
    print("Test 1:")
    print("asteroids =", asteroids1)
    print("Result:", solution.asteroidCollision(asteroids1))
    print()
    
    # Test case 2
    asteroids2 = [8, -8]
    print("Test 2:")
    print("asteroids =", asteroids2)
    print("Result:", solution.asteroidCollision(asteroids2))
    print()
    
    # Test case 3
    asteroids3 = [10, 2, -5]
    print("Test 3:")
    print("asteroids =", asteroids3)
    print("Result:", solution.asteroidCollision(asteroids3))