// 1009 - Salary with Bonus
#include <iostream>
using namespace std;

int main(){
    string name;
    float salary, total, fsalary;
    cin >> name >> salary >> total;
    
    fsalary = salary + ((total*15)/100);
    printf("TOTAL = R$ %0.2f\n", fsalary);

	return 0;
}
