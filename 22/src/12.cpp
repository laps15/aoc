#include "common.h"

typedef struct {
    char height;
    int steps;
} Cell;

void reset_steps(vector<vector<Cell>> &G) {
    for (auto &row:G) {
        for (auto &cell:row) {
            cell.steps = inf;
        }
    }
}

p<int> getNeighbour(vector<vector<Cell>> &G, p<int> pos, int neighbours_index) {
    p<int> deltas[] = {
        p<int>(-1,0),
        p<int>(0,-1),
        p<int>(0,1),
        p<int>(1,0),
    };

    int dx = deltas[neighbours_index].fi;
    int x = pos.fi + dx;
    x = max(0, x);
    x = min((int) G.size()-1, x);

    int dy = deltas[neighbours_index].se;
    int y = pos.se + dy;
    y = max(0, y);
    y = min((int) G[x].size()-1, y);
    
    return p<int>(x,y);
}

void bfs(vector<vector<Cell>> &G, p<int> pos) {
    pair<p<int>, int> current;
    queue<pair<p<int>, int>> Q;
    Q.push(pair<p<int>, int>(pos, 0));
    int steps = 0;

    do {
        current = Q.front();
        Q.pop();

        pos = current.fi;
        steps = current.se;

        if (G[pos.fi][pos.se].steps <= steps) continue;

        G[pos.fi][pos.se].steps = steps;

        for (int neighbour_index = 0; neighbour_index < 4; neighbour_index++) {
            p<int> neighbour = getNeighbour(G, pos, neighbour_index);

            if (G[neighbour.fi][neighbour.se].steps <= steps) continue;
            if (neighbour == pos) continue;

            if (G[pos.fi][pos.se].height + 1 >= G[neighbour.fi][neighbour.se].height) {
                Q.push(pair<p<int>, int>(neighbour, steps+1));
            }
        }
    } while (!Q.empty());
}

void printG(vector<vector<Cell>> &G) {
    for (lui i= 0; i < G.size(); i++) {
        for (lui j= 0; j< G[i].size(); j++) {
            printf("%4d", G[i][j].steps);
        }
        printf("\n");
    }
    printf("\n");
}

void solve_v1(vector<vector<Cell>> &G, p<int> pos, p<int> target) {
    reset_steps(G);
    bfs(G, pos);
    
    cout << "First answer: ";
    cout << G[target.fi][target.se].steps << endl;
}

void solve_v2(vector<vector<Cell>> &G, vector<p<int>> poses, p<int> target) {
    int solution = inf;
    for (auto pos: poses) {
        reset_steps(G);

        bfs(G, pos);
        solution = min(solution, G[target.fi][target.se].steps == -1 ? solution : G[target.fi][target.se].steps);
    }
    
    cout << "Second answer: ";
    cout << solution << endl;
}

vector<vector<Cell>> G;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string line;
    vector<string> data;
    p<int> starting_cell, target;
    vector<p<int>> starting_cells;

    while (cin >> line) {
        vector<Cell> L;
        for (auto c:line) {
            Cell cell;
            cell.height = c;

            if (cell.height == 'S') {
                cell.height = 'a';
                starting_cell = p<int>(G.size(), L.size());
            }

            if (cell.height == 'a') {
                starting_cells.pb(p<int>(G.size(), L.size()));
            }

            if (cell.height == 'E') {
                cell.height = 'z';
                target = p<int>(G.size(), L.size());
            }

            L.pb(cell);
        }
        G.pb(L);
    }

    solve_v1(G, starting_cell, target);
    solve_v2(G, starting_cells, target);
    return 0;
}
