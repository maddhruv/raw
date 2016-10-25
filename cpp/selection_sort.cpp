#include <iostream>
#include <algorithm>

using namespace std;

int main(){
  const int length(5);
  int array[length] = {30,10,40,60,20};
  for(int startIndex = 0; startIndex<length; ++startIndex){
    int smallestIndex = startIndex;
    for(int currentIndex = startIndex+1; currentIndex<length; ++currentIndex){
      if (array[currentIndex]<array[smallestIndex])
      smallestIndex = currentIndex;
    }
    swap(array[startIndex], array[smallestIndex]);
  }
  for(int index=0; index<length; index++){
    cout<<array[index]<<endl;
    return 0;
  }
}
