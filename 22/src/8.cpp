#include "common.h"

#define  MAXSZ 11234

#define TOP 0
#define RIGHT 1
#define BOTTOM 2
#define LEFT 3

bool visi[MAXSZ][MAXSZ];

typedef struct {
    int height;
    int max[4];
    bool seen;
} Cell;

void initCell(Cell &c, char height) {
    int i_height = height - '0';

    c.height = i_height;
    c.max[TOP] = i_height;
    c.max[BOTTOM] = i_height;
    c.max[LEFT] = i_height;
    c.max[RIGHT] = i_height;

    c.seen = 0;
}

void initialize(vector<vector<Cell>> &data) {
    for (lui i = 1; i< data.size() - 1; i++) {
        for (lui j = 1; j< data[i].size() - 1; j++) {
            data[i][j].seen |= data[i][j].height > data[i-1][j].max[TOP];
            data[i][j].max[TOP] = max(data[i][j].height, data[i-1][j].max[TOP]);

            data[i][j].seen |= data[i][j].height > data[i][j-1].max[LEFT];
            data[i][j].max[LEFT] = max(data[i][j].height, data[i][j-1].max[LEFT]);
        }
    }

    for (lui i = data.size() - 2; i > 0; i--) {
        for (lui j = data[i].size() - 2; j > 0; j--) {
            data[i][j].seen |= data[i][j].height > data[i+1][j].max[BOTTOM];
            data[i][j].max[BOTTOM] = max(data[i][j].height, data[i+1][j].max[BOTTOM]);
            
            data[i][j].seen |= data[i][j].height > data[i][j+1].max[RIGHT];
            data[i][j].max[RIGHT] = max(data[i][j].height, data[i][j+1].max[RIGHT]);
        }
    }
}

void solve_v1(vector<vector<Cell>> &data) {
    int solution = data.size() * 2 + (data[0].size() - 2) * 2;
    for (lui i = 0; i< data.size(); i++) {
        for (lui j = 0; j< data[i].size(); j++) {
            if (data[i][j].seen) {
                solution++;
            }
        }
    }

    cout << "First answer: ";
    cout << solution << endl;
}

int getScore(int x, int y, vector<vector<Cell>> &data) {
    long long l = 0, r = 0, t = 0, b = 0;

    for (lui i = x; i-- > 0;) {
        l++;
        if (data[x][y].height <= data[i][y].height) {
            break;
        }
    }

    for (lui i = x+1; i < data[x].size(); i++) {
        r++;
        if (data[x][y].height <= data[i][y].height) {
            break;
        }
    }

    for (lui i = y; i-- > 0;) {
        t++;
        if (data[x][y].height <= data[x][i].height) {
            break;
        }
    }
    
    for (lui i = y+1; i < data[x].size(); i++) {
        b++;
        if (data[x][y].height <= data[x][i].height) {
            break;
        }
    }

    return l * r * t * b;
}

void solve_v2(vector<vector<Cell>> &data) {
    cout << "Second answer: ";
    int solution = -1;

    for (lui i = 1; i < data.size() - 1; i++) {
        for (lui j= 1; j < data[i].size() - 1; j++) {
            if (!data[i][j].seen) continue;

            solution = max(solution, getScore(i, j, data));
        }
    }

    cout << solution << endl;
}

vector<vector<Cell>> data;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string line;
    while (cin >> line) {
        vector<Cell> line_data;
        for (lui i = 0; i < line.length(); i++) {
            Cell c;
            initCell(c, line[i]);
            line_data.pb(c);
        }
        data.pb(line_data);
    }

    initialize(data);
    solve_v1(data);
    solve_v2(data);
    return 0;
}
