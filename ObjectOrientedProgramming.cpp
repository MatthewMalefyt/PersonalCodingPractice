#include <iostream>                 //Object Oriented Programming Basics
#include <string>

using namespace std;

class MatthewsClass {
    public:                         //public can be used by main() to access variables
                                    //good practice to put variables in private so they cannot be accessed and changed easily

        void setName(string x) {    //function to allow for the name to be changed (set to x)
            name = x;
        }
        string getName() {          //function to get the name from the private class
            return name;
        }
    private:                        //private variables can only be accessed inside the class
        string name;
};

int main()
{

    MatthewsClass MatthewsObject ();                   //creating object to access stuff inside of class
    MatthewsObject.setName("Sir Matthew Malefyt");  //object.function to access inside of function setName
    cout << MatthewsObject.getName();               //object.function to access inside of function getName which connects to private class


  
    //DO NOT DO THIS. THIS WOULD BE IF YOUR VARIABLE WAS PUBLIC. DO NOT MAKE THE VARIABLE PUBLIC (variable can be accessed outside of class)!!!
    /*
    MatthewsClass MatthewsObject;
    MatthewsObject.name = "Matthew Malefyt";
    cout << MatthewsObject.name;
    */
    return 0;
}


