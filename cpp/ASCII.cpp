#include <iostream>
using namespace std;

int main(){
	char ch;
	cout<<"Enter the character to print ASCII value:\n";
	cin>>ch;
	cout<<ch<<" has an ASCII value of \t "<<static_cast<int>(ch)<<endl;
	return 0;
}