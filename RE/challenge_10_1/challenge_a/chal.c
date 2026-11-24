#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check(int a, int b, int c, int d) {
    if (a < 0 || a > 9)
        return 0;

    if (b < 0 || b > 9)
        return 0;

    if (c < 0 || c > 9)
        return 0;

    if (d < 0 || d > 9)
        return 0;

    if (a + b + c + d != 18)
        return 0;

    if (a * b != 24)
        return 0;

    if (c - d != 2)
        return 0;

    if (a < b)
      return 0;

    if (a <= d)
        return 0;

    return 1;
}

int main(void) {
    char input[32];

    printf("Enter the 4-digit access code: ");
    fflush(stdout);

    if (!fgets(input, sizeof(input), stdin))
        return 1;

    if (strlen(input) < 4) {
        puts("Invalid input.");
        return 1;
    }

    int a = input[0] - '0';
    int b = input[1] - '0';
    int c = input[2] - '0';
    int d = input[3] - '0';

    if (check(a, b, c, d)) {
        puts("Access granted.");
        printf("unlim{z3_%x_%x_%x_%x_stuffffff!}", a, b, c, d);
    } else {
        puts("Access denied.");
    }

    return 0;
}
