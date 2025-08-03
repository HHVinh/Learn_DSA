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

Node* nhapThongTinNhanVien()
{
    Node* p = new Node;

    cout << "Họ và tên: ";
    cin.ignore(); 
    getline(cin, p->data.HoVaTen);
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
    }
    else
    {   
        int stt = 1;
        while (temp != nullptr)
        {   
            double luong = temp->data.LuongCoBan * temp->data.HeSoLuong;
            if (temp->data.NamSinh == 2000 && luong > 10000000)
            {
                cout << stt++ << "/ ";
                cout << "Họ và tên: " << temp->data.HoVaTen << endl;
            }
            
            temp = temp->pNext;
        }
        if (stt == 1)
        {
            cout << "Không có nhân viên sinh năm 2000 và lương trên 10 triệu!";
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
        Node* p = nhapThongTinNhanVien();
        themVaoCuoiDSLK(LinkedList, p);
    }

    cout << "\n===== DANH SÁCH NHÂN VIÊN =====\n";
    inDanhSachNhanVien(LinkedList);

    giaiPhongDSLK(LinkedList);

    return 0;    
}