#include<iostream>
using namespace std;

int main(){
  cout<<"This program prints the size of every type of varible is consuming."<<endl;

  int integer;
  double doubleInteger;
  char character;
  float floatNumber;
  int intArray[1];
  float floatArray[1];


  cout<< "Variable type ---- Size Occupies"<<endl;
  cout<< "Integer \t --"<< sizeof(integer)<<" bytes"<<endl;
  cout<< "Double Integer   --"<< sizeof(doubleInteger)<<" bytes"<<endl;
  cout<< "character \t --"<< sizeof(character)<<" bytes"<<endl;
  cout<< "Float Number     --"<< sizeof(floatNumber)<<" bytes"<<endl;
  cout<< "Integer Array \t --"<< sizeof(intArray)<<" bytes"<<endl;
  cout<< "Float Array      --"<< sizeof(floatArray)<<" bytes"<<endl;
}
