#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep_(i, j, n) for (int i = j; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()

double PI = acos(-1.0);

int solution(int x, int y, int r, int d, vector<vector<int> > target)
{
    int answer = 0;

    int mx, my;
    rep(i, target.size()){

        mx = target[i][0];
        my = target[i][1];

        if(hypot(mx, my) < r && abs((180/PI)*(atan2(my, mx) - atan2(y, x))) < d){
            answer++;
        }


    }


    return answer;
}