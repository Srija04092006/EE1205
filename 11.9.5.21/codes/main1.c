#include <stdio.h>
#include <math.h>

double x1(int n) {
    return (5.0 / 81) * (pow(10, (n + 2)) - 9 * n -19);
}

int main() {
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    for (int n = 0; n <= 5; ++n) {
        double value = x1(n);
        fprintf(file, "%d %lf\n", n, value);
    }

    fclose(file);

    return 0;
}

