#include <stdio.h>
#include <stdlib.h>


int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);  
}

int main() {
    FILE *myFile;
    myFile = fopen("1.txt", "r");

    //read file into array
    int firstArray[1000];
    int secondArray[1000];
    int result = 0;
    int i;

    int j = 0;
    int k = 0;
    for (i = 0; i < 2000; i++)
    {
        if (i % 2 == 0) {
            fscanf(myFile, "%d", &firstArray[j]);
            j++;
        } else {
            fscanf(myFile, "%d", &secondArray[k]);
            k++;
        }
        
    }

    for (i =0; i < 1000; i++){
        printf("Number from 1st list is: %d\n\n", firstArray[i]);
        printf("Number from 2nd list is: %d\n\n", secondArray[i]);
    }

    int n = sizeof(firstArray) / sizeof(firstArray[0]);

    qsort(firstArray, n, sizeof(int), compare);
    qsort(secondArray, n, sizeof(int), compare);

    // Find and print the minimum element in arr
    for (i=0; i<1000; i++){
        result += abs(firstArray[i] - secondArray[i]);

    }
    printf("Result: %d\n", result);
    return 0;

}
