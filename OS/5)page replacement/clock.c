#include <stdio.h>

int checkHit(int page, int temp[], int occupied) {
    int i;

    for (i = 0; i < occupied; i++) {
        if (page == temp[i])
            return 1;
    }

    return 0;
}

void printFrame(int temp[], int occupied) {
    int i;

    for (i = 0; i < occupied; i++)
        printf("%d\t\t", temp[i]);
}

int main() {
    int stream[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2};
    int frames = 3, pages, faults = 0, hits = 0;
    int temp[frames], bit[frames];
    int occupied = 0, pointer = 0;
    int i, j, found;

    pages = sizeof(stream) / sizeof(stream[0]);

    for (i = 0; i < frames; i++)
        bit[i] = 0;

    printf("Incoming\tFrame 1\t\tFrame 2\t\tFrame 3\n");

    for (i = 0; i < pages; i++) {
        printf("%d\t\t", stream[i]);

        found = 0;

        for (j = 0; j < occupied; j++) {
            if (stream[i] == temp[j]) {
                bit[j] = 1;
                found = 1;
                break;
            }
        }

        if (found == 1) {
        	hits++;
            printFrame(temp, occupied);
        }
        else if (occupied < frames) {
            temp[occupied] = stream[i];
            bit[occupied] = 1;
            occupied++;
            faults++;

            printFrame(temp, occupied);
        }
        else {
            while (bit[pointer] == 1) {
                bit[pointer] = 0;
                pointer = (pointer + 1) % frames;
            }

            temp[pointer] = stream[i];
            bit[pointer] = 1;
            pointer = (pointer + 1) % frames;
            faults++;

            printFrame(temp, occupied);
        }

        printf("\n");
    }

    printf("\nPage Faults: %d\n", faults);
    printf("Page Hits: %d\n", hits);
    return 0;
}
