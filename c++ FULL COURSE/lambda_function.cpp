#include <iostream>
using namespace std;

int main()
{
    auto func = []()
    {
        cout << "Hllo world , From the Greatest GEnius ever Born on the planet" << endl;
    };
    func(); // lambda Function.
    // there is also another way to call the fucntion wthout assigning into any variable.
    []()
    {
        cout << "Hllo world , From the Greatest GEnius ever Born on the planet" << endl;
    }(); // here the bracket after the curly braces is being used to call this function by itself
/* from here the function is being written in the form of its full form .*/
    auto result = [](double a, double b) -> double
    {
        return (a + b);
    };
    double result_ = result(23.5, 563.5);
    cout << "the resutl for the above funda is " << result_ << endl;

    return 0;
}
