#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Check if there are enough command line arguments
    if (argc < 2) {
        printf("Usage: %s number1 number2 ...\n", argv[0]);
        return 1;
    }

    // Dynamic memory allocation for the numbers
    int *numbers = malloc((argc - 1) * sizeof(int));
    if (numbers == NULL) {
        perror("Failed to allocate memory");
        return 1;
    }

    // Convert command line arguments to integers and store them in the array
    for (int i = 1; i < argc; i++) {
        numbers[i - 1] = atoi(argv[i]);
    }

    // The threshold value
    int threshold = 170;

    // Iterate through the numbers and print based on the threshold
    for (int i = 0; i < argc - 1; i++) {
        if (numbers[i] > threshold) {
            printf("255 ");
        } else {
            printf("0 ");
        }
    }
    printf("\n");

    // Free the allocated memory
    free(numbers);

    return 0;
}

