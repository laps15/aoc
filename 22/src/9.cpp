#include "common.h"

typedef p<int> ii;

#define UP 'U'
#define RIGHT 'R'
#define DOWN 'D'
#define LEFT 'L'

const ii MOVE_U(1,0);
const ii MOVE_R(0,1);
const ii MOVE_D(-1,0);
const ii MOVE_L(0,-1);

void solve_v1(int solution) {
    cout << "First answer: ";

    cout << solution << endl;
}

void solve_v2(int solution) {
    cout << "Second answer: ";

    cout << solution << endl;
}

unordered_map<string, bool> visited_v1;
unordered_map<string, bool> visited_v2;

ii getHeadExpectedMove(char dir) {
    if (dir == UP) {
        return MOVE_U;
    }
    if (dir == RIGHT) {
        return MOVE_R;
    }
    if (dir == DOWN) {
        return MOVE_D;
    }
    return MOVE_L;
}

void applyMove(ii &position, ii move) {
    position.fi += move.fi;
    position.se += move.se;
}

int getDiffFromHead(int d) {
    if (abs(d) == 2)
        return d/2;

    return 0;
}

int getDiff(int d) {
    if (abs(d) == 2)
        return d/2;

    return d;
}

ii getTailExpectedMove(ii &h, ii &t) {
    ii delta;
    delta.fi = getDiffFromHead(h.fi - t.fi);
    delta.se = getDiffFromHead(h.se - t.se);

    if (delta.fi && h.se != t.se)
        delta.se = getDiff(h.se - t.se);
    else if (delta.se && h.fi != t.fi)
        delta.fi = getDiff(h.fi - t.fi);

    return delta;
}

bool move_v1(ii &h, ii &t, char dir) {
    applyMove(h, getHeadExpectedMove(dir));
    applyMove(t, getTailExpectedMove(h, t));

    string tail_position = to_string(t.fi) + "." + to_string(t.se);
    if (visited_v1.find(tail_position) == visited_v1.end()) {
        visited_v1[tail_position] = true;

        return true;
    }

    return false;
}


bool move_v2(vector<ii> &rope, char dir, bool debug) {
    applyMove(rope[0], getHeadExpectedMove(dir));

    lui t = 0;
    for (lui h = 0; h < rope.size() - 1; h++) {
        t = h + 1;

        applyMove(rope[t], getTailExpectedMove(rope[h], rope[t]));
        debug && cout << "#" << h << " pos: " << to_string(rope[h].fi) + "." + to_string(rope[h].se) << endl;
    }
    
    string tail_position = to_string(rope[t].fi) + "." + to_string(rope[t].se);
    debug && cout << "#" << t << " pos: " << to_string(rope[t].fi) + "." + to_string(rope[t].se) << endl;
    if (visited_v2.find(tail_position) == visited_v2.end()) {
        return visited_v2[tail_position] = true;
    }

    return false;
}

void printRope(vector<ii> rope) {
    for (lui h = 0; h < rope.size(); h++) {
        cout << "#" << h << " pos: " << to_string(rope[h].fi) + "." + to_string(rope[h].se) << endl;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    char dir;
    int steps;
    ii head, tail;
    int ans_v1 = 1;
    visited_v1["0.0"] = true;
    head.fi = head.se = tail.fi = tail.se =  0;

    vector<ii> rope(10);
    int ans_v2 = 1;
    visited_v2["0.0"] = true;

    while (cin >> dir >> steps) {
        while (steps--) {
            move_v1(head, tail, dir) && ans_v1++;

            move_v2(rope, dir, false) && ans_v2++;
        }
    }

    solve_v1(ans_v1);
    solve_v2(ans_v2);
    return 0;
}
