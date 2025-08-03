/*Lab Danh sách liên kết đơn
Họ Tên  : Huỳnh Hữu Vinh
MSSV    : 24880076
*/
#include <iostream>
#include <string>

using namespace std;

struct Node
{
	int data;
	Node* pNext;
};

/* Yêu cầu 1. Khởi tạo một NODE trong DSLK đơn từ một số nguyên k */
Node* CreateNode(int k)
{
	Node* p = new Node; 
	
	/*Sinh viên tự hoàn thành đoạn code này*/

	p->data = k;
	p->pNext = nullptr;

	return p;
}

/* Yêu cầu 2. Thêm số nguyên k vào đầu DSLK đơn */
void InsertFirst(Node*& pHead, int k)
{
	Node* p = CreateNode(k);	//Tạo NODE p từ số nguyên k
	
	/*Sinh viên tự hoàn thành đoạn code này*/
	
	if(pHead == nullptr)
	{
		pHead = p;
	} 
	else
	{
		p->pNext = pHead;
		pHead = p;
	}
}

/* Yêu cầu 3. Thêm số nguyên k vào cuối DSLK đơn */
void InsertLast(Node*& pHead, int k)
{
	Node* p = CreateNode(k);	//Tạo NODE p từ số nguyên k
	
	/*Sinh viên tự hoàn thành đoạn code này*/
	
	if(pHead == nullptr)
	{
		pHead = p;
	}
	else
	{	
		Node* temp = pHead;
		while (temp->pNext != nullptr)
		{
			temp = temp->pNext;
		}
		temp->pNext = p;
	}
}

/* Yêu cầu 4. In toàn bộ số nguyên trong DSLK đơn */
void PrintList(Node* pHead)
{
	/*Sinh viên tự hoàn thành đoạn code này*/

	if(pHead == nullptr)
	{
		std::cout << "Danh sách liên kết rỗng\n";
	}
	else
	{
		Node* temp = pHead;
		int soLuong = 0;
		std::cout << "Các số nguyên trong DSLK là: \n";

		while (temp != nullptr)
		{
			if(temp->data == (int)temp->data)
			{	
				std::cout << "Số thứ " << ++soLuong << " là : " << temp->data << endl;
			}
			temp = temp->pNext;
		}
	}
}

/* Yêu cầu 5. Tìm kiếm số nguyên k trong DSLK đơn. Nếu có trả về true. Ngược lại trả về false */
bool SearchList(Node* pHead, int k)
{
	bool result = false;

	/*Sinh viên tự hoàn thành đoạn code này*/
	
	if(pHead == nullptr)
	{
		return result;
	}

	Node* temp = pHead;

	while (temp != nullptr)
	{
		if(temp->data == k)
		{	
			result = true;
			return result;
		}
		temp = temp->pNext;
	}
	return result;
}

/* Yêu cầu 6. Hoàn thành hàm main() theo yêu cầu */
int main()
{
	Node* pHead = NULL;
	int k;
	do
	{
		std::cout << "Nhap gia tri cua Node (Nhap -1 de ngung thao tac): ";
		std::cin >> k;		
		if (k != -1)
		{
			/*Thêm k vào CUỐI DSLK đơn - Sinh viên tự hoàn thành đoạn code này*/
			
			InsertLast(pHead, k);
		}		
	} while (k != -1);

	
	/*In toàn bộ số nguyên trong DSLK đơn - Sinh viên tự hoàn thành đoạn code này*/
	PrintList(pHead);
	

	/*Nhập vào số nguyên k và kiểm tra k có trong DSLK đơn không - Sinh viên tự hoàn thành đoạn code này*/	

	std::cout << "Nhập số nguyên cần tìm: ";
	std::cin >> k;

	if (SearchList(pHead, k))
	{
		std::cout << k << " có trong danh sách.\n";
	}
	else
	{
		std::cout << k << " không có trong danh sách.\n";
	}
	
	return 0;
}



