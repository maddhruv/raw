#include<iostream>
using namespace std;

//compile error while initialising a data member at the time of declaration of class

class dj{
  int a = 2;

};
int main(){
  cout<<"Hello\n";
  return 0;
}
