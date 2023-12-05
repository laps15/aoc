#include<bits/stdc++.h> 

using namespace std;
using lui = long unsigned int;

void printsstr(string s) {
    for (lui i = 0; i < s.length(); i++) {
        cout << s[i] - 'a' << endl;
    }
}

vector<long long> v;

void solve1() {
    cout << "First answer: ";
    cout << v[v.size()-1] << endl;
}

void solve2() {
    cout << "Second answer: ";
    cout << v[v.size()-1] + v[v.size()-2] + v[v.size()-3] << endl;
}

int main () {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    string line;
    long long sum = 0;
    
    while (getline(cin, line)) {

        // cout << "empty: " << line.empty() << " line: " << line << " sum: " << sum << " maxCal: " << maxCal << endl;
        if (line.empty()) {
            v.push_back(sum);
            sum = 0;
            continue;
        }

        sum += stoi(line);
    };

    sort(v.begin(), v.end());

    solve1();
    solve2();
}