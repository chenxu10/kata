/* Write hello world and sqaure of x*/
#include <iostream>

void hello_world(){
    std::cout << "Hello world" << std::endl;
}


double sqaure(double x){
    return x * x;
}

void printsquare(double x){
    std::cout << "sqaure of x" << x << "is" << sqaure(x) << "\n";
}

int main(){
    double x = 12;
    printsquare(x);
};