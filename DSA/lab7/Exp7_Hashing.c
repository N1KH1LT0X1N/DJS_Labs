#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 7

typedef struct {
    int key;
    int value;
    int used;
} HashEntry;

FILE *output_file;

// Hash function
int hashFunction(int key) {
    return key % TABLE_SIZE;
}

// Insert element using linear probing
void insert(HashEntry *hashTable, int key, int value) {
    fprintf(output_file, "\nInserting key: %d, value: %d\n", key, value);
    
    int hkey = hashFunction(key);
    fprintf(output_file, "Initial hash index: %d\n", hkey);
    
    int i = 0;
    int index;
    
    while (i < TABLE_SIZE) {
        index = (hkey + i) % TABLE_SIZE;
        fprintf(output_file, "  Trying index: %d", index);
        
        if (hashTable[index].used == 0) {
            hashTable[index].key = key;
            hashTable[index].value = value;
            hashTable[index].used = 1;
            fprintf(output_file, " - INSERTED\n");
            return;
        } else {
            fprintf(output_file, " - OCCUPIED\n");
        }
        
        i++;
    }
    
    fprintf(output_file, "Hash table is full, cannot insert\n");
}

// Search element using linear probing
int search(HashEntry *hashTable, int key) {
    fprintf(output_file, "\nSearching for key: %d\n", key);
    
    int hkey = hashFunction(key);
    fprintf(output_file, "Initial hash index: %d\n", hkey);
    
    int i = 0;
    int index;
    
    while (i < TABLE_SIZE) {
        index = (hkey + i) % TABLE_SIZE;
        fprintf(output_file, "  Checking index: %d", index);
        
        if (hashTable[index].used == 1 && hashTable[index].key == key) {
            fprintf(output_file, " - FOUND! Value: %d\n", hashTable[index].value);
            return hashTable[index].value;
        } else {
            fprintf(output_file, " - NOT FOUND\n");
        }
        
        i++;
    }
    
    fprintf(output_file, "Key not present in hash table\n");
    return -1;
}

// Display hash table
void displayHashTable(HashEntry *hashTable) {
    fprintf(output_file, "\n=== HASH TABLE CONTENTS ===\n");
    fprintf(output_file, "Index | Key  | Value | Status\n");
    fprintf(output_file, "------|------|-------|--------\n");
    
    for (int i = 0; i < TABLE_SIZE; i++) {
        if (hashTable[i].used) {
            fprintf(output_file, "%5d | %4d | %5d | Used\n", i, hashTable[i].key, hashTable[i].value);
        } else {
            fprintf(output_file, "%5d | ---- | ----- | Empty\n", i);
        }
    }
}

int main() {
    output_file = fopen("output.txt", "w");
    if (output_file == NULL) {
        printf("Error: Could not create output file\n");
        return 1;
    }
    
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "EXPERIMENT 7: HASHING\n");
    fprintf(output_file, "====================================\n");
    fprintf(output_file, "Hash Function: key mod %d\n", TABLE_SIZE);
    fprintf(output_file, "Collision Resolution: Linear Probing\n\n");
    
    HashEntry *hashTable = (HashEntry *)malloc(TABLE_SIZE * sizeof(HashEntry));
    
    // Initialize hash table
    for (int i = 0; i < TABLE_SIZE; i++) {
        hashTable[i].used = 0;
    }
    
    int choice;
    int key, value;
    
    while (1) {
        printf("\n--- HASHING MENU ---\n");
        printf("1. Insert element\n");
        printf("2. Search element\n");
        printf("3. Display hash table\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        fprintf(output_file, "\n--- Operation: ");
        
        switch (choice) {
            case 1:
                fprintf(output_file, "INSERT ---\n");
                printf("Enter key: ");
                scanf("%d", &key);
                printf("Enter value: ");
                scanf("%d", &value);
                insert(hashTable, key, value);
                break;
                
            case 2:
                fprintf(output_file, "SEARCH ---\n");
                printf("Enter key to search: ");
                scanf("%d", &key);
                search(hashTable, key);
                break;
                
            case 3:
                fprintf(output_file, "DISPLAY ---\n");
                displayHashTable(hashTable);
                printf("\nHash table displayed in output.txt\n");
                break;
                
            case 4:
                fprintf(output_file, "EXIT ---\n");
                goto exit_loop;
                
            default:
                fprintf(output_file, "INVALID CHOICE ---\n");
                printf("Invalid choice\n");
        }
    }
    
    exit_loop:
    
    fprintf(output_file, "\n====================================\n");
    fprintf(output_file, "CONCLUSION:\n");
    fprintf(output_file, "Learnt the implementation of linear\n");
    fprintf(output_file, "probing used for indexing values in\n");
    fprintf(output_file, "hash tables for efficient storage.\n");
    fprintf(output_file, "====================================\n");
    
    fclose(output_file);
    free(hashTable);
    
    printf("\nOutput written to output.txt\n");
    return 0;
}
