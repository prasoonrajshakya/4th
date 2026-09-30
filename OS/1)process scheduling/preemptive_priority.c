#include <stdio.h>

void preemptivePriority(int pid[], int at[], int bt[], int pr[], int n) {
    int rem_bt[20], ct[20], wt[20], tat[20];
    int i, highest;
    int completed = 0;
    int time = 0;
    float total_wt = 0, total_tat = 0;

    for(i = 0; i < n; i++)
        rem_bt[i] = bt[i];

    while(completed < n) {

        highest = -1;

        for(i = 0; i < n; i++) {
            if(at[i] <= time && rem_bt[i] > 0) {
                if(highest == -1 || pr[i] < pr[highest])
                    highest = i;
            }
        }

        if(highest == -1) {
            time++;
            continue;
        }

        rem_bt[highest]--;
        time++;

        if(rem_bt[highest] == 0) {
            ct[highest] = time;
            completed++;
        }
    }

    for(i = 0; i < n; i++) {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];

        total_wt += wt[i];
        total_tat += tat[i];
    }

    printf("\nPID\tAT\tBT\tPR\tCT\tWT\tTAT\n");
    printf("----------------------------------------------------\n");

    for(i = 0; i < n; i++) {
        printf("%d\t%d\t%d\t%d\t%d\t%d\t%d\n",pid[i], at[i], bt[i], pr[i], ct[i], wt[i], tat[i]);
    }

    printf("\nAverage Waiting Time = %.2f", total_wt / n);
    printf("\nAverage Turnaround Time = %.2f\n", total_tat / n);
}

int main() {
    int n = 4;

    int pid[] = {1, 2, 3, 4};
    int at[]  = {0, 1, 2, 3};
    int bt[]  = {4, 3, 1, 2};

    /* Smaller value = Higher Priority */
    int pr[]  = {2, 1, 3, 2};

    preemptivePriority(pid, at, bt, pr, n);

    return 0;
}
