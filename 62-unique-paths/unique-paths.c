int uniquePaths(int m, int n) {
    


int backtracking(int currM, int currN, int**memo){
    if(currM == m-1 && currN == n-1){
        return 1;
    }
    else if(currM >= m || currN >= n){
        return 0;
    }
    if(memo[currM][currN] != -1){
        return memo[currM][currN];
    }
    int right = backtracking(currM+1, currN, memo);
    int left = backtracking(currM, currN+1, memo);
    memo[currM][currN] = right+left;
    return(right+left);
}

int** memo = (int**)malloc(m*sizeof(int*));
for(int i=0;i<m;i++){
    memo[i] = (int*)malloc(n*sizeof(int));
}
for(int i= 0;i<m;i++){
    for(int j=0;j<n;j++){
        memo[i][j] = -1;
    }
}
return(backtracking(0, 0, memo));
    
}