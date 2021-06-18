// 1011 - Sphere
#include <iostream>
#include <math.h>
using namespace std;

int main(){
    float pi = 3.14159, r, result;
    cin >> r;

    result = (4.0/3) * pi * pow(r, 3);

    printf("VOLUME = %0.3f\n", result);

	return 0;
}
