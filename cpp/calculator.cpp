#include<iostream>

using namespace std;
int num1, num2, op;
void add(int,int);
void substraction(int,int);
void multiplication(int, int);
void division(int, int);
void scan();
void printOption();
void option(int);

int main(){
  cout<<"++Calculator++"<<endl;
  cout<<"Welcome to Calculator: "<<endl;
  scan();
  printOption();
  cin>>op;
  option(op);
  cout<<endl;
  return 0;
}

void add(int m, int n){
  cout<<m+n;
}
void substraction(int m, int n){
  cout<<m-n;
}
void multiplication(int m, int n){
  cout<<m*n;
}
void division(int m, int n){
  cout<<m/n;
}

void option(int d){
  switch(d){
    case 1:
      add(num1, num2);
      break;
    case 2:
      substraction(num1, num2);
      break;
    case 3:
      multiplication(num1, num2);
      break;
    case 4:
      division(num1, num2);
      break;
    default:
      cout<<"default";
  }
}

void printOption(){
  cout<<"Choose Option: \n 1). Addition \n 2). Substraction \n 3). Multiplication \n 4). Division \n 5). Modulus \n 6). Quit \n";

}
 void scan(){
   cout<<"Enter the two numbers to work upon: "<<endl;
   cin>>num1>>num2;

 }
