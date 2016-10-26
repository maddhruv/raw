#include <iostream>
#include <string>

using namespace std;

int main(){
	int choice;
	cout<<"Enter your choice:\n";
	cin>>choice;
	cin.ignore(32767,'\n');
	//ignore or delete the \n character in the cin expression on input
	string name;
	getline(cin, name);
	cout<<name<<endl<<choice<<endl;
	cout<<"the length of the string is: "<<name.length()<<endl;
	return 0;
}
