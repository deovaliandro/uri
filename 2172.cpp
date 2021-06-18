#include <iostream>

int main() {
    int m, n;
    bool aha = false;
    while (aha == false){
        std::cin >> m >> n;
        if (m == 0 && n == 0){
            aha = true;
            break;
        }

        std::cout << (m*n) << std::endl;
        
    }


    return 0;
}