/*User Defined Structurer*/

/*Struct*/


/*Class*/

/*Enum*/
#include <cassert>
#include <iostream>
using namespace std;

struct Vector{
    int sz;
    double* elem;
};

void vector_init(Vector& v, int s){
    v.elem = new double[s];
    v.sz = s;
}

double read_and_sum(int s){
    Vector v;
    vector_init(v,s);
    
    // for (int i = 0; i < s; ++i) {
    //     cin >> v.elem[i];
    // }  

    double sum = 0.0;
    for (int i=0; i<s; ++i){
        sum += v.elem[i];
    };

    cout << "Sum :" << sum << endl;
    return sum;
}

void test_read_and_sum(){
    assert((read_and_sum(5) == 6));
};

int main(){
    read_and_sum(3);
    // test_read_and_sum();
};