#include<stdio.h>
#include<stdio.h> 

int findNextProcess(int at[], int bt[], int is_completed[], int n, int current_time) {
    int min_index = -1;
    int i;
    for (i = 0; i < n; i++) {
        if (at[i] <= current_time && is_completed[i] == 0) {
            if (min_index == -1 || bt[i] < bt[min_index]) {
                min_index = i;
            }
        }
    }
    return min_index;
}

void sjf(int pid[], int at[], int bt[], int wt[], int tat[], int n) {
    int completed = 0, current_time = 0;
    int is_completed[n],i;

    for (i = 0; i < n; i++)
        is_completed[i] = 0;

    while (completed != n) {
        int index = findNextProcess(at, bt, is_completed, n, current_time);
		if (index == -1) {
            current_time++;
        } else {
            wt[index] = current_time - at[index];
            current_time += bt[index];
            tat[index] = wt[index] + bt[index];

            is_completed[index] = 1;
            completed++;
        }
    }
}

void print(int pid[], int at[], int bt[], int wt[], int tat[], int n) {
    float avg_wt = 0, avg_tat = 0;
    int i;
    printf("Process Scheduling: SJF\n");
    printf("\nPID\tAT\tBT\tWT\tTAT\n");

    for (i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\t%d\n",pid[i], at[i], bt[i], wt[i], tat[i]);
        avg_wt += wt[i];
        avg_tat += tat[i];
    }
    printf("Average waiting time= %f\n",avg_wt/n);
    printf("Average turn around time= %f",avg_tat/n);
}

int main() {
    int n = 3;

    int pid[3] = {1, 2, 3};
    int at[3]  = {0, 3, 2};
    int bt[3]  = {3, 5, 4};

    int wt[3], tat[3], ft[3];

    sjf(pid, at, bt, wt, tat, n);

    print(pid, at, bt, wt, tat, n);

    return 0;
}

