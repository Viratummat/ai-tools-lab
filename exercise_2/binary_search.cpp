#include <iostream>
using namespace std;

/**
 * Find target in sorted array using binary search.
 * 
 * @param arr Sorted array of integers
 * @param size Size of array
 * @param target Value to find
 * @return Index of target, or -1 if not found
 */
int binarySearch(int arr[], int size, int target) {
    int left = 0;
    int right = size - 1;
    
    while (left <= right) {
        int mid = (left + right) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

int main() {
    int numbers[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int size = 10;
    
    cout << "Searching for 7: " << binarySearch(numbers, size, 7) << endl;      // 3
    cout << "Searching for 1: " << binarySearch(numbers, size, 1) << endl;      // 0
    cout << "Searching for 19: " << binarySearch(numbers, size, 19) << endl;    // 9
    cout << "Searching for 10: " << binarySearch(numbers, size, 10) << endl;    // -1
    
    return 0;
}