#include "common.h"
#include <regex>

#define r_card regex("Card\\W+\\d+:\\W+((\\d+\\W*)+)\\W\\|\\W((\\d+\\W*)+)")
#define r_number regex("(\\d+)")

struct card {
    int number;
    vector<int> win;
    vector<int> have;
};

void solve_v1(vector<card> data) {
    cout << "First answer: ";
    int solution = 0;

    for (auto c: data) {
        int hits = 0;
        for (auto w:c.win) {
            for (auto h:c.have) {
                if (w == h) {
                    hits++;
                }
            }
        }

        solution += hits ? 1<<(hits-1) : 0;
    }

    cout << solution << endl;
}

void solve_v2() {
    cout << "Second answer: ";
    int solution = -1;
    cout << solution << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<card> data;


    string line;
    while (getline(cin, line)) {
        card C;
        smatch matches;
        regex_search(line, matches, r_card);
        auto winners = string(matches[1]);
        auto have = string(matches[3]);
        cout << winners << endl << have << endl;

        smatch matches2;
        while (regex_search(winners, matches2, r_number)) {
            C.win.pb(stoi(matches2[0]));
            winners = matches2.suffix().str();
        }

        smatch matches3;
        while (regex_search(have, matches3, r_number)) {
            C.have.pb(stoi(matches3[0]));
            have = matches3.suffix().str();
        }

        data.pb(C);
    }

    cout << "Finished reading\n";

    // for (auto c:data) {
    //     printf("Card %d: %d %d %d %d %d | %d %d %d %d %d %d %d %d\n", c.number, c.win[0], c.win[1], c.win[2], c.win[3], c.win[4], c.have[0], c.have[1], c.have[2], c.have[3], c.have[4], c.have[5], c.have[6], c.have[7]);
    // }

    solve_v1(data);
    solve_v2();
    return 0;
}
