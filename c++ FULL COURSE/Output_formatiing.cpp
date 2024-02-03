#include <iostream>
#include <ios>
#include <iomanip>
using namespace std;

int main()
{
    int col_width(14);
    cout << left;
    cout << setw(col_width) << " First Name" << setw(col_width) << "Last name" << setw(col_width) << "age" << endl;
    cout << setw(col_width) << "Rupesh" << setw(col_width) << "Mishra" << setw(col_width) << "20" << endl;
    cout << setw(col_width) << "Shreya" << setw(col_width) << "Joshi" << setw(col_width) << "21" << endl;
    cout << setw(col_width) << "Shreya " << setw(col_width) << "Lakhera" << setw(col_width) << "21" << endl;
    int arr[]{1, 3, 5, 6, 7, 8, 9, 0};
    // int count{size(arr)};// this is not working in my computer and basic of this is sizeof(arrayname)/sizeof(singleelement in the array)
    // cout << "the size of the given arra is " << count;
    char message[]{'r', 'u', 'p', 'e', 's', 'h'};
    char* ptr = {"ehllo"};

    cout << message;
}