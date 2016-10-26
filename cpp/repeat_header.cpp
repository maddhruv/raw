#include <iostream>
#include <string>
#include "midhruvjaink.h"

using namespace std;

int main(){
  char character;
  int choice;
  double times, integer;
  string line;
  float floating;
  cout<<"What do you want to repeat??\n";
  cout<<"1. Character\n2. Integer\n3. String\n4. Float\n";
  cin>>choice;
  cout<<"How many times do you want it to repeat:\n";
  cin>>times;
  switch (choice) {
    case 1:
      cin>>character;
      mi::char_repeat(character, times);
      break;
    case 2:
      cin>>integer;
      mi::int_repeat(integer, times);
      break;
    case 3:
      getline(cin, line);
      mi::string_repeat(line, times);
      break;
    case 4:
      cin>>floating;
      mi::float_repeat(floating, times);
      break;
    default:
      cout<<"Error!";
      break;
  }
  cout<<endl;
  return 0;
}
