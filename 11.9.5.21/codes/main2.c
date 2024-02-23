#include <stdio.h>
#include <math.h>

double x1(int n) {
    return (5.0 / 81) * (pow(10, (n + 2)) - 9 * n - 19);
}

double x2(int n) {
    return (2.0 / 27) * (pow(10, -(n + 1)) + 9 * n + 8);
}

int main() {
    FILE *file_stem1, *file_scatter1, *file_stem2, *file_scatter2;

    // Open files for writing for sequence 1
    file_stem1 = fopen("theory1.dat", "w");
    file_scatter1 = fopen("simulate1.dat", "w");

    if (file_stem1 == NULL || file_scatter1 == NULL) {
        printf("Error opening files for sequence 1!\n");
        return 1;
    }

    for (int n = 0; n <= 5; ++n) {
        double value_x1 = x1(n);
        fprintf(file_stem1, "%d %lf\n", n, value_x1);
        fprintf(file_scatter1, "%d %lf\n", n, value_x1);
    }

    // Close the files for sequence 1
    fclose(file_stem1);
    fclose(file_scatter1);

    // Open files for writing for sequence 2
    file_stem2 = fopen("theory2.dat", "w");
    file_scatter2 = fopen("simulate2.dat", "w");

    if (file_stem2 == NULL || file_scatter2 == NULL) {
        printf("Error opening files for sequence 2!\n");
        return 1;
    }

    for (int n = 0; n <= 5; ++n) {
        double value_x2 = x2(n);
        fprintf(file_stem2, "%d %lf\n", n, value_x2);
        fprintf(file_scatter2, "%d %lf\n", n, value_x2);
    }

    // Close the files for sequence 2
    fclose(file_stem2);
    fclose(file_scatter2);

    return 0;
}

