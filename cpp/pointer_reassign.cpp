#include <iostream>

using namespace std;

int main(){
	int v1(5);
	int v2(6);
	int *ptr;
	ptr = &v1;
	cout<<*ptr<<endl;
	ptr = &v2;
	cout<<*ptr<<endl;
	*ptr = 7;
	cout<<*ptr<<endl;
	return 0;
}