#include<bits/stdc++.h> 

using namespace std;

using lui = long unsigned int;

bool visi[3][300];

void process(string line, int j) {
    for (lui i = 0; i< line.length(); i++) {
        visi[j][(short)line[i]] = j ? visi[j-1][(short)line[i]] : true;
    }
}

int main () {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    int total = 0;
    
    string line[3];
    while (getline(cin, line[0]) && getline(cin, line[1]) && getline(cin, line[2])) {
        memset(visi, 0, sizeof visi);

        for (lui j = 0; j < 3; j++) {
            process(line[j], j);
        }

        for (lui i = 0; i< 'z'+1; i++) {
            if (visi[2][i]) {
                total += i > 'a' ? (i-'a' + 1) : (i-'A'+27);
            }
        }

    }
    cout << total << endl;
}