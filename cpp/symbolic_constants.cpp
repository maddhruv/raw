#include <iostream>
#include "symb.h"//header file that includes all constants with a namespace constants
#define MAX 30/*bad because harder to debug as debugger shows only the substitute_text not the integer value and
				secondly they have  global scope*/	
using namespace std;

int main(){
	const int maximum(30);//better way to use symbolic constant
	cout<<"#defined way: "<<MAX<<endl;
	cout<<"const way: "<<maximum<<endl;
	cout<<"The value of pi is: "<<constants::pi<<endl;
	return 0;
}