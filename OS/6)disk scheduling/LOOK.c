#include <stdio.h>
#include <stdlib.h>

int main() {
    int request[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int n = sizeof(request) / sizeof(request[0]);

    int head = 53;
    int totalHeadMovement = 0;
    int i, j, temp;

    // Sort the requests
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (request[i] > request[j]) {
                temp = request[i];
                request[i] = request[j];
                request[j] = temp;
            }
        }
    }

    printf("Disk Request Queue: ");
    for (i = 0; i < n; i++) {
        printf("%d ", request[i]);
    }

    printf("\nInitial Head Position: %d", head);
    printf("\nDirection: Towards 200");

    printf("\n\nHead Movement:\n");
    printf("%d", head);

    // Move towards 200 and service requests
    for (i = 0; i < n; i++) {
        if (request[i] >= head) {
            totalHeadMovement += abs(head - request[i]);
            head = request[i];
            printf(" -> %d", head);
        }
    }

    // Reverse direction and service remaining requests
    for (i = n - 1; i >= 0; i--) {
        if (request[i] < 53) {
            totalHeadMovement += abs(head - request[i]);
            head = request[i];
            printf(" -> %d", head);
        }
    }

    printf("\n\nTotal Head Movement = %d cylinders\n", totalHeadMovement);

    return 0;
}
