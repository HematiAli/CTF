#include <stdio.h>
#include <stdint.h>
#include <string.h>

int check(const char *p) {
    if (strlen(p) != 8)
        return 0;

    uint8_t a = p[0];
    uint8_t b = p[1];
    uint8_t c = p[2];
    uint8_t d = p[3];
    uint8_t e = p[4];
    uint8_t f = p[5];
    uint8_t g = p[6];
    uint8_t h = p[7];

    if ((a ^ b) != 0x69)
        return 0;

    if ((b ^ c) != 0x6c)
        return 0;

    if ((c ^ d) != 0x0d)
        return 0;

    if ((d ^ e) != 0x3d)
        return 0;

    if ((e ^ f) != 0x0c)
        return 0;

    if ((f ^ g) != 0x08)
        return 0;

    if ((g ^ h) != 0x18)
        return 0;

    if ((a & h) != 0x52)
        return 0;

    if ((c | f) != 0x7f)
        return 0;

    return 1;
}

int main(void) {
    char input[64];

    printf("Enter the password: ");
    fflush(stdout);

    if (!fgets(input, sizeof(input), stdin))
        return 1;

    input[strcspn(input, "\n")] = '\0';

    if (check(input)) {
        puts("Access granted!");

        printf(
            "unlim{bitwise_%s}\n",
            input
        );
    } else {
        puts("Access denied.");
    }

    return 0;
}
