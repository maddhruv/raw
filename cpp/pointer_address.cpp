#include <iostream>
#include <typeinfo>

using namespace std;

int main(){
	int x(4);
	cout<<typeid(&x).name();
	return 0;.
}