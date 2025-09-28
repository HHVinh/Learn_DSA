from typing import List
from collections import deque  # Dùng deque để duyệt BFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Mảng indegree lưu số lượng môn học cần phải học trước (bậc vào) cho từng môn
        indegree = [0] * numCourses

        # Danh sách kề (adj) để lưu các môn học phụ thuộc vào môn khác
        adj = [[] for _ in range(numCourses)]

        # Xây dựng đồ thị và mảng indegree
        for src, dst in prerequisites:
            indegree[dst] += 1     # Môn 'dst' có thêm một môn tiên quyết
            adj[src].append(dst)   # Môn 'dst' phụ thuộc vào môn 'src'

        # Hàng đợi chứa các môn không có tiên quyết (indegree = 0)
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        # Biến đếm số môn đã hoàn thành
        finish = 0

        # Bắt đầu duyệt BFS
        while q:
            node = q.popleft()
            finish += 1  # Hoàn thành môn này

            # Giảm indegree cho các môn phụ thuộc vào môn vừa học xong
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # Nếu số môn hoàn thành == tổng số môn => có thể học hết
        return finish == numCourses


# --- Đoạn code để chạy thử ---
if __name__ == "__main__":
    solution = Solution()

    # Ví dụ 1: Có thể hoàn thành hết các môn
    numCourses = 2
    prerequisites = [[1, 0]]  # Học 0 trước, sau đó học 1
    print("Ví dụ 1:", solution.canFinish(numCourses, prerequisites))  # True

    # Ví dụ 2: Không thể hoàn thành (có vòng lặp phụ thuộc)
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]  # 0 cần 1, 1 cần 0 => vòng lặp
    print("Ví dụ 2:", solution.canFinish(numCourses, prerequisites))  # False
