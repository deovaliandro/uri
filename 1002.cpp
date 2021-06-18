// 1002 - Area of a Circle
#include <iostream>
#include <math.h>
using namespace std;

int main(){
	float r, pi = 3.14159;
	cin >> r;
	
	float a = pi * pow(r, 2);
	printf("%0.4f\n", a);
	
	return 0;
}
