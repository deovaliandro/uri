// 1008 - Salary
#include <iostream>
using namespace std;

int main(){
    int id, hours;
    float salary;

    cin >> id >> hours >> salary;

    printf("NUMBER = %d\n", id);
    printf("SALARY = U$ %0.2f\n", (hours*salary));

	return 0;
}
