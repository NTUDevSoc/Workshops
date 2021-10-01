#ifndef OCTOPUS_H // include guard
#define OCTOPUS_H

#include "Animal.h"
class Octopus :
    public Animal
{
private:
    int maxFullness = 70;
    int minBoredom = 30;

public:
    void escape();
};

#endif

