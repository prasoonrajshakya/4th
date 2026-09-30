#include <stdio.h>

void roundRobin(int pid[], int at[], int bt[], int n, int quantum) {
    int rem_bt[n], wt[n], tat[n], ct[n],i, j ;
    for(i=0; i<n; i++)
        rem_bt[i] = bt[i];

    int queue[100], front = 0, rear = 0;
    int visited[n];

    for( i=0; i<n; i++)
        visited[i] = 0;

    int time = 0, completed = 0;

    for( i=0; i<n; i++) {
        if(at[i] == 0) {
            queue[rear++] = i;
            visited[i] = 1;
        }
    }

    while(completed < n) {

        if(front == rear) {
            time++;

            for( i=0; i<n; i++) {
                if(!visited[i] && at[i] <= time) {
                    queue[rear++] = i;
                    visited[i] = 1;
                }
            }
            continue;
        }

        int i = queue[front++];

        if(rem_bt[i] > quantum) {
            time += quantum;
            rem_bt[i] -= quantum;
        }
        else {
            time += rem_bt[i];
            rem_bt[i] = 0;
            ct[i] = time;
            completed++;
        }

        for( j=0; j<n; j++) {
            if(!visited[j] && at[j] <= time) {
                queue[rear++] = j;
                visited[j] = 1;
            }
        }

        if(rem_bt[i] > 0)
            queue[rear++] = i;
    }

    float total_wt = 0, total_tat = 0;

    for(i=0; i<n; i++) {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];

        total_wt += wt[i];
        total_tat += tat[i];
    }

    printf("\nPID\tAT\tBT\tCT\tWT\tTAT\n");
    printf("--------------------------------------------\n");

    for(i=0; i<n; i++)
        printf("%d\t%d\t%d\t%d\t%d\t%d\n",pid[i], at[i], bt[i], ct[i], wt[i], tat[i]);

    printf("\nAverage Waiting Time = %.2f", total_wt/n);
    printf("\nAverage Turnaround Time = %.2f\n", total_tat/n);
}

int main() {
    int pid[] = {1,2,3};
    int at[] = {0,3,5};
    int bt[] = {3,5,4};
    int quantum;

    printf("Enter Time Quantum: ");
    scanf("%d",&quantum);

    roundRobin(pid, at, bt, 3, quantum);

    return 0;
}
