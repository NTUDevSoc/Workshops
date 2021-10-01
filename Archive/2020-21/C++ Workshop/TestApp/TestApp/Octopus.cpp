#include "Octopus.h"

void Octopus::escape() {
	if (Octopus::boredom > Octopus::minBoredom * 2) {
		std::cout << Octopus::name + " has escaped!";
		Octopus::boredom = Octopus::minBoredom;
		Octopus::fullness = 10;
	}
	else {
		std::cout << Octopus::name + " is having too much fun to escape!";
	}
}