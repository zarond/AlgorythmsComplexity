#include "generator.h"

// Функция для проверки, отсортирован ли массив
bool ValidateArray(T* A, unsigned int n) {
	for (int i = 0; i < n - 1; ++i)
		if (A[i] > A[i + 1]) return false;
	return true;
}

// Провести один эксперимент для данных массива Data, n количества элементов массива и m - максимального количества разрядов
testCmplxty performtest(testCmplxty(*sorter)(T*, unsigned int, unsigned int), T* Data, unsigned int n, unsigned int m) {
	T* A = new T[n];
	testCmplxty complexity;

	memcpy(A, Data, sizeof(T)*n);
	complexity = sorter(A, n, m);
	if (ValidateArray(A, n) == false) throw("array is not sorted");

	delete[] A;
	return complexity;
}

// Сгенерировать данные и провести repeats экспериментов на этих данных, записать результаты в файлы file и fileskips 
void begin(testCmplxty(*sorter)(T*, unsigned int, unsigned int), std::ofstream &file, std::ofstream &fileskips, unsigned int n, int maxpower, int repeats) {
	std::random_device rd;  //Will be used to obtain a seed for the random number engine
	std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
	std::uniform_int_distribution<T> dis(0);
	
	T* Data;

	Data = new T[n];

	testCmplxty complexity;

	for (int j = 0; j < repeats; ++j) {
		for (int i = 0; i < n; ++i) {
			Data[i] = dis(gen)>>(64-maxpower);
		}

		complexity = performtest(sorter, Data, n, maxpower);
		file << complexity.actions << ' ';
		fileskips << complexity.skips << ' ';
	}

	delete[] Data;
}