#include <iostream>

// Function to calculate the sum of two numbers
int calculateSum(int a, int b){
    return a + b;
}

// Test function for calculateSum
void testCalculateSum() {
    int a = 5, b = 7;
    int expectedResult = 12;
    int actualResult = calculateSum(a, b);

    if (actualResult == expectedResult) {
        std::cout << "Test passed: calculateSum(" << a << ", " << b << ") returned " << actualResult << std::endl;
    } else {
        std::cout << "Test failed: calculateSum(" << a << ", " << b << ") returned " << actualResult << ", but expected " << expectedResult << std::endl;
    }
}

int main() {
    testCalculateSum();
    return 0;
}