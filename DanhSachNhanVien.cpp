#include <iostream>
#include <iomanip>
using namespace std;

typedef struct NHANVIEN
{
    string HoVaTen;
    int NamSinh;
    float HeSoLuong;
    double LuongCoBan;
} nv;

typedef struct NODE
{
    nv data;
    NODE* pNext;
} Node;

void khoiTaoDSLK(Node* &pHead)
{
    pHead = nullptr;
}

Node* newNode()
{
    Node* p = new Node; // Cấp phát bộ nhớ

    cout << "Họ và tên: ";
    cin.ignore(); // Xóa dấu xuống dòng nếu có
    getline(cin, p->data.HoVaTen); // getline dùng đọc cả dòng
    cout << "Năm sinh: ";
    cin >> p->data.NamSinh;
    cout << "Hệ số lương: ";
    cin >> p->data.HeSoLuong;
    cout << "Lương cơ bản: ";
    cin >> p->data.LuongCoBan;

    p->pNext = nullptr;

    return p;
}

void themVaoCuoiDSLK(Node* &pHead, Node* pNew)
{
    if(pHead == nullptr)
    {
        pHead = pNew;
    }
    else {
        Node* temp = pHead;

        while (temp->pNext != nullptr)
        {
            temp = temp->pNext;
        }

        temp->pNext = pNew;  
    }
}

void inDanhSachNhanVien(Node* pHead)
{   
    Node* temp = pHead;

    if(temp == nullptr)
    {
        cout << "Danh sách nhân viên rỗng";
        return;
    }
    else
    {   
        int stt = 1;
        while (temp != nullptr)
        {
            cout << "Số thứ tự: " << stt++ << endl;
            cout << "Họ và tên: " << temp->data.HoVaTen << endl;
            cout << "Năm sinh: " << temp->data.NamSinh << endl;
            cout << fixed << setprecision(2); // In đầy đủ và hiển thị đúng phần thập phân là 2 số
            cout << "Hệ số lương: " << temp->data.HeSoLuong << endl;
            cout << "Lương cơ bản: " << temp->data.LuongCoBan << endl;
            cout << "Tổng lương: " << temp->data.LuongCoBan * temp->data.HeSoLuong<< endl;

            temp = temp->pNext;

        }
    }
}

void giaiPhongDSLK(Node* &pHead)
{
    while (pHead != nullptr)
    {
        Node* temp = pHead;
        pHead = pHead->pNext;
        delete temp;
    }
}

int main()
{
    Node* LinkedList;
    khoiTaoDSLK(LinkedList);

    int soLuong;
    cout << "Nhập số lượng nhân viên: ";
    cin >> soLuong;

    for (int i = 0; i < soLuong; i++)
    {
        cout << "\nNhập nhân viên thứ " << i+1 << ": \n";
        Node* p = newNode();
        themVaoCuoiDSLK(LinkedList, p);
    }

    cout << "\n===== DANH SÁCH NHÂN VIÊN =====\n";
    inDanhSachNhanVien(LinkedList);

    giaiPhongDSLK(LinkedList);

    return 0;    
}