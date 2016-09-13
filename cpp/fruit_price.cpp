#include<iostream>

using namespace std;
//set fruits' price and show price
class fruit{
  int price;
  public:
    void setprice(int x){
      price = x;
    }
    void showprice(){
      cout<<price<<endl;
    }
};

int main(){
  int cost(20);
  fruit apple;
  apple.setprice(cost);
  apple.showprice();
  return 0;
}
