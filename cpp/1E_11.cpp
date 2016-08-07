#include <iostream>

using namespace std;
//area of rectangle
int area(int m, int n){
  int area=m*n;
  cout<<area<<endl;
}
int main(){
  int a, b;
  a=2;
  b=3;
  area(a,b);
  return 0;
}
