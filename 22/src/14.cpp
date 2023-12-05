#include "common.h"
#include <regex>

#define r_coordinate regex("\\b(\\d+),(\\d+)\\b")

#define ROCK '#'
#define FREE '.'
#define SAND 'O'

typedef p<lui> pii;

void setAllEmpty(vector<vector<char>> &m, pii msize) {
    for (lui i = 0; i< msize.fi; i++) {
        vector<char> row;
        for (lui j = 0; j< msize.se; j++) {
            row.pb((i == msize.fi-1) ? ROCK : FREE);
        }

        m.pb(row);
    }
}

void drawLine(vector<vector<char>> &m, pii start, pii end) {
    if (start.fi == end.fi) {
        int istart = min(start.se, end.se);
        int iend = max(start.se, end.se);

        for (int i= istart; i<= iend; i++) {
            m[start.fi][i] = ROCK;
        }

        return;
    }
    
    if (start.se == end.se) {
        int istart = min(start.fi, end.fi);
        int iend = max(start.fi, end.fi);

        for (int i= istart; i<= iend; i++) {
            m[i][start.se] = ROCK;
        }

        return;
    }

    throw "Diagonal line I don't know what to do :(";
}

void init(vector<vector<char>> &m, pii msize, vector<vector<pii>> &paths) {
    m.clear();

    setAllEmpty(m, msize);

    for (auto &p:paths) {
        pii start = p[0];
        for (lui i= 1; i< p.size(); i++) {
            pii end = p[i];

            drawLine(m, start, end);

            start = end;
        }
    }
}

void printMap(vector<vector<char>> &m, pii xlim, pii ylim) {
    for (lui i = 0; i < m.size(); i++) {
        if(i < xlim.fi || i > xlim.se) continue;

        for (lui j = 0; j< m[i].size(); j++) {
            if(j < ylim.fi || i > ylim.se) continue;
            cout << m[i][j];
        }
        cout << endl;
    }
    cout << endl;
}


void solve_v1(vector<vector<char>> m, pii source) {
    int solution = 0;
    bool map_changed;
    
    do {
        map_changed = false;
        pii current(source.fi, source.se);

        while (m[current.fi][current.se] == FREE) {
            if (current.fi+1 == m.size()-1) break;

            if (m[current.fi+1][current.se] == FREE) {
                current.fi++;
                continue;
            }
            if (m[current.fi+1][current.se-1] == FREE) {
                current.fi++;
                current.se--;
                continue;
            }
            if (m[current.fi+1][current.se+1] == FREE) {
                current.fi++;
                current.se++;
                continue;
            }

            m[current.fi][current.se] = SAND;
            map_changed = true;
        }

        solution += map_changed;
    } while (map_changed);
    // printMap(m, pii(0,11), pii(488, 504));

    cout << "First answer: ";
    cout << solution << endl;
}

void solve_v2(vector<vector<char>> m, pii source) {
    int solution = 0;
    bool map_changed;
    
    do {
        map_changed = false;
        pii current(source.fi, source.se);

        while (m[current.fi][current.se] == FREE) {
            if (m[current.fi+1][current.se] == FREE) {
                current.fi++;
                continue;
            }
            if (m[current.fi+1][current.se-1] == FREE) {
                current.fi++;
                current.se--;
                continue;
            }
            if (m[current.fi+1][current.se+1] == FREE) {
                current.fi++;
                current.se++;
                continue;
            }

            m[current.fi][current.se] = SAND;
            map_changed = true;
        }

        solution += map_changed;
        // printMap(m, pii(0,11), pii(493, 504));
    } while (map_changed);

    cout << "Second answer: ";
    cout << solution << endl;
}



vector<vector<pii>> paths;
vector<vector<char>> bitmap;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string line;
    pii max_dim(0,0);
    pii source(0, 500);
    smatch matches;

    while (getline(cin, line)) {
        vector<pii> obstacle;
        while (regex_search(line, matches, r_coordinate)) {
            pii c(stoull(matches[2]), stoull(matches[1]));
            obstacle.pb(c);
            max_dim.fi = max(max_dim.fi, c.fi);
            max_dim.se = max(max_dim.se, c.se); 

            line = matches.suffix().str();
        }
        paths.pb(obstacle);
    }

    // Max x is 500 + height, so we add a bit of padding
    max_dim.se = source.se + (max_dim.fi+2) + 3;
    max_dim.fi += 3;
    
    init(bitmap, max_dim, paths);

    solve_v1(bitmap, source);
    solve_v2(bitmap, source);
    return 0;
}
