#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ofstream myfile;
	myfile.open("example.txt");
	myfile<<"Hello, World!\n this is an example file";
	myfile.close();
	return 0;
}