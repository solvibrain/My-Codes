#include <iostream>
using namespace std;

class Square{
    private:
        double dimension{1.0};
    public:
        Square(){
            cout<<"Want to calculate the Area of the Square:"<<endl;
            cout<< "with the same value or the value you want to put the different";
        }
        double area();       
};

int main(){


    return 0;
}