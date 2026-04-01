#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX_SIZE 100000

// Global counters for performance analysis
long long selection_comparisons = 0;
long long selection_swaps = 0;
long long quick_comparisons = 0;
long long quick_swaps = 0;

// ==================== SELECTION SORT ====================
// Time Complexity: O(n^2) - all cases
// Space Complexity: O(1)
// Stability: Not stable

void selection_sort(int arr[], int n) {
    selection_comparisons = 0;
    selection_swaps = 0;
    
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        
        // Find the minimum element in remaining unsorted array
        for (int j = i + 1; j < n; j++) {
            selection_comparisons++;
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        
        // Swap the found minimum element with first element
        if (min_idx != i) {
            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
            selection_swaps++;
        }
    }
}

// ==================== QUICK SORT ====================
// Time Complexity: O(n log n) average, O(n^2) worst
// Space Complexity: O(log n) - recursive stack
// Stability: Not stable

int partition(int arr[], int low, int high) {
    // Choose rightmost element as pivot
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        quick_comparisons++;
        if (arr[j] < pivot) {
            i++;
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            quick_swaps++;
        }
    }
    
    // Swap arr[i+1] and arr[high] (pivot)
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    quick_swaps++;
    
    return i + 1;
}

void quick_sort_helper(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quick_sort_helper(arr, low, pi - 1);
        quick_sort_helper(arr, pi + 1, high);
    }
}

void quick_sort(int arr[], int n) {
    quick_comparisons = 0;
    quick_swaps = 0;
    quick_sort_helper(arr, 0, n - 1);
}

// ==================== UTILITY FUNCTIONS ====================

// Copy array
void copy_array(int src[], int dest[], int n) {
    for (int i = 0; i < n; i++) {
        dest[i] = src[i];
    }
}

// Verify if array is sorted
int is_sorted(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return 0;
        }
    }
    return 1;
}

// Print array
void print_array(int arr[], int n, int show_all) {
    if (show_all) {
        for (int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
            if ((i + 1) % 10 == 0) printf("\n");
        }
        printf("\n");
    } else {
        printf("[");
        for (int i = 0; i < (n < 10 ? n : 10); i++) {
            printf("%d", arr[i]);
            if (i < (n < 10 ? n - 1 : 9)) printf(", ");
        }
        if (n > 10) printf(", ... (total %d elements)", n);
        printf("]\n");
    }
}

// Generate random array
void generate_random_array(int arr[], int n, int max_val) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % max_val;
    }
}

// Generate worst case (reverse sorted) array
void generate_worst_case_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = n - i;
    }
}

// ==================== PERFORMANCE TESTING ====================

void test_sorting(int test_size, const char* test_case_name) {
    int *arr1 = (int *)malloc(test_size * sizeof(int));
    int *arr2 = (int *)malloc(test_size * sizeof(int));
    
    if (!arr1 || !arr2) {
        printf("Memory allocation failed!\n");
        return;
    }
    
    printf("\n=== Test Case: %s (Size: %d) ===\n", test_case_name, test_size);
    
    if (strcmp(test_case_name, "Random") == 0) {
        generate_random_array(arr1, test_size, 10000);
    } else if (strcmp(test_case_name, "Worst Case") == 0) {
        generate_worst_case_array(arr1, test_size);
    } else {
        // Best case - already sorted
        for (int i = 0; i < test_size; i++) {
            arr1[i] = i;
        }
    }
    
    copy_array(arr1, arr2, test_size);
    
    // Test Selection Sort
    clock_t start = clock();
    selection_sort(arr1, test_size);
    clock_t end = clock();
    double sel_time = ((double)(end - start) / CLOCKS_PER_SEC) * 1000;
    
    printf("\nSelection Sort:\n");
    printf("  Time: %.4f ms\n", sel_time);
    printf("  Comparisons: %lld\n", selection_comparisons);
    printf("  Swaps: %lld\n", selection_swaps);
    printf("  Sorted: %s\n", is_sorted(arr1, test_size) ? "YES" : "NO");
    
    // Test Quick Sort
    start = clock();
    quick_sort(arr2, test_size);
    end = clock();
    double quick_time = ((double)(end - start) / CLOCKS_PER_SEC) * 1000;
    
    printf("\nQuick Sort:\n");
    printf("  Time: %.4f ms\n", quick_time);
    printf("  Comparisons: %lld\n", quick_comparisons);
    printf("  Swaps: %lld\n", quick_swaps);
    printf("  Sorted: %s\n", is_sorted(arr2, test_size) ? "YES" : "NO");
    
    printf("\nPerformance Analysis:\n");
    printf("  Speedup: %.2fx (Quick Sort is %.2fx %s)\n", 
           (sel_time / quick_time), 
           (sel_time / quick_time),
           (quick_time < sel_time) ? "faster" : "slower");
    
    free(arr1);
    free(arr2);
}

// ==================== MAIN ====================

int main() {
    printf("========================================\n");
    printf("  SORTING ALGORITHM PERFORMANCE ANALYSIS\n");
    printf("  Selection Sort vs Quick Sort\n");
    printf("========================================\n");
    
    srand(time(0));
    
    // Test with different array sizes
    int test_sizes[] = {100, 1000, 5000};
    char test_cases[][20] = {"Random", "Best Case", "Worst Case"};
    
    for (int i = 0; i < 3; i++) {
        printf("\n\n+============================================+\n");
        printf("|          SIZE: %d ELEMENTS              |\n", test_sizes[i]);
        printf("+============================================+\n");
        
        for (int j = 0; j < 3; j++) {
            test_sorting(test_sizes[i], test_cases[j]);
        }
    }
    
    // Additional detailed test
    printf("\n\n+============================================+\n");
    printf("|        DETAILED COMPARISON TEST           |\n");
    printf("+============================================+\n");
    
    int *test_arr1 = (int *)malloc(50 * sizeof(int));
    int *test_arr2 = (int *)malloc(50 * sizeof(int));
    
    printf("\nOriginal Array:\n");
    for (int i = 0; i < 50; i++) {
        test_arr1[i] = rand() % 100;
    }
    print_array(test_arr1, 50, 0);
    
    copy_array(test_arr1, test_arr2, 50);
    
    selection_sort(test_arr1, 50);
    printf("\nAfter Selection Sort:\n");
    print_array(test_arr1, 50, 0);
    printf("Comparisons: %lld, Swaps: %lld\n", selection_comparisons, selection_swaps);
    
    quick_sort(test_arr2, 50);
    printf("\nAfter Quick Sort:\n");
    print_array(test_arr2, 50, 0);
    printf("Comparisons: %lld, Swaps: %lld\n", quick_comparisons, quick_swaps);
    
    free(test_arr1);
    free(test_arr2);
    
    printf("\n\n+============================================+\n");
    printf("|           SUMMARY & CONCLUSIONS           |\n");
    printf("+============================================+\n");
    printf("\nSelection Sort:\n");
    printf("  - Predictable O(n²) performance\n");
    printf("  - Works well on small datasets\n");
    printf("  - Minimal extra space needed\n");
    printf("  - Better for memory-constrained systems\n");
    printf("\nQuick Sort:\n");
    printf("  - Average O(n log n) performance\n");
    printf("  - Much faster on large datasets\n");
    printf("  - Worst case O(n²) with poor pivot selection\n");
    printf("  - Industry standard for general-purpose sorting\n");
    printf("\nRecommendation:\n");
    printf("  Use Quick Sort for better average performance.\n");
    printf("  Use Selection Sort for educational purposes or very small arrays.\n");
    
    return 0;
}
