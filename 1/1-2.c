#include <stdio.h>
#include <stdlib.h>


int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);  
}

int findFirstOccurrence(int arr[], int size, int target) {
    int low = 0, high = size - 1;
    int result = -1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            result = mid;  // Update result and keep searching in the left half
            high = mid - 1;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return result;
}

int findLastOccurrence(int arr[], int size, int target) {
    int low = 0, high = size - 1;
    int result = -1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target) {
            result = mid;  // Update result and keep searching in the right half
            low = mid + 1;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return result;
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


    for (i=0; i<1000; i++){
    
        int target = firstArray[i];

        int firstIndex = findFirstOccurrence(secondArray, n, target);
        int lastIndex = findLastOccurrence(secondArray, n, target);

        if (firstIndex != -1) {
            printf("First occurrence of %d is at index %d\n", target, firstIndex);
            printf("Last occurrence of %d is at index %d\n", target, lastIndex);
            result += target * (lastIndex - firstIndex + 1);
        } else {
            printf("%d is not in the array.\n", target);
        }

    }

    printf("Result: %d\n", result);
    return 0;

}
