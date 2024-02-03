#include <iostream>
using namespace std;

int main()
{
    // memory leak is studyin here
    int *p_number{new int{1223}};
    int number{22};
    p_number=&number;

    return 0;
}