#include <stdio.h>
#include <stdlib.h>

FILE *output_file;

// Linear Search - O(n)
int linearSearch(int arr[], int n, int val) {
    fprintf(output_file, "\n--- LINEAR SEARCH ---\n");
    fprintf(output_file, "Searching for value: %d\n", val);
    
    for (int i = 0; i < n; i++) {
        if (arr[i] == val) {
            fprintf(output_file, "Element found at position: %d (index: %d)\n", i + 1, i);
            return i;
        }
    }
    
    fprintf(output_file, "Value is not present in the array\n");
    return -1;
}

// Binary Search - O(log n) - requires sorted array
int binarySearch(int arr[], int n, int key) {
    fprintf(output_file, "\n--- BINARY SEARCH ---\n");
    fprintf(output_file, "Searching for value: %d\n", key);
    
    int low = 0, high = n - 1;
    
    while (high >= low) {
        int mid = (low + high) / 2;
        fprintf(output_file, "Checking mid position: %d, value: %d\n", mid, arr[mid]);
        
        if (key == arr[mid]) {
            fprintf(output_file, "Element found at position: %d (index: %d)\n", mid + 1, mid);
            return mid;
        }
        
        if (key < arr[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    
    fprintf(output_file, "Element not found in the array\n");
    return -1;
}

// Bubble Sort - O(n^2)
void bubbleSort(int arr[], int n) {
    fprintf(output_file, "\n--- BUBBLE SORT ---\n");
    fprintf(output_file, "Original Array: ");
    for (int i = 0; i < n; i++) {
        fprintf(output_file, "%d ", arr[i]);
    }
    fprintf(output_file, "\n");
    
    for (int i = 0; i < n - 1; i++) {
        for (int j = n - 1; j > i; j--) {
            if (arr[j] < arr[j - 1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j - 1];
                arr[j - 1] = temp;
            }
        }
        fprintf(output_file, "Pass %d: ", i + 1);
        for (int k = 0; k < n; k++) {
            fprintf(output_file, "%d ", arr[k]);
        }
        fprintf(output_file, "\n");
    }
    
    fprintf(output_file, "Sorted Array: ");
    for (int i = 0; i < n; i++) {
        fprintf(output_file, "%d ", arr[i]);
    }
    fprintf(output_file, "\n");
}

int main() {
    output_file = fopen("output.txt", "w");
    if (output_file == NULL) {
        printf("Error: Could not create output file\n");
        return 1;
    }
    
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "EXPERIMENT 6: SEARCHING AND SORTING\n");
    fprintf(output_file, "====================================\n");
    
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    fprintf(output_file, "\nNumber of elements: %d\n", n);
    
    int *arr = (int *)malloc(n * sizeof(int));
    int *arr_binary = (int *)malloc(n * sizeof(int));
    
    printf("Enter the elements:\n");
    fprintf(output_file, "Input Array: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        arr_binary[i] = arr[i];
        fprintf(output_file, "%d ", arr[i]);
    }
    fprintf(output_file, "\n");
    
    // Linear Search
    int search_val;
    printf("\nEnter the element to search (for Linear Search): ");
    scanf("%d", &search_val);
    linearSearch(arr, n, search_val);
    
    // Bubble Sort the array for Binary Search
    fprintf(output_file, "\n=== SORTING ARRAY FOR BINARY SEARCH ===\n");
    bubbleSort(arr_binary, n);
    
    // Binary Search
    printf("Enter the element to search (for Binary Search): ");
    scanf("%d", &search_val);
    binarySearch(arr_binary, n, search_val);
    
    // Analysis
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "ANALYSIS OF TIME COMPLEXITY:\n");
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "Linear Search:  O(n)\n");
    fprintf(output_file, "Binary Search:  O(log n)\n");
    fprintf(output_file, "Bubble Sort:    O(n^2)\n");
    
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "CONCLUSION:\n");
    fprintf(output_file, "Thus we have successfully implemented\n");
    fprintf(output_file, "linear and binary searching techniques\n");
    fprintf(output_file, "and bubble sorting.\n");
    fprintf(output_file, "====================================\n");
    
    fclose(output_file);
    free(arr);
    free(arr_binary);
    
    printf("\nOutput written to output.txt\n");
    return 0;
}

