#include <iostream>

using namespace std;
//area of square
class area{
  public:
    void sq(int a)
    {
      int r=a*a;
      cout<<r<<endl;
    }
  };
int main(){
  area ob;
  int m=3;
  ob.sq(m);
}
