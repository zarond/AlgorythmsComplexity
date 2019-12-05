#pragma once

#include <iostream>
#include <fstream>
#include "structs.h"
#include <random>

bool ValidateArray(T* A, unsigned int n);

testCmplxty performtest(testCmplxty(*sorter)(T*, unsigned int, unsigned int), T* Data, unsigned int n = 50000000, unsigned int m = 64);
void begin(testCmplxty(*sorter)(T*, unsigned int, unsigned int), std::ofstream &file, std::ofstream &fileskips, unsigned int n, int maxpower, int repeats);