#include "common.h"

#define DISPLAY_MAX_LINES 6
#define DISPLAY_MAX_COLS 40

#define between_inclusive(x, a, b) ((x) >= a && (x) <= (b))
#define vector2row(i) ((i)/DISPLAY_MAX_COLS)
#define vector2col(i) ((i)%DISPLAY_MAX_COLS)

int targets_v1[] = {20, 60, 100, 140, 180, 220};

bool display[DISPLAY_MAX_LINES][DISPLAY_MAX_COLS];

typedef struct {
    string name;
    int value;
} Instruction;

int getInstructionClockCount(Instruction i) {
    if (i.name == "addx")
        return 2;
    return 1;
}

void solve_v1(vector<Instruction> data) {
    int x = 1, clock_count = 1, next_clock = 0, solution = 0;

    for (auto ins: data) {
        next_clock = clock_count + getInstructionClockCount(ins);
        for (auto t: targets_v1) {
            if (t >= clock_count && t < next_clock) {
                solution += t * x;
            }
        }
        clock_count = next_clock;
        x += ins.value;
    }

    cout << "First answer: ";
    cout << solution << endl;
}

void solve_v2(vector<Instruction> data) {
    mset(display, 0);
    int x = 1, clock_count = 1, next_clock = 0;

    for (auto ins: data) {
        next_clock = clock_count + getInstructionClockCount(ins);
        for (int i= clock_count; i< next_clock; i++) {
            display[vector2row(i-1)][vector2col(i-1)] = between_inclusive(vector2col(i-1), x-1, x+1); 
        }

        clock_count = next_clock;
        x += ins.value;
    }

    cout << "Second answer: " << endl;
    for (lui i = 0; i< DISPLAY_MAX_LINES; i++) {
        for (lui j= 0; j< DISPLAY_MAX_COLS; j++) {
            cout << (display[i][j] ? '#' : ' ');
        }
        cout << endl;
    }
}

vector<Instruction> data;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string instruction;
    while (cin >> instruction) {
        Instruction i;
        i.name = instruction;
        i.value = 0;
        if (instruction != "noop") {
            cin >> i.value;
        }

        data.pb(i);
    }

    solve_v1(data);
    solve_v2(data);
    return 0;
}
