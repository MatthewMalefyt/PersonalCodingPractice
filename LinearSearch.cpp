#include <iostream>

using namespace std;

int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i; // Target found at index i
        }
    }
    return -1; // Target not found
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7, 5, 9};  // Array to search
    int arr_size = sizeof(arr) / sizeof(arr[0]);  // Calculate the number of elements in the array
    int target; 

    // Get user input for the target value
    cout << "Enter the target value to search for: ";
    cin >> target;

    // Call linearSearch function
    int result = linearSearch(arr, arr_size, target);

    // Output the result
    if (result != -1) {
        cout << "Target found at index: " << result << endl;
    } else {
        cout << "Target not found in the array." << endl;
    }

    return 0;
}
