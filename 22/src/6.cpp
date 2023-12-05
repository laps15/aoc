#include "common.h"

void solve_v1(lui solution) {
    cout << "First answer: ";

    cout << solution << endl;
}

void solve_v2(lui solution) {
    cout << "Second answer: ";

    cout << solution << endl;
}

lui getSolution(string line, int minLength) {
    for (lui i= minLength-1; i< line.length(); i++) {
        bool correct = true;
        for (int j = minLength-1; j>=0 && correct; j--) {
            for (int k = j-1; k>=0 && correct; k--) {
                correct &= line[i-j] != line[i-k];
            }
        }

        if (correct) {
            return i+1;
        }
    }

    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string line;
    while (cin >> line) {
        solve_v1(getSolution(line, 4));
        solve_v2(getSolution(line, 14));
    }

    return 0;
}
