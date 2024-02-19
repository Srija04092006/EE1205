#include <stdio.h>
#include <math.h>

int main() {
    FILE *fp;
    fp = fopen("data.txt", "w");

    if (fp == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    for (int n = 0; n <= 10; ++n) {
        double xn = (5 * (pow(10, n + 1) - 1)) / 9;
        fprintf(fp, "%d %lf\n", n, xn);
    }

    fclose(fp);

    return 0;
}

