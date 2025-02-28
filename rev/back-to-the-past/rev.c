#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define BUFFER_SIZE 4096

int main(int argc, char **argv) {
    if(argc < 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }
    
    const time_t start_seed = 1717214400;
    const time_t end_seed = 1714536000;
    const char *flag = "PWNME";
    unsigned char buffer[BUFFER_SIZE];
    
    for(time_t seed = start_seed; seed >= end_seed; --seed) {
        srand(seed);
        FILE *fp = fopen(argv[1], "rb");
        if(!fp) {
            printf("Can't open file %s\n", argv[1]);
            return 1;
        }
        
        size_t bytes_read = 0;
        int c;
        while((c = fgetc(fp)) != EOF && bytes_read < sizeof(buffer)) {
            int key = rand();
            int mod_key = key - ((key/0x7F) * 0x7F);
            buffer[bytes_read++] = mod_key ^ c;
        }
        fclose(fp);
        
        if(bytes_read >= strlen(flag)) {
            void *found = memmem(buffer, bytes_read, flag, strlen(flag));
            if(found) {
                printf("Found valid seed: %ld\n", seed);
                fwrite(buffer, 1, bytes_read, stdout);
                return 0;
            }
        }
    }
    
    printf("No valid seed found in range\n");
    return 1;
}
