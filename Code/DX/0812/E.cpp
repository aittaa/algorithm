#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep_(i, j, n) for (int i = j; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()

double PI = acos(-1.0);

int solution(vector<vector<int>> monsters, vector<vector<int>> bullets) {
    int answer = 0;

    vector<double> m_atv;
    vector<double> b_atv;

    for(int i = 0; i < monsters.size(); i++){
        m_atv.push_back(atan2(monsters[i][1], monsters[i][0]));
    }
    for(int i = 0; i < bullets.size(); i++){
        b_atv.push_back(atan2(bullets[i][1], bullets[i][0]));
    }

    sort(all(m_atv));
    sort(all(b_atv));

    int m_cnt = 0, b_cnt = 0;
    while(b_cnt < bullets.size()){

        while(m_cnt < monsters.size() && m_atv.at(m_cnt) < b_atv.at(b_cnt))
            ++m_cnt;

        if(m_cnt == monsters.size()) break;

        if (m_atv.at(m_cnt) == b_atv.at(b_cnt)){
            answer++;
            m_cnt++;
        }

        ++b_cnt;
    }

    if(answer) return answer;
    else return -1;
}