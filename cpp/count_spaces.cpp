#include <iostream>
#include <cstring>

using namespace std;

int main(){
	char buffer[255];
	cout<<"Enter the string!\n";
	cin.getline(buffer, 255);
	int spacesFound = 0;

	for(int i=0; i<strlen(buffer); i++){
		if(buffer[i]==' ')
			spacesFound++;
	}
	cout<<"Spaces Found: "<<spacesFound<<endl;

}