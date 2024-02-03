#include <iostream>
#include <cctype.h>
using namespace std;

int main(){
    //code for searching in the string 
    cout<< endl;
    cout<< "strchr"<<endl;

    const char* str= {"hey this is the string to check"};
    char target;
    cout <<"Enter the character you want to search withn in the string.";<< endl;
    cin>> target;
    const char* result = str;
    int iteration{};
    
    while ((result = strchr(result , target))!= nullptr )
    
    {
        cout<< "found"<<target << "string at" << result << "\n";    /* code */
    }
    


    return 0;
}
    
