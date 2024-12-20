#include <iostream>
#include <string> 
using namespace std;

void FizzBuzz() {
  
    for (int i = 1; i <= 100; i++) {
      string n = ""; 
      
      if (i % 3 == 0)  {
        n = "Fizz";
        cout << n << endl;
      }
      
      
      if (i % 5 == 0)  {
        n = "Buzz";
        cout << n << endl;
      }
      
      
      if (i % 5 == 0 && i % 3 == 0)  {
        n = "FizzBuzz";
        cout << n << endl;
      }
      
      if (n == "")
        cout << i << endl; 
    }
}
