#include <iostream>

void line(), message();

int main()
{
	std::cout	<< "The program starts with the main()."
				<< std::endl;
	line();
	message();
	line();
	std::cout << "At the end of the main()." << std::endl;

	return 0;
}

void line()
{
	std::cout << "-----------------------------------" << std::endl;
}

void message()
{
	std::cout << "In function message() printing on the screen." << std::endl;
}
