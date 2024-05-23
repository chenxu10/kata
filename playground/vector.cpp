/*User Defined Structurer*/

/*Struct*/


/*Class*/

/*Enum*/
#include <cassert>

struct Vector{
    int sz;
    double* elem;
};

void vector_init(Vector& v, int s){
    v.elem = new double[s];
    v.sz = s;
}

double read_and_sum(int s){
    return 6;    
}

void test_read_and_sum(){
    assert((read_and_sum(5) == 6));
};

int main(){
    test_read_and_sum();
};