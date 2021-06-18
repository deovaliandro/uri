// 1017 - Fuel Spent
#include <iostream>
using namespace std;

int main(){
    int time, averange;
    float distance, result;

    cin >> time >> averange;
    
    distance = time*averange;
    result = distance/12;

    printf("%0.3f\n", result);

	return 0;
}
