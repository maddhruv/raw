#include <iostream>

using namespace std;
//area of rectangle
class area{
  public:
    void rect(int a, int b)
    {
      int r=a*b;
      cout<<r<<endl;
    }
  };
int main(){
  area ob;
  int m=3, n=4;
  ob.rect(m,n);
}
