#include <iostream>
using namespace std;
char s[5]="ABCX",a[5],
      d[4], ss[4]="DEF";
int b[5],bb[4],dem=0;
void xuat()
{
     char c[7];
     int i=0,j=0;
     while(a[i]!=0)  //a[i] chua rong thi lam tiep
     {
           if (a[i]=='X')   //neu gap X thi se thay cac hoan vi cua DEF vao
           {
                c[j]=d[0];
                c[j+1]=d[1];
                c[j+2]=d[2];
                j=j+3;
           }
           else
           {
                c[j]=a[i];    //gan hoan vi vua tim vao de in
                j++;
           }
           i++;
     }
     	dem++;
    	cout<<dem<<".";
    	for(i=0;i<6;i++)
    	cout<<c[i];
    	cout<<"\n";
}
void hoanvi3(int n) //su dung thuat toan quay lui de tim hoan vi cua DEF
{
     for(int k=0;k<3;k++)
     if (bb[k])   //de kiem tra xem da co xau con chua
     {
           d[n]=ss[k];
           if (n==2)           //neu tim duoc het hoan vi DEF thi xuat du lieu
		   xuat();
           else
           {
                bb[k]=0;    //danh dau la da gan
                hoanvi3(n+1);  //chay de quy den khi xuat hoan vi
                bb[k]=1;   //chay xong thi gan lai ban 1(true) de quay lui lai de gan tiep voi xau con tiep theo
           }
     }
}
void hoanvi(int i) //thuat toan quay lui ABCX
{
     for(int j=0;j<4;j++)
     if (b[j])   //de kiem tra xem da co xau con chua
     {
           a[i]=s[j];   	
           if (i==3)   //neu tim het hoan vi cua ABCX thi goi lenh hoanvi3(0) de chay tim hoan vi DEF thay vao X va xuat
		   hoanvi3(0);  
           else
           {
                b[j]=0;       //danh dau la gan
                hoanvi(i+1);   // chay de quy den khi chay den lam hoanvi3()
                b[j]=1;   //chay xong thi gan lai ban 1(true) de quay lui lai de gan tiep voi xau con tiep theo
           }
     }
}
int main()
{
     a[4];
     for(int i=0;i<5;i++) 
	 b[i]=1;				//danh dau neu nhu van bang 1(true) thi gan hoan vi vao cua DEF
     for(int i=0;i<4;i++) 
	 bb[i]=1;	//danh dau neu nhu van bang 1(true) thi gan hoan vi vao cua ABCX(X se thay bang hoan vi DEF)
     hoanvi(0);
     getch();
}
