// WorkingExample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#include "shape.h"

int main()
{
    shape square;

    square.createShape(2.0, 2.0, 2.0);

    std::cout << square.calculateArea() << std::endl;
    std::cout << square.calulateVolume() << std::endl;
}

