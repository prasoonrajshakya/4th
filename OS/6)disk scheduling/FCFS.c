#include <stdio.h>
#include <stdlib.h>

int main() {
    int request[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int n = sizeof(request) / sizeof(request[0]);
    int head = 53;
    int totalHeadMovement = 0;
    int i;

    printf("Disk Request Queue: ");
    for (i = 0; i < n; i++) {
        printf("%d ", request[i]);
    }

    printf("\nInitial Head Position: %d", head);

    printf("\n\nHead Movement:\n");
    printf("%d", head);                         // print starting position once

    for (i = 0; i < n; i++) {
        totalHeadMovement += abs(head - request[i]);
        head = request[i];

        printf(" -> %d", head);                 // print each new position
    }

    printf("\n\nTotal Head Movement = %d cylinders\n", totalHeadMovement);
    printf("Average Seek Length = %.2f cylinders\n", (float)totalHeadMovement / n);

    return 0;
}
