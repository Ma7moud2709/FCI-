#include <iostream>
using namespace std;

int main(){
	int n1,n2,choice;
	bool flag = true;
	cout << "Enter Number Of Elements In Set (A): ";
	cin >> n1;
	cout << "Enter Number Of Elements In Set (B): ";
	cin >> n2;

	int A[10], B[10];
	for (int i = 0; i < n1; i++) {
		cout << "Enter The Value Of Element[" << i + 1 << "] in Set (A): ";
		cin >> A[i];
	}
	for (int i = 0; i < n2; i++) {
		cout << "Enter The Value Of Element[" << i + 1 << "] in Set (B): ";
		cin >> B[i];
	}
	cout << "Enter the Number of Your Operation:\n[1]A-B \n[2]B-A\n -->";
	cin >> choice;
	
	switch (choice) {
		case 1:
			cout << "A-B = {";
			for (int i = 0; i < n1; i++) {
				for (int j = 0; j < n2; j++) {
					if (A[i] == B[j]) {
						flag = false;
						break;
					}
					else
						flag = true;
				}
				if (flag) {
					cout << A[i] << ",";
				}
			}
			cout << "}";
			break;
		case 2:
			cout << "B-A = {";
			for (int i = 0; i < n2; i++) {
				for (int j = 0; j < n1; j++) {
					if (B[i] == A[j]) {
						flag = false;
						break;
					}
					else
						flag = true;
				}
				if (flag) {
					cout << B[i] << ",";
				}
			}
			cout << "}";
			break;
	}
}