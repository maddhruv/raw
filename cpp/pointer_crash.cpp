#include <iostream>

using namespace std;

void dj(int *&p){
	//nothing here	
}

int main(){
	int *p;
	dj(p);
	cout<<*p<<endl;
	return 0;
}