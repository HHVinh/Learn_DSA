class TrieNode:
    def __init__(self):
        self.children = {}       # dictionary lưu các node con theo ký tự
        self.endOfWord = False   # đánh dấu node này là kết thúc một từ

class Trie:

    def __init__(self):
        self.root = TrieNode()   # gốc của cây Trie

    def insert(self, word: str) -> None:
        cur = self.root          # bắt đầu từ node gốc
        for c in word:           # duyệt từng ký tự trong word
            if c not in cur.children:          # nếu chưa có nhánh cho ký tự c
                cur.children[c] = TrieNode()   # tạo node mới
            cur = cur.children[c] # đi xuống node con theo ký tự c
        cur.endOfWord = True     # đánh dấu node cuối cùng là kết thúc của từ

    def search(self, word: str) -> bool:
        cur = self.root          # bắt đầu từ gốc
        for c in word:           # duyệt từng ký tự
            if c not in cur.children: # nếu không tìm thấy nhánh thì trả về False
                return False
            cur = cur.children[c]     # đi xuống node con
        return cur.endOfWord     # chỉ đúng nếu từ này kết thúc tại node cuối

    def startsWith(self, prefix: str) -> bool:
        cur = self.root          # bắt đầu từ gốc
        for c in prefix:         # duyệt từng ký tự prefix
            if c not in cur.children: # nếu ký tự không tồn tại thì sai
                return False
            cur = cur.children[c]     # đi xuống node con
        return True              # nếu duyệt hết prefix thì trả về True


# ================== TEST ==================
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    print(trie.search("apple"))    # True  (apple có trong Trie)
    print(trie.search("app"))      # True  (app cũng có trong Trie)
    print(trie.search("appl"))     # False (chỉ là prefix, không phải từ hoàn chỉnh)
    print(trie.startsWith("ap"))   # True  (có từ bắt đầu bằng 'ap')
    print(trie.startsWith("ban"))  # True  (có từ bắt đầu bằng 'ban')
    print(trie.startsWith("bat"))  # False (không có từ nào bắt đầu bằng 'bat')
