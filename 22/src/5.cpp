#include<bits/stdc++.h> 

using namespace std;

using lui = long unsigned int;
using li = long int;

vector<vector<char>> Stacks;
 
void parse_stacks_input() {
    vector<string> lines;
    string line;
    while (getline(cin, line) && line.length() > 0) {
        lines.push_back(line);
    }
 
    for (lui i= 1; i< lines[lines.size()-1].length(); i+= 4) {
        Stacks.push_back({});
    }
 
    for (int i= lines.size()-2; i>= 0; i--) {
        for (lui j= 1; j< lines[i].length(); j+= 4) {
            if (lines[i][j] != ' ') {
                Stacks[j/4].push_back(lines[i][j]);
            }
        }
    }
}


char getFromTop(stack<char> &S) {
    char tmp = S.top();
    S.pop();

    return tmp;
}

void printAllFromTop(vector<stack<char>> S) {
    for (lui i = 0; i < S.size(); i++) {
        cout << S[i].top();
    }
    cout << endl;
}

vector<stack<char>> S_v1, S_v2;
stack<char> Stmp;

void solve_v1() {
    cout << "First answer: ";
    printAllFromTop(S_v1);
}

void solve_v2() {
    cout << "Second answer: ";
    printAllFromTop(S_v2);
}

int main () {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    parse_stacks_input();

    string total = "";
    
    for (lui i = 0; i < Stacks.size(); i++) {
        S_v1.push_back({});
        S_v2.push_back({});
        for (lui j = 0; j< Stacks[i].size(); j++) {
            S_v1[i].push(Stacks[i][j]);
            S_v2[i].push(Stacks[i][j]);
        }
    }

    string dump;
    int amount, from, to;
    while (cin >> dump >> amount >> dump >> from >> dump >> to) {
        for (int i= 0; i< amount; i++) {
            char tmp_v1 = getFromTop(S_v1[from-1]);
            char tmp_v2 = getFromTop(S_v2[from-1]);

            S_v1[to-1].push(tmp_v1);

            Stmp.push(tmp_v2);
        }

        do {
            char tmp_v2 = getFromTop(Stmp);
            S_v2[to-1].push(tmp_v2);
        } while (!Stmp.empty());
    }

    solve_v1();
    solve_v2();
}