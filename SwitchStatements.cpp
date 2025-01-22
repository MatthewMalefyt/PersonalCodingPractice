#include <iostream>
#include <string>

using namespace std;

int main()
{
    int age = 15;

    switch(age) {                                       //switch statement can save time from making a lot of statements
    case 15:
        cout << "you can graduate college" << endl;
        break;
    case 19:
        cout << "you can go to grad school" << endl;
        break;
    case 21:
        cout << "you can become a tech billionare" << endl;
        break;
    default:
            cout << "Work in tech" << endl;
    }

}

