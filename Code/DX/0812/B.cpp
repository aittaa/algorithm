#include <string>
#include <vector>

using namespace std;

#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep_(i, j, n) for (int i = j; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()


int solution(vector<int> paper) {
    int answer = 0;

    sort(rall(paper));

    int sum = 0;
    rep(i, paper.size()){
        sum += paper.at(i);
        int temp = (i+1)*(i+1);
        if(sum >= temp && temp > answer)
            answer = i+1;

    }


    return answer;
}