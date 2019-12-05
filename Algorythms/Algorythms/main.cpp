#include <iostream>
#include "generator.h"
#include "LSDSort.h"

int main() {
	std::ofstream file, fileskips;
	file.open("out.txt");
	fileskips.open("outskips.txt");
	if (&file == nullptr || &fileskips == nullptr) return 1;

	unsigned int minpower = 0, maxpower = 0, minind = 0, maxind = 0, repeats = 0, numb = 0;

	std::cin >> minpower >> maxpower >> minind >> maxind >> repeats >> numb; // ввод параметров для эксперимента из консоли

	if (minpower == 0 || minpower > maxpower || minind == 0 || minind > maxind || repeats == 0 || numb == 0) return 2;

	for (int i = minpower; i <= maxpower; ++i) {
		for (int j = minind; j <= maxind; ++j) {
			T n = j * numb;
			file << n << ' ' << i << ' ';
			fileskips << n << ' ' << i << ' ';
			begin(LSD_RadixSortBinaryWithComplexity, file, fileskips, n, i, repeats);
			file << std::endl;
			fileskips << std::endl;
		}
	}

	file.close();
	fileskips.close();
	system("pause");
	//system("python graph.py");
}