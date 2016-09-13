#include<iostream>

using namespace std;
//show foors and inches
class distance{
  int f, i;
  public:
    void setDist(int x, int y){
      f = x;
      i = y;
    }
    void showDist(){
      cout<<f<<endl<<i<<endl;
    }
};

int main(){
  int a(5);
  int b(10);
  //distance is conflicting with std::distance
  ::distance ob;
  ob.setDist(a,b);
  ob.showDist();
  return 0;
}
