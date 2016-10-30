#include <iostream>
#include <cstring>

using namespace std;

int main(){
	char buffer[255], toFind;
	cout<<"Enter the string!\n";
	cin.getline(buffer, 255);
	cout<<"Enter the character to count:\n";
	cin>>toFind;
	int charFound = 0;

	for(int i=0; i<strlen(buffer); i++){
		if(buffer[i]==toFind)
			charFound++;
	}
	cout<<toFind<<" found: "<<charFound<<" times"<<endl;
}