#include<iostream>
#include <string>

using namespace std;

class Name{
public:
  void setName(string x){
    name=x;
  }
  string getName(){
    return name;
  }
private:
  string name;
};

int main(){
  Name na;
  na.setName("Dhruv");
  cout<<na.getName()<<endl;
  return 0;
}
