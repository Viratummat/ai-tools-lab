/**
 * Binary search implementation in Java.
 */
public class BinarySearch {
    
    /**
     * Find target in sorted array using binary search.
     * 
     * @param arr Sorted array of integers
     * @param target Value to find
     * @return Index of target, or -1 if not found
     */
    public static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        
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
    
    public static void main(String[] args) {
        int[] numbers = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        
        System.out.println("Searching for 7: " + binarySearch(numbers, 7));      // 3
        System.out.println("Searching for 1: " + binarySearch(numbers, 1));      // 0
        System.out.println("Searching for 19: " + binarySearch(numbers, 19));    // 9
        System.out.println("Searching for 10: " + binarySearch(numbers, 10));    // -1
    }
}