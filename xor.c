#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <input> <output> <key>\n", argv[0]);
        return 1;
    }

    FILE *in = fopen(argv[1], "rb");
    FILE *out = fopen(argv[2], "wb");
    if (!in || !out) {
        perror("Error opening file");
        return 1;
    }

    const char *key = argv[3];
    size_t key_len = strlen(key);
    if (key_len == 0) {
        fprintf(stderr, "Error: Key cannot be empty\n");
        return 1;
    }

    unsigned char buf[4096];
    size_t bytes_read;
    size_t key_pos = 0;

    while ((bytes_read = fread(buf, 1, sizeof(buf), in)) > 0) {
        for (size_t i = 0; i < bytes_read; i++) {
            buf[i] ^= key[key_pos];
            key_pos = (key_pos + 1) % key_len;
        }
        fwrite(buf, 1, bytes_read, out);
    }

    fclose(in);
    fclose(out);
    return 0;
}
