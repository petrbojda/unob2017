#include <bitset>
#include <iostream>
using namespace std;

void line(), int_to_print_binary(int);

int main()
{
	int x = 0xF0;

	cout	<< "The number to be shifted: ";
	cout << x << " binary: ";
	int_to_print_binary(x);
	cout << endl;
	line();
	cout << endl;

	x >>= 4;
	cout	<< "The number shifted to the right by 4 bits: ";
	cout << x << " binary: ";
	int_to_print_binary(x);
	cout << endl;
	line();
	cout << endl;

	x <<= 2;
	cout	<< "The number shifted back to the left by 2 bits: ";
	cout << x << " binary: ";
	int_to_print_binary(x);
	cout << endl;
	line();
	cout << endl;

	return 0;
}

void line()
{
	cout << "-----------------------------------" << endl;
}

void int_to_print_binary(int num)
{	
	cout << bitset<8>(num);
}
