#include <iostream>
#include "NewStuff.h"  //access the header file and thus connect to the NewStuff.cpp file

using namespace std;

int main()                            
{
                                        //   program to have user add to the total 
    int best = 1;
    int number;
    int total = 0;

    while(best <=5){
        cin >> number;
       total = total  +  number;
       best++;
    }

    cout << "Your total is " << total << endl;

    return 0;
}
