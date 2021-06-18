// 1012 - Area
#include <iostream>
#include <math.h>
using namespace std;

int main(){
    float a, b, c, pi = 3.14159;

    cin >> a >> b >> c;

    float i = (a*c)/2;
    float j = pi*pow(c, 2);
    float k = ((a+b)/2)*c;
    float l = b*b;
    float m = a*b;

    printf("TRIANGULO: %0.3f\n", i);
    printf("CIRCULO: %0.3f\n", j);
    printf("TRAPEZIO: %0.3f\n", k);
    printf("QUADRADO: %0.3f\n", l);
    printf("RETANGULO: %0.3f\n", m);

	return 0;
}
