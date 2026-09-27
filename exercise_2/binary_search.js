/**
 * Find target in sorted array using binary search.
 * 
 * @param {number[]} arr - Sorted array of numbers
 * @param {number} target - Value to find
 * @return {number} Index of target, or -1 if not found
 */
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;
    
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        
        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

// Test it
const numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];

console.log(`Searching for 7: ${binarySearch(numbers, 7)}`);      // 3
console.log(`Searching for 1: ${binarySearch(numbers, 1)}`);      // 0
console.log(`Searching for 19: ${binarySearch(numbers, 19)}`);    // 9
console.log(`Searching for 10: ${binarySearch(numbers, 10)}`);    // -1