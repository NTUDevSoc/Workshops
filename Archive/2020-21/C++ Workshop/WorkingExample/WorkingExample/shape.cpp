#include "shape.h"

void shape::createShape(double len, double wid, double hei) {
	shape::length = len;
	shape::width = wid;
	shape::height = hei;
}

double shape::calculateArea() {
	return shape::length * shape::width;
}

double shape::calulateVolume() {
	return calculateArea() * shape::height;
}