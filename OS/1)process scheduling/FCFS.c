#include<stdio.h> 
 
void findWaitingTime(int processes[], int n,  int bt[], int wt[]) { 
    // waiting time for first process is 0 
    wt[0] = 0; 
    int i;
    // calculating waiting time 
    for (i = 1; i < n ; i++ ) 
        wt[i] =  bt[i-1] + wt[i-1] ; 
} 
  
void findTurnAroundTime( int processes[], int n,  int bt[], int wt[], int tat[]) { 
    int i;
	for (  i = 0; i < n ; i++) 
        tat[i] = bt[i] + wt[i]; 
} 
  
//Function to calculate average time 
void findavgTime( int processes[], int n, int bt[]) 
{ 
    int wt[n], tat[n], total_wt = 0, total_tat = 0,i; 
  
    findWaitingTime(processes, n, bt, wt); 
   
    findTurnAroundTime(processes, n, bt, wt, tat); 
  
    printf("Processes   Burst time   Waiting time   Turn around time\n"); 
  

    for (i=0; i<n; i++) 
    { 
        total_wt = total_wt + wt[i]; 
        total_tat = total_tat + tat[i]; 
        printf("   %d\t",(i+1));
        printf("\t%d \t", bt[i] );
        printf("\t%d \t",wt[i] );
        printf("\t%d\n",tat[i] ); 
    } 
    float s=(float)total_wt / (float)n;
    float t=(float)total_tat / (float)n;
    printf("Average waiting time = %f\n",s);
    printf("Average turn around time = %f ",t); 
} 

int main() {
    int processes[] = {1, 2, 3}; 
    int n = sizeof processes / sizeof processes[0]; 
  
    //Burst time of all processes 
    int  burst_time[] = {10, 5, 8}; 
  
    findavgTime(processes, n,  burst_time); 
    return 0; 
} 

