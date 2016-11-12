#include <iostream>

using namespace std;

class hello{
private:
	int p;
public:
	hello(){
		p = 0;
	}
	int set(int i){
		p += i;
		return p;
	};
	friend int hm(hello &hello);
};

int hm(hello &hello){
	hello.p = 0;
	return hello.p;
}

int main(){
	hello ob;
	ob.set(2);
	cout<<ob.set(3)<<endl;	
	cout<<hm(ob)<<endl;
	return 0;
}