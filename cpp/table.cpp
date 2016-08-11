#include<iostream>

using namespace std;

int main(){
  int no, i, max;
  cout<<"Table++ \nEnter the number find the table:";
  cin>>no;
  cout<<"Upto what!!"<<endl;
  cin>>max;
  for (i=1;i<=max;i++){
    cout<<no<<"x"<<i<<"="<<no*i<<endl;
  }
  return 0;
}
