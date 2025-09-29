from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Tạo dictionary ánh xạ mỗi môn học -> danh sách môn tiên quyết
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Tập hợp lưu các môn đang nằm trên đường duyệt DFS
        visiting = set()

        # Hàm DFS kiểm tra xem có thể hoàn thành môn 'crs' không
        def dfs(crs):
            if crs in visiting:
                # Nếu gặp lại môn đang trong đường DFS -> phát hiện chu kỳ
                return False
            if preMap[crs] == []:
                # Nếu môn này không còn môn tiên quyết -> có thể học được
                return True

            # Đánh dấu môn hiện tại đang được duyệt
            visiting.add(crs)

            # Kiểm tra tất cả môn tiên quyết của môn hiện tại
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # Xóa khỏi tập "visiting" sau khi duyệt xong
            visiting.remove(crs)

            # Ghi nhớ rằng môn này đã xử lý xong (không cần duyệt lại sau này)
            preMap[crs] = []
            return True

        # Kiểm tra tất cả các môn
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


# --- Chạy thử ---
if __name__ == "__main__":
    solution = Solution()

    # Ví dụ 1: Có thể hoàn thành
    numCourses = 2
    prerequisites = [[1, 0]]  # Học 0 trước, rồi học 1
    print("Ví dụ 1:", solution.canFinish(numCourses, prerequisites))  # True

    # Ví dụ 2: Không thể hoàn thành (có vòng lặp)
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]  # 0 cần 1, 1 cần 0
    print("Ví dụ 2:", solution.canFinish(numCourses, prerequisites))  # False
