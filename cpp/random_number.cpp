#include<iostream>
#include<cstdlib>
#include<ctime>

using namespace std;

int main(){
  int l;
  //generates random numbers every micro second
  srand(time(0));
  for(l=0; l<11; l++){
    cout<<1+(rand()%9)<<endl;
  }
}
