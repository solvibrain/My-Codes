#include <iostream>
using namespace std;

template <typename T>
T maximum(T a, T b)
{
    return a > b ? a : b;
}
int main()
{
    int result = maximum(25, 43);
    cout << " the maximum is " << result << endl;

    return 0;
}