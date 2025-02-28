#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

// Custom PRNG implementation
uint64_t seed;

void srand_custom(int32_t arg1) {
    seed = (uint64_t)(arg1 - 1);  // Matches decompiled srand behavior
}

uint32_t rand_custom() {
    seed = 0x5851f42d4c957f2d * seed + 1;
    return (uint32_t)(seed >> 33);  // Return upper 31 bits
}

int is_all_printable(const uint8_t *buf, size_t len) {
    for (size_t i = 0; i < len; i++) {
        if (buf[i] < 32 || buf[i] > 126) return 0;
    }
    return 1;
}

int main() {
    // Read encrypted file
    FILE *fp = fopen("flag.enc", "rb");
    fseek(fp, 0, SEEK_END);
    size_t len = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    uint8_t *cipher = malloc(len);
    fread(cipher, 1, len, fp);
    fclose(fp);

    // May 2024 range (UTC)
    const uint32_t start = 1714521600;
    const uint32_t end = 1717199999;

    // Brute-force loop
    for (uint32_t ts = start; ts <= end; ts++) {
        uint8_t *plain = malloc(len);
        srand_custom(ts);  // Seed set to ts-1 per decompiled code
        
        // Decrypt with custom PRNG
        for (size_t i = 0; i < len; i++) {
            plain[i] = cipher[i] ^ (rand_custom() % 127);
        }

        if (is_all_printable(plain, len)) {
            printf("Potential plaintext (seed %u):\n", ts);
            printf("%.*s\n\n", (int)len, plain);
        }
        
        free(plain);
    }

    free(cipher);
    return 0;
}

