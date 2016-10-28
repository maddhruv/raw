#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int printer();

int main(){
	string name, headerFiles;
	cout<<"Enter the name of the file you want to create(without .cpp extension):\n";
	getline(cin,name);
	cout<<name[0];
	name += ".cpp";
	cout<<"Want to include another header file(iostream is already included):\n";
	getline(cin,headerFiles);
	//creates the file here
	ofstream theFile;
	theFile.open(name.c_str());
	//header files
	theFile<<"#include <iostream>\n";
	theFile<<"#include <"<<headerFiles<<">\n";
	//namespace
	theFile<<"\nusing namespace std;\n\n";
	//main fxn
	theFile<<"int main(){\n";
	theFile<<"\tcout<<\"the first generated program\"<<endl;";
	theFile<<"}";
	theFile.close();
	return 0;
}
