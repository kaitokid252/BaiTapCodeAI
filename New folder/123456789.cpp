#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;
int main()
{
	int l;
	string a,b,c;
	cout <<"Nhap xau goc: ";
	getline(cin,a);
	cout<<"Nhap xau con cu: ";
	getline(cin,b);
	cout<<"Nhap xau con moi: ";
	getline(cin,c);
	l=a.find(b);
	if (l<0)
	{
		cout <<"Xau '"<<b<<"' khong co trong xau '"<<a<<"'";
	}
	else
	{
		a.replace(l,b.size(),c);
		cout <<"Xau goc sau khi thay the: '"<<a<<"'";
	}
}
