#ifndef ANIMAL_H // include guard
#define ANIMAL_H

#include <string>
#include <iostream>

class Animal
{
private: // members cannot be accessed (or viewed) from outside the class
	int maxFullness = 100;
	int minBoredom = 0;

protected: // members cannot be accessed from outside the class, however, they can be accessed in inherited classes
	std::string name;
	int fullness = 100;
	int boredom = 10;

public: // members are accessible from outside the class
	void setName();
	std::string play(int time);
	std::string eat(int amount);
};

#endif