#include <stdio.h>

int main() {
    int stream[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2};
    int frames = 3, pages, faults = 0, hits= 0, pointer = 0;
    int temp[frames], i, j, found;

    pages = sizeof(stream) / sizeof(stream[0]);

    printf("Incoming\tFrame 1\t\tFrame 2\t\tFrame 3");

    for (i = 0; i < frames; i++) {
        temp[i] = -1;
    }

    for (i = 0; i < pages; i++) {
        found = 0;

        for (j = 0; j < frames; j++) {
            if (stream[i] == temp[j]) {
                found = 1;
                hits++;
                break;
            }
        }

        if (found == 0) {
            temp[pointer] = stream[i];
            pointer = (pointer + 1) % frames;
            faults++;
        }

        printf("\n%d\t\t", stream[i]);

        for (j = 0; j < frames; j++) {
            if (temp[j] != -1)
                printf("%d\t\t", temp[j]);
            else
                printf("-\t\t");
        }
    }

    printf("\n\nTotal Page Faults: %d\n", faults);
    printf("Page Hits: %d", hits);
    return 0;
}
