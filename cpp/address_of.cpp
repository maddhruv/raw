#include <iostream>

using namespace std;

int main(){
	int x(5);
	cout<<"the address of var x is: "<<&x<<endl;
	//dereference operator
	cout<<*&x;<<endl
	return 0;
}