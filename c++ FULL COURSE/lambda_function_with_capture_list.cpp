#include <iostream>

using namespace std;

int main()
{
    int c{454};
    cout << " the address of the variable c is" << &c << endl;
    auto func1 = [c]()
    {
        cout << "the value of the c is " << c << endl;
        // here we can check by using the address
        cout << "the address of the variable c i s" << &c << endl;
    }; // here I am using the lambda function with the caputre list and also as pass by value
    cout << "******************************************************************************************" << endl;
    for (size_t i{0}; i < 5; ++i)
    {
        cout << " the outer value is" << c << endl;
        func1();
        ++c;
    }
    cout << "*************************************************************************************************" << endl;
    // Now from here I am going to use the lambda function by passing by value
    auto func = [&c]()
    {
        cout << "the value of the c is " << c << endl;
        cout << " the address of the c is " << &c << endl;
    };
    cout << "*************************************************************************************************" << endl;
    for (size_t i{0}; i < 5; ++i)
    {
        cout << " the outer value is" << c << endl;
        func();
        ++c;
    }
    cout << "*************************************************************************************************" << endl;
    return 0;
}