#ifndef MIDHRUVJAINK_H
#define MIDHRUVJAINK_H
#include <string>

namespace mi{
  //character repeat function
  int char_repeat(char x, int times){
    for(int i=0; i<times; i++){
      std::cout<<x;
    }
  }
  //integer repeat function
  int int_repeat(double x, int times){
    for(int i=0; i<times; i++){
      std::cout<<x;
    }
  }
  //string repeat function
  int string_repeat(std::string x, int times){
    for(int i=0; i<times; i++){
      std::cout<<x;
    }
  }
  //float repeat function
  int float_repeat(float x, int times){
    for(int i=0; i<times; i++){
      std::cout<<x;
    }
  }

}

#endif
