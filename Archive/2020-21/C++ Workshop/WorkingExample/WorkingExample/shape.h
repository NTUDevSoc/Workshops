#ifndef SHAPE_H // include guard
#define SHAPE_H

class shape
{
private: 
	double length;
	double width;
	double height;

public:
	void createShape(double len, double wid, double hei);

	double calculateArea();

	double calulateVolume();

};

#endif