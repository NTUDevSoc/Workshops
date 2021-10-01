#include "Animal.h"

void Animal::setName() {
	std::string myName;
	std::cout << "Enter the animal's name:";
	std::cin >> myName;
	Animal::name = myName;
}

std::string Animal::play(int time) {
	Animal::fullness -= time * 2;
	if (Animal::fullness <= 0) {
		Animal::fullness = 0;
	}
	
	Animal::boredom -= time;
	if (Animal::boredom <= Animal::minBoredom) {
		Animal::boredom = Animal::minBoredom;
		return "content";
	}
	else {
		return "bored";
	}

}

std::string Animal::eat(int amount) {
	Animal::boredom += amount * 2;
	Animal::fullness += amount;
	if (Animal::fullness >= Animal::fullness) {
		Animal::fullness = Animal::maxFullness;
		return "full";
	}
	else {
		return "hungry";
	}
}