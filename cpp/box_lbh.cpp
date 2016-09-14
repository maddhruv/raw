#include<iostream>

using namespace std;
//box with l,b,h;
class box{
  int l,b,h;
 public:
    void setBox(int x, int y, int z){
      l=x;
      b=y;
      h=z;
    }
    void showBox(){
      cout<<l<<endl<<b<<endl<<h<<endl;
    }
};

int main(){
  int a(5);
  int b(10);
  int c(50);
  //object 1
  box box1;
  box1.setBox(a,b,c);
  box1.showBox();
  //object 2
  box box2;
  box2.setBox(c,b,a);
  box2.showBox();
  return 0;
}
