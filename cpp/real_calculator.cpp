#include<iostream>
#include<cmath>

using namespace std;

int main(){
  float inod, od, total;
  char ot;
  cin>>inod;
  cin>>ot;
  cin>>od;
  switch (ot){
    case '+':
      od = od + inod;
      break;
    case '-':
      od = inod - od;
      break;
    case '*':
      od = od*inod;
      break;
    case '/':
      od = inod/od;
      if(inod == 0 && od == 0){
        cout<<"Not defined!";
      }
      break;
    default:
      cout<<endl;
  }
  total = od;
  cin>>ot;
  //loop starts
  while(ot=='+' || ot=='-' || ot=='*' || ot=='/'){
    cin>>od;
    switch (ot) {
      case '+':
        total = od + total;
        break;
      case '-':
        total = total - od;
        break;
      case '*':
        total = od*total;
        break;
      case '/':
        total = total/od;
        if(total == 0 && od == 0){
          cout<<"Not defined!";
        }
        break;
      default:
        cout<<endl;
    }
    cin>>ot;
  }
  cout<<total<<endl;
  cout<<"exiting...";
}
