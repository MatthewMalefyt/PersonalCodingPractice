#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// An optimized version of Bubble Sort 
void bubbleSort(int arr[], int n) {
    bool swapped;
  
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
      
        // If no two elements were swapped, then break
        if (!swapped)
            break;
    }
}

// Function to print an array
void printArray(const int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << " " << arr[i];
}

int main() {
    int arr[] = { 64, 34, 25, 12};
    int n = sizeof(arr) / sizeof(arr[0]);  // Calculate size of the array
    bubbleSort(arr, n);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}
}
