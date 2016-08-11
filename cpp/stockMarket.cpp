#include<iostream>
#include<cmath>

using namespace std;

int main(){
  float t, my, r, day;
  my = 20000;
  r = 0.02;
  for(day =1; day<=20; day++){
    t=my*powr(1+r, day);
    cout<<day<<"------"<t;
  }
}
