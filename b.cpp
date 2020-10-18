#include <bits/stdc++.h>
//#include <atcoder/all>
#define rep(i, n) for (int i = 0; i < (n); ++i)
// using namespace atcoder;
using namespace std;
using ll = long long;
using P = pair<ll, ll>;
//マクロ
// forループ関係
//引数は、(ループ内変数,動く範囲)か(ループ内変数,始めの数,終わりの数)、のどちらか
// Dがついてないものはループ変数は1ずつインクリメントされ、Dがついてるものはループ変数は1ずつデクリメントされる
#define FOR(i, a, b) for (ll i = a; i <= (ll)(b); i++)
#define _GLIBCXX_DEBUG
// xにはvectorなどのコンテナ
#define ALL(x) (x).begin(), (x).end()  // sortなどの引数を省略したい
#define SIZE(x) ((ll)(x).size())       // sizeをsize_tからllに直しておく
#define MAX(x) *max_element(ALL(x))    //最大値を求める
#define MIN(x) *min_element(ALL(x))    //最小値を求める
//定数
#define INF 1000000000000  // 10^12:極めて大きい値,∞
#define inf 2147483647     // int値の最大値
#define MOD 1000000007     // 10^9+7:合同式の法
#define MAXR 100000        // 10^5:配列の最大のrange(素数列挙などで使用)
//略記
#define PB push_back                             // vectorヘの挿入
#define MP make_pair                             // pairのコンストラクタ
#define F first                                  // pairの一つ目の要素
#define S second                                 // pairの二つ目の要素
#define CST(x) cout << fixed << setprecision(x)  //小数点以下の桁数指定
template <class T> inline bool chmin(T &a, T b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}
template <class T> inline bool chmax(T &a, T b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}
int gcd(int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}
int lcm(int a, int b) {
    return a * b / gcd(a, b);
}
//各桁の和
int sumDight(int x) {
    int sum = 0;
    while (x > 0) {
        sum += (x % 10);
        x /= 10;
    }
    return sum;
}
//回文数
int divideReverse(int x) {
    int reverse = 0;
    int r;
    while (x > 0) {
        r = x % 10;
        reverse = reverse * 10 + r;
        x /= 10;
    }
    return reverse;
}

int how_many_times(int N) {
    int exp = 0;
    while (N % 2 == 0) N /= 2, ++exp;
    return exp;
}
int GCD(int m,int n){
    if (n == 0) return m;

    return GCD(n,m%n)
}
bool func(int i,int w,const vector<int> &a){
    if(i==0){
        if (w == 0) return true;
        else
            return false;
    }

    if (func(i, w, a)) return true;
    if (func(i, w - a[i - 1], a)) return true;
    return false;
}
vector<int> memo;
int tribo(int n) {
    if (n == 0) return 0;
    if (n == 1) return 0;
    if (n == 2) return 1;

    if (memo[n] != -1) return memo[n];

    return memo[n] = tribo(n - 1) + tribo(n - 2) + tribo(n - 3);
}
int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    memo.assign(50, -1);
    tribo(49);
    
}
