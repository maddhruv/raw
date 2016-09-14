#include<iostream>
using namespace std;

class dj{
public:
  dj(){
    int a(4);
    cout<<a<<endl;
  }
  void hello(){
    cout<<"hello\n";
  }
};

int main(){
  dj ob;
  ob.hello();
  return 0;
}
