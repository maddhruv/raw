#include <iostream>

using namespace std;

class Dhruv{
private:
	int mId;
public:
	Dhruv(int id){
		set(id);
	}
	void set(int id){
		mId = id;
	}
	int get(){
		return mId;
	}
};

int main(){
	Dhruv dhruv(1);
	dhruv.set(1);
	cout<<dhruv.get()<<endl;
	return 0;
}