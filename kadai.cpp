#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)

int greedy(){
    int n;
    vector<vector<int>> Time(n, vector<int> (n));
    vector<int> ans(n);
    rep(i,n){
        int min = 1e10;
        rep(j, n) { 
            ans[i] +=min(Time[i][j]) }
    }
}
int bitDp(int a,int b){
    int n;
    vector<vector<int>> Time(100, vector<int> (100));
    vector<vector<int>> dp((1 << 21), vector<int>(100));

    if(dp[a][b] >=0){
        return dp[a][b];
    }

    if(a==(1<<b)){
        return dp[a][b] = 0;
    }
    int ans = 1e10;
    rep(i,n){
        if(!((a>>i) & 1)){
            ans = min(ans, bitDp(a | 1 << i, i) + Time[b][i]);
        }

    }
    dp[a][b] = ans;
    return ans;
}
int main() {
  //~~~
}