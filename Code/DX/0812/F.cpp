#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep_(i, j, n) for (int i = j; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()

int INF = 987654321;
int MAX_CNT = INF;
string target;
vector<string> *strs_p;

void backtrack(string current_str, int cur_cnt){

    if(current_str == target){
        MAX_CNT = min(MAX_CNT, cur_cnt);
        return;

    } else if (target.rfind(current_str, 0) != 0) {
        return;
    }

    rep(i, strs_p->size()){
        backtrack(current_str + strs_p->at(i), cur_cnt+1);
    }

}


int solution(vector<string> strs, string t)
{
    int answer = 0;
    target = t;
    strs_p = &strs;

    rep(i, strs.size()){
        backtrack(strs.at(i), 1);
    }

    if(MAX_CNT != INF) return MAX_CNT;
    else return -1;

}