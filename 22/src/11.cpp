#include "common.h"
#include <regex>

#define r_number regex("\\b(\\d+)\\b")
#define r_operation regex("(old|\\d+) (\\+|\\*) (old|\\d+)")

#define MAX_ROUNDS_V1 20
#define MAX_ROUNDS_V2 10000

using llu = long long unsigned;

typedef struct {
    string first_element;
    char operation;
    string second_element;
} Operation;

typedef struct {
    int id;
    vector<llu> items;
    Operation operation;
    int test;
    int throw_to[2];
    llu inspected_items;
} Monkey;

Monkey readMonkey(string first_line) {
    Monkey m;
    smatch matches;
    string line;

    regex_search(first_line, matches, r_number);
    m.id = stoi(matches[0]);

    getline(cin, line);
    while (regex_search(line, matches, r_number)) {
        m.items.pb(stoull(matches[0]));
        line = matches.suffix().str();
    }
    
    getline(cin, line);
    regex_search(line, matches, r_operation);
    m.operation.first_element = matches[1];
    m.operation.operation = matches[2].str()[0];
    m.operation.second_element = matches[3];

    getline(cin, line);
    regex_search(line, matches, r_number);
    m.test = stoi(matches[0]);

    getline(cin, line);
    regex_search(line, matches, r_number);
    m.throw_to[true] = stoi(matches[0]);

    getline(cin, line);
    regex_search(line, matches, r_number);
    m.throw_to[false] = stoi(matches[0]);

    getline(cin, line);

    m.inspected_items = 0;
    return m;
}

llu getLimiter(vector<Monkey> data) {
    llu result= 1;

    for (auto monkey: data) {
        result *= monkey.test;
    }

    return result;
}

llu getWorryLevel_v2(llu worryLevel, llu mod, Monkey m) {
    llu a,b;

    a = b = worryLevel;
    if (m.operation.first_element != "old")
        a = stoull(m.operation.first_element);

    if (m.operation.second_element != "old")
        b = stoull(m.operation.second_element);

    if (m.operation.operation == '*')
        return ((a * b) % mod);
    
    return ((a + b) % mod);
}

llu getWorryLevel_v1(llu worryLevel, llu mod, Monkey m) {
    return getWorryLevel_v2(worryLevel, mod, m) / 3;
}


bool compareMonkey(Monkey a, Monkey b) {
    return a.inspected_items < b.inspected_items;
}

void solve(vector<Monkey> data, llu mod, int rounds, llu (*worryLevelHandler)(llu, llu, Monkey)) {
    for (int i= 0; i< rounds; i++) {
        for (auto &monkey:data) {
            for (auto worryLevel:monkey.items) {
                llu newWorryLevel = worryLevelHandler(worryLevel, mod, monkey);
                monkey.inspected_items++;

                Monkey next_monkey = data[monkey.throw_to[(newWorryLevel % monkey.test) == 0]];

                data[monkey.throw_to[(newWorryLevel % monkey.test) == 0]].items.pb(newWorryLevel);
            }

            monkey.items.clear();
        }
    }

    sort(rall(data), compareMonkey);
    cout << data[0].inspected_items * data[1].inspected_items << endl;
}

void solve_v1(vector<Monkey> data, llu mod) {
    cout << "First answer: ";
    solve(data, mod, MAX_ROUNDS_V1, getWorryLevel_v1);
}

void solve_v2(vector<Monkey> data, llu mod) {
    cout << "Second answer: ";
    solve(data, mod, MAX_ROUNDS_V2, getWorryLevel_v2);
    // sort(rall(data), compareMonkey);
    // cout << data[0].inspected_items * data[1].inspected_items << endl;
}


vector<Monkey> data;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string line;
    while (getline(cin, line)) {
        data.pb(readMonkey(line));
    }

    solve_v1(data, getLimiter(data));
    solve_v2(data, getLimiter(data));
    return 0;
}
