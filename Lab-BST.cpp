/*Viết chương trình C++ cài đặt cấu trúc dữ liệu cây nhị phân tìm kiếm
  Họ và tên SV: Huỳnh Hữu Vinh
  MSSV: 24880076
*/
#include <iostream>

using namespace std;

struct NODE {
    int key;
    NODE *pLeft;
    NODE *pRight;
};

/* Yêu cầu 1. Khởi tạo một NODE từ một số nguyên k chuẩn bị thêm vào cây nhị phân tìm kiếm*/
NODE* createNode(int k) {
    NODE* p = new NODE();

    p->key = k;
	p->pLeft = NULL;
	p->pRight = NULL;

    return p;
}

/* Yêu cầu 2. Viết hàm thêm số nguyên k vào vào cây nhị phân tìm kiếm */
void insertNode(NODE* &pRoot, int k) {
    if (pRoot == NULL) {
        pRoot = createNode(k);
        return;
    }
    if (k < pRoot->key) {
        insertNode(pRoot->pLeft, k);
    } else if (k > pRoot->key) {
        insertNode(pRoot->pRight, k);
    }
}

/* Yêu cầu 3. Viết hàm duyệt trước NLR */
void NLR(NODE* pRoot) {
    if (pRoot != NULL) {
        cout << pRoot->key << " ";
        NLR(pRoot->pLeft);
        NLR(pRoot->pRight);
    }
}

/* Yêu cầu 4. Viết hàm duyệt giữa LNR */
void LNR(NODE* pRoot) {
    if (pRoot != NULL) {
        LNR(pRoot->pLeft);
        cout << pRoot->key << " ";
        LNR(pRoot->pRight);
    }
}

/* Yêu cầu 5. Viết hàm duyệt sau LRN */
void LRN(NODE* pRoot) {
    if (pRoot != NULL) {
        LRN(pRoot->pLeft);
        LRN(pRoot->pRight);
        cout << pRoot->key << " ";
    }
}

/* Yêu cầu 6. Viết hàm tìm kiếm số nguyên k trong cây nhị phân tìm kiếm. 
Nếu có trả về true. Ngược lại trả về false. */
bool searchData(NODE *pRoot, int k) {
    bool result = false;

    if (pRoot == NULL) {
        result = false;
    } else if (pRoot->key == k) {
        result = true;
    } else if (k < pRoot->key) {
        result = searchData(pRoot->pLeft, k);
    } else {
        result = searchData(pRoot->pRight, k);
    }

	return result;
}

/* Yêu cầu 6. Hoàn thành hàm main() theo yêu cầu */
int main() {
    NODE* pRoot = NULL;
	int k;
	do
	{
		cout << "Nhap gia tri cua Node (Nhap -1 de ngung thao tac): ";
		cin >> k;		
		if (k != -1)
		{
			/*Thêm k vào cây nhị phân tìm kiếm - Sinh viên tự hoàn thành đoạn code này*/
			insertNode(pRoot, k);	
		}		
	} while (k != -1);

    /*In toàn bộ số nguyên trong cây theo phép duyệt trước - Sinh viên tự hoàn thành đoạn code này*/
    cout << "NLR: ";
	NLR(pRoot);
    cout << endl;

    /*In toàn bộ số nguyên trong cây theo phép duyệt giữa - Sinh viên tự hoàn thành đoạn code này*/
    cout << "LNR: ";
	LNR(pRoot);
    cout << endl;

    /*In toàn bộ số nguyên trong cây theo phép duyệt sau - Sinh viên tự hoàn thành đoạn code này*/
    cout << "LRN: ";
	LRN(pRoot);
    cout << endl;

    /*Nhập vào số nguyên k và kiểm tra k có trong cây hay không - Sinh viên tự hoàn thành đoạn code này*/	
	cout << "Nhap so nguyen can tim: ";
    cin >> k;
    if (searchData(pRoot, k)) {
        cout << k << " co trong cay." << endl;
    } else {
        cout << k << " khong co trong cay." << endl;
    }

    return 0;
}
