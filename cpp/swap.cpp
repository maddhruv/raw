#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  int x(2), y(3);
  cout<<"Before swapping: x="<<x<<"\ty="<<y<<endl;
  swap(x,y);
  cout<<"After swapping:  x="<<x<<"\ty="<<y<<endl;
  return 0;
}
