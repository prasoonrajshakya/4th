#include <stdio.h>
#include <stdlib.h>

int main() {
    int request[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int n = sizeof(request)/sizeof(request[0]);
    int head = 53;
    int totalHeadMovement = 0;
    int completed[8] = {0};
    int i, j, closest, distance, minDistance;

    printf("Disk Request Queue: ");
    for (i = 0; i < n; i++) {
        printf("%d ", request[i]);
    }

    printf("\nInitial Head Position: %d\n", head);

    printf("\nHead Movement:\n");
    printf("%d", head);

    for (i = 0; i < n; i++) {
        minDistance = 201;
        closest = -1;

        // Find the closest uncompleted request
        for (j = 0; j < n; j++) {
            if (completed[j] == 0) {
                distance = abs(head - request[j]);

                if (distance < minDistance) {
                    minDistance = distance;
                    closest = j;
                }
            }
        }

        completed[closest] = 1;
        totalHeadMovement += minDistance;
        head = request[closest];

        printf(" -> %d", head);
    }

    printf("\n\nTotal Head Movement = %d cylinders\n", totalHeadMovement);

    return 0;
}
