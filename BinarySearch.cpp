#include <iostream>
#include <string>

using namespace std;

// Binary Search function
int binarySearch(int arr[], int size, int targetVal) {
    int left = 0;
    int right = size - 1;

    while (left <= right) {
        //int mid = left + (right - left) / 2; // To avoid overflow
        int mid = left + right / 2; //this also works

        if (arr[mid] == targetVal) {
            return mid;  // Target found
        }

        if (arr[mid] < targetVal) {
            left = mid + 1;  // Search in the right half
        } else {
            right = mid - 1;  // Search in the left half
        }
    }

    return -1;  // Target not found
}

int main() {
  
    // Initialize the array and target value
    int myArray[] = {1, 2, 3, 5, 8, 6};
    int myTarget;
    
    cout << "Enter the value to search for: ";
    cin >> myTarget;
    cout << myTarget << endl; 
    
    // Get the size of the array
    int size = sizeof(myArray) / sizeof(myArray[0]);

    // Perform binary search
    int result = binarySearch(myArray, size, myTarget);

    // Output the result
    if (result != -1) {
        cout << "Value " << myTarget << " found at index " << result << endl;
    } else {
        cout << "Target not found in array." << endl;
    }

    return 0;
}
