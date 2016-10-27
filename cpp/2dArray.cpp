#include <iostream>
#include "midhruvjaink.h"

using namespace std;

int main(){
  int row, column;
  cout<<"Enter the number of rows and columns:\n";
  cin>>row>>column;
  mi::char_repeat('_', 7*column);
  cout<<endl;
  int array[row][column];
  for(int r=0; r<row; r++){
    for(int c=0; c<column; c++){
      array[r][c]=r+c;
    }
  }
  for(int r=0; r<row; r++){
    for(int c=0; c<column; c++){
      cout<<array[r][c]<<"\t";
    }
    cout<<endl;
  }
}
