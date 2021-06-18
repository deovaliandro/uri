// 1010 - Simple Calculate
#include <iostream>
using namespace std;

int main(){
	int a, b, codeA, codeB;
	float pa, pb, total;

	cin >> codeA >> a >> pa;
	cin >> codeB >> b >> pb;
	
	total = (a*pa)+(b*pb);
	printf("VALOR A PAGAR: R$ %0.2f\n", total);

	return 0;
}
