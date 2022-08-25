#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep_(i, j, n) for (int i = j; i < (int)(n); i++)
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()


using namespace std;

string solution(string a, string b) {

    reverse(all(a));
    reverse(all(b));

    vector<int> result;

    int carry = 0, val = 0;
    rep(i, max(a.size(), b.size())){
        val = carry;

        if (i < a.size())
            val += a.at(i) - '0';

        if (i < b.size())
            val += b.at(i) - '0';

        result.push_back(val % 10);

        carry = (val/10) ? 1 : 0;

    }

    if(carry == 1) result.push_back(carry);

    reverse(all(result));
    std::stringstream ss;
    for(int e : result)
        ss << e;

    return ss.str();
}
