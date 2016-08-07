#include <iostream>

using namespace std;
//add 2 nos with arg
int add(int m, int n){
  int r=m+n;
  cout<<r<<endl;
}
int main(){
  int a, b;
  a=2;
  b=3;
  add(a,b);
  return 0;
}
