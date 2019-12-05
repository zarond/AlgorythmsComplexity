#pragma once

#include <cstdint>

typedef uint64_t T;  // тип данных, используемый в эксперименте

struct testCmplxty { // тип данных, возвращаемый функцией. Сведения об одном эксперименте
	T actions = 0;
	T skips = 0;
};