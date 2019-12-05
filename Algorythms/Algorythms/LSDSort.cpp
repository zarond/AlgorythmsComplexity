#include "LSDSort.h"
#include "generator.h"

// ������� ���������� ��� �������� ���������� ��������
void LSD_RadixSortBinary(T* A, unsigned int n, unsigned int m) {
	// n - ���������� �����
	// m - ���������� ��������
	// ����������� = 2
	unsigned int* C = new unsigned int[2];
	T* B = new T[n];
	for (T i = 1; i << (63 - m); i <<= 1) {
		C[0] = C[1] = 0;
		for (unsigned int j = 0; j < n; ++j) {
			(A[j] & i) ? 0 : ++C[1]; // ����������� - ������� ������ ���������� ����� � ����� ����������� ������ ��� ������� ������.
		}
		if (C[1] == 0 || C[1] == n) continue; // ������������� ����������� � ������ ���� ��� ������������� ����������� �� �������� �������.
		for (unsigned int j = 0; j < n; ++j) {
			B[C[bool(A[j] & i)]++] = A[j];
		}
		for (unsigned int j = 0; j < n; ++j) {
			A[j] = B[j];
		}
	}
	delete[] C;
	delete[] B;
	return;
}

// ������� ���������� � ��������� ���������� ��������
testCmplxty LSD_RadixSortBinaryWithComplexity(T* A, unsigned int n, unsigned int m) {
	// n - ���������� �����
	// m - ���������� ��������
	// ����������� = 2
	T assign = 0, cmpr = 0, bitshft = 0, bitwand = 0, incr = 0; // ���������� ��� �������� ���������� ��������
	T skips = 0; // ���������� ��� �������� ���������� ��������� �������
	//////////////////
	unsigned int* C = new unsigned int[2];
	T* B = new T[n];
	for (T i = 1; i << (64 - m); i <<= 1) {
		C[0] = C[1] = 0;
		assign += 2;
		for (unsigned int j = 0; j < n; ++j) {
			(A[j] & i) ? 0 : ++C[1] + incr++;
			++cmpr; 
			++bitwand;
		}
		cmpr+=2;
		if (C[1] == 0 || C[1] == n) { ++skips; continue; }
		for (unsigned int j = 0; j < n; ++j) {
			B[C[bool(A[j] & i)]++] = A[j];
			assign++; bitwand++; incr++;
		}
		for (unsigned int j = 0; j < n; ++j) {
			A[j] = B[j];
			assign++;
		}
	}
	delete[] C;
	delete[] B;
	testCmplxty test;
	test.actions = (assign + cmpr + bitwand + incr + bitshft);	// ������������ ��������� ���������� �������� ��� ����������
	test.skips = skips;											// � ������� ��� ���������� ������� �������
	return test;
}
