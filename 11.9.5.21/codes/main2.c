#include <stdio.h>
#include <math.h>

// Function for x1
double x1(int n) {
    return (5.0 / 81) * (pow(10, (n + 2)) - 9 * n - 19);
}

// Function for x2
double x2(int n) {
    return (2.0 / 27) * (pow(10, -(n + 1)) + 9 * n + 8);
}

int main() {
    // Writing data for x1 to "data_x1.txt"
    FILE *file_x1 = fopen("data_x1.txt", "w");
    if (file_x1 == NULL) {
        printf("Error opening file for writing x1.\n");
        return 1;
    }

    // Writing data for x2 to "data_x2.txt"
    FILE *file_x2 = fopen("data_x2.txt", "w");
    if (file_x2 == NULL) {
        printf("Error opening file for writing x2.\n");
        return 1;
    }

    for (int n = 0; n <= 5; ++n) {
        double value_x1 = x1(n);
        double value_x2 = x2(n);

        fprintf(file_x1, "%d %lf\n", n, value_x1);
        fprintf(file_x2, "%d %lf\n", n, value_x2);
    }

    fclose(file_x1);
    fclose(file_x2);

    return 0;
}

