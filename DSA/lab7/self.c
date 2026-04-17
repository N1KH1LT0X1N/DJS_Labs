#include <stdio.h>
#include <stdlib.h>

void main(){
    printf("Enter size of Hashtable: ");
    int size;
    scanf("%d", &size);

    int hashtable[size];
    for(int i=0; i<size; i++){
        hashtable[i] = -1;
    }

    printf("Enter the number you want to insert: ");
    int num;
    scanf("%d", &num);

    int i = 0;
    int hashkey = num % size;
    int hashtable_index = (hashkey + i) % size;

    if(hashtable[hashtable_index] == -1){
        hashtable[hashtable_index] = num;
        printf("Inserted %d at index %d\n", num, hashtable_index);
    }
    else{
        printf("Collision occurred for key %d at index %d\n", num, hashtable_index);
        while(i < size){
            i++;
            hashtable_index = (hashkey + i) % size;
            if(hashtable[hashtable_index] == -1){
                hashtable[hashtable_index] = num;
                printf("Inserted %d at index %d\n", num, hashtable_index);
                return;
            }
            else{
                printf("Collision occurred for key %d at index %d\n", num, hashtable_index);
            }
        }
    }
}