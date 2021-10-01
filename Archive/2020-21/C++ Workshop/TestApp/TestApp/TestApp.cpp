// TestApp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include "Octopus.h"

void testFileHandling();
void testVectors();

int main()
{
	std::cout << "Welcome to your Zoo!\nYou get one pet, an Octopus!" << std::endl;
	Octopus myPet;
	myPet.setName();

	std::string temp;
	int choice;
	int input;

	do {
		std::cout << "\n0: Exit \n1: Feed Octopus \n2: Play with your Octopus\n3: Octo-Escape\n4: Test file handling"
			"\n5: Test Vectors" << std::endl;
		std::cin >> temp;
		choice = stoi(temp);

		switch (choice) {
		case 1:
			std::cout << "How much do you want to feed them?" << std::endl;
			std::cin >> temp;
			input = stoi(temp);
			std::cout << "Your Octopus is " << myPet.eat(input) << std::endl;
			continue;

		case 2:
			std::cout << "How long do you want to play for?" << std::endl;
			std::cin >> temp;
			input = stoi(temp);
			std::cout << "Your Octopus is " << myPet.play(input) << std::endl;
			continue;

		case 3:
			myPet.escape();
			continue;

		case 4:
			testFileHandling();
			continue;
		case 5:
			testVectors();
			continue;
		default:
			continue;
		}
	} while (choice != 0);

	return 0;
}

void testFileHandling() {
	// Write a line to the end of the file
	std::ofstream writeFile;
	writeFile.open("TestFile.txt", std::ios::app); // writes to file in append
	
	std::string input;
	std::cout << "Enter what you want added to the file: ";
	std::cin >> input;
	writeFile << input;

	writeFile.close();

	// Reading the file
	std::ifstream readFile;
	readFile.open("TestFile.txt");

	if (!readFile) { // Checking if the file exists ( this is important for checking things )
		std::cout << "No file found" << std::endl;
		return;
	}

	std::string line;
	while (!readFile.eof()) {
		std::getline(readFile, line);
		std::cout << line << std::endl;
	}
	readFile.close(); // Dont forget to close your file
}

void testVectors() {

	std::vector<int> testVec{ 1, 2, 3, 4, 5 };

	for (int i = 0; i < testVec.size(); i++) {
		std::cout << testVec.at(i) << std::endl;
	}

	for (auto it = testVec.rbegin(); it < testVec.rend(); it++) {
		std::cout << *it << std::endl;
	}
} 
