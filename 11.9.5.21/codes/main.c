#include <stdio.h>
#include <math.h>

double x2(int n) {
    return (2.0 / 27) * (pow(10, -(n + 1)) + 9 * n + 8);
}

int main() {
    FILE *file = fopen("dat.txt", "w");
    if (file == NULL) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    for (int n = 0; n <= 5; ++n) {
        double value = x2(n);
        fprintf(file, "%d %lf\n", n, value);
    }

    fclose(file);

    return 0;
}

