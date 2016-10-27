#include <iostream>
using namespace std;

int main()
{
	const double gravity(9.8);
	const double electron;//error: uninitialized const ‘electron’ [-fpermissive] const double electron
	gravity = 10;//error: assignment of read-only variable ‘gravity’ gravity = 10
	return 0;
}