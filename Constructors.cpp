#include <iostream>                 //Basics of Constructors
#include <string>

using namespace std;

class MatthewsClass {
    public:                         //public can be used by main() to access variables
                                    //good practice to put variables in private so they cannot be accessed and changed easily

        MatthewsClass (string z) {          //This is a constructor that gets called automatically (same name as class)
            setName(z);                     //Notes:  It is used to initialize the data members of new objects. It constructs the values i.e. provides data for the object which is why it is known as a constructor.

        }

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

    MatthewsClass MatthewsObject("Lucky Matthew Malefyt");  //creating object to access stuff inside of class
   cout << MatthewsObject.getName();                         // constructor is set to object


    MatthewsClass MatthewsObject2("Sally McSalad");     //Does not overwrite MatthewsObject
    cout << MatthewsObject2.getName();                  //You can create multiple objects from the same class w/o overwriting!!
    return 0;                                           //They are each assigned to different variables 
}
                                                        
