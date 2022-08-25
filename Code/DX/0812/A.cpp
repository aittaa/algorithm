#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep_(i, j, n) for (int i = j; i < (int)(n); i++)
#define all(v) v.begin(), v.end()

using namespace std;

bool check[26];

string solution(string sentence) {

    vector<char> alphabets;

    rep(i, sentence.size())
        if(isalpha(sentence.at(i)))
            alphabets.push_back(tolower(sentence.at(i)));

    for(auto c : alphabets)
        check[c - 'a'] = true;

    vector<char> result;
    for(int i = 0; i < 26; i++)
        if(check[i] == 0) 
            result.push_back('a' + i);


    if(result.size() != 0)
        return string(all(result));
    else
        return "perfect";

}