#include "common.h"
#include <regex>

#define r_gamenumber regex("Game\\W(\\d+): (.*)")
#define r_iteration regex("\\b(\\d+),(\\d+)\\b")

void solve_v1() {
    cout << "First answer: ";

    cout << solution << endl;
}

void solve_v2() {
    cout << "Second answer: ";

    cout << solution << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while (cin >> dump >> amount >> dump >> from >> dump >> to) {
    }

    solve_v1();
    solve_v2();
    return 0;
}
