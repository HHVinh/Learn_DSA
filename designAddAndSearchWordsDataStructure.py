class TrieNode:
    def __init__(self):
        self.children = {}      # dictionary: key = ký tự, value = node con
        self.word = False       # đánh dấu node này là kết thúc một từ


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # gốc của Trie

    def addWord(self, word: str) -> None:
        cur = self.root         # bắt đầu từ node gốc
        for c in word:          # duyệt từng ký tự trong word
            if c not in cur.children:          # nếu ký tự chưa có
                cur.children[c] = TrieNode()   # tạo node mới
            cur = cur.children[c] # đi xuống node con
        cur.word = True         # đánh dấu kết thúc từ

    def search(self, word: str) -> bool:
        def dfs(j, root):       # hàm tìm kiếm dùng DFS, j = chỉ số bắt đầu
            cur = root
            for i in range(j, len(word)):  # duyệt từ vị trí j đến hết từ
                c = word[i]
                if c == ".":    # dấu '.' có thể thay bằng bất kỳ ký tự nào
                    for child in cur.children.values():  # thử tất cả nhánh con
                        if dfs(i + 1, child):            # nếu có nhánh khớp thì True
                            return True
                    return False # nếu không nhánh nào khớp thì False
                else:           # ký tự thường
                    if c not in cur.children:  # nếu không có nhánh
                        return False
                    cur = cur.children[c]      # đi tiếp xuống node con
            return cur.word   # chỉ đúng nếu node cuối đánh dấu là một từ

        return dfs(0, self.root) # bắt đầu tìm từ vị trí 0 tại root


# ================== TEST ==================
if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    print(wd.search("pad"))  # False (không có "pad")
    print(wd.search("bad"))  # True  (có "bad")
    print(wd.search(".ad"))  # True  (".ad" khớp với "bad", "dad", "mad")
    print(wd.search("b.."))  # True  ("b.." khớp với "bad")
    print(wd.search("ba"))   # False (chưa kết thúc từ)
