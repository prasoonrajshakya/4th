#include <stdio.h>
#include <limits.h>

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
    int temp[3], distance[3];
    int occupied = 0;
    int i, j, k;
    int max, index = 0;

    pages = sizeof(stream) / sizeof(stream[0]);

    printf("Incoming\tFrame 1\t\tFrame 2\t\tFrame 3\n");

    for (i = 0; i < pages; i++) {
        printf("%d\t\t", stream[i]);

        if (checkHit(stream[i], temp, occupied)) {
            hits++;
            printFrame(temp, occupied);
        }
        else if (occupied < frames) {
            temp[occupied] = stream[i];
            occupied++;
            faults++;

            printFrame(temp, occupied);
        }
        else {
            max = INT_MIN;

            for (j = 0; j < frames; j++) {
                distance[j] = INT_MAX;   // assume never used again

                for (k = i + 1; k < pages; k++) {
                    if (temp[j] == stream[k]) {
                        distance[j] = k - i;   // real distance to next use
                        break;
                    }
                }

                if (distance[j] > max) {
                    max = distance[j];
                    index = j;
                }
            }

            temp[index] = stream[i];
            faults++;

            printFrame(temp, occupied);
        }

        printf("\n");
    }

    printf("\nPage Faults: %d\n", faults);
    printf("Page Hits:   %d\n", hits);

    return 0;
}
