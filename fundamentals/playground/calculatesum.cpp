#include <iostream>
#include <cassert>

// Function to calculate the sum of two numbers

int calculate_sum(int a, int b){
    return a + b;
}

void test_calculateSum(){
    int a = 5, b = 9;
    int actualResult = calculate_sum(a,b);
    int expectedResult = 14;
    assert (actualResult == expectedResult);
}
// Test function for calculateSum

//     if (actualResult == expectedResult) {
//         std::cout << "Test passed: calculateSum(" << a << ", " << b << ") returned " << actualResult << std::endl;
//     } else {
//         std::cout << "Test failed: calculateSum(" << a << ", " << b << ") returned " << actualResult << ", but expected " << expectedResult << std::endl;
//     }
// }

int main(){
    test_calculateSum();
    return 0;
}