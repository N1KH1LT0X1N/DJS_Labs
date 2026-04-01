#include <stdio.h>

/* Linear Search: O(n) - checks each element from start to end */
int linear_search(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

/* Binary Search: O(log n) - array must be sorted */
int binary_search(int arr[], int n, int key) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == key)
            return mid;
        if (arr[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

/* Helper: sort array for binary search (simple bubble sort) */
void sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int t = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = t;
            }
        }
    }
}

int main(void) {
    int arr[] = { 40, 10, 30, 20, 50, 60, 25 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int key = 30;  // Hardcoded key to search
    int index;

    printf("Array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n\nSearching for: %d\n\n", key);

    // Linear Search
    printf("1. Linear Search\n");
    index = linear_search(arr, n, key);
    if (index >= 0)
        printf("Linear: Found at index %d\n", index);
    else
        printf("Linear: Not found\n");

    // Binary Search
    printf("\n2. Binary Search (uses sorted array)\n");
    sort(arr, n);
    printf("Sorted array: ");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    index = binary_search(arr, n, key);
    if (index >= 0)
        printf("Binary: Found at index %d\n", index);
    else
        printf("Binary: Not found\n");

    return 0;
}
