#include <iostream>

using namespace std;
//area of square
class dj{
  private:
    void prmem(){
      cout<<"Private";
    }
  public:
    void pumem(){
      cout<<"Public";
    };
  void prmem();
  void pumem();
  };
int main(){
  dj ob;
  ob.pumem();
  ob.prmem();
}
