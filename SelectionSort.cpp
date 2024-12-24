#include <iostream>
using namespace std;

// Function to perform optimized selection sort
void selectionSort(int arr[], int n) {
    // Outer loop to iterate through the entire array
    for (int i = 0; i < n - 1; i++) {
        // Assume the first unsorted element is the minimum
        int minIndex = i;

        // Find the smallest element in the unsorted portion
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        // If minIndex is not the same as i, a swap is needed
        if (minIndex != i) {
            swap(arr[i], arr[minIndex]);
        }

        // Optimization: if no swap happened, the array is already sorted
        if (minIndex == i) {
            break;  // Early exit since the array is already sorted
        }
    }
}

// Function to print the array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};  // Example array
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    printArray(arr, n);

    selectionSort(arr, n);  // Sorting the array using optimized selection sort

    cout << "Sorted array: ";
    printArray(arr, n);

    return 0;
}
