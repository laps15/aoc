#include "common.h"

enum Type {List, Numeric};

typedef struct Package {
    Type type;
    int numeric_value;
    vector<Package*> list_value;
} Package;

Package *getNumeric(string number) {
    Package *new_package = new Package();
    new_package->type = Numeric;
    new_package->numeric_value = stoi(number);

    return new_package;
}

Package *parseData(string data) {
    Package *result = NULL;
    stack<Package*> S;
    string number;

    for (lui idx = 0; idx < data.length(); idx++) {
        if (data[idx] == '[') {
            Package *new_package = new Package();
            S.push(result);
            if (result != NULL) {
                result->type = List;
                result->list_value.pb(new_package);
            }
            result = new_package;
            continue;
        }
        if (data[idx] == ',') {
            if (!number.empty()) {
                result->list_value.pb(getNumeric(number));
                number.clear();
            }
            continue;
        }
        if (data[idx] == ']') {
            if (!number.empty()) {
                result->list_value.pb(getNumeric(number));
                number.clear();
            }
            if (S.top() != NULL)
                result = S.top();
            S.pop();
            continue;
        }

        number += data[idx];
    }

    return result;
}

void printPackage(Package *p, bool isRoot = true) {
    if (p->type == Numeric) {
        cout << p->numeric_value;
        return;
    }

    cout << '[';
    for (lui i = 0; i< p->list_value.size(); i++) {
        printPackage(p->list_value[i], false);
        if (i < p->list_value.size()-1) {
            cout << ", ";
        }
    }
    cout << "]";

    isRoot && cout << endl;
}

short compare(Package* a, Package* b) {
    if (a->type != b->type) {
        Package *np = new Package();
        np->type = List;

        if (a->type == Numeric) {
            np->list_value.pb(a);
            return compare(np, b);
        }

        np->list_value.pb(b);
        return compare(a, np);
    }

    if (a->type == List) {
        lui size = min(a->list_value.size(), b->list_value.size());

        for (lui i = 0; i< size; i++) {
            short result = compare(a->list_value[i], b->list_value[i]);
            
            if (!result) continue;

            return result;
        }

        if (a->list_value.size() == b->list_value.size()) {
            return 0;
        }

        return ((int)a->list_value.size() - (int)b->list_value.size()) / abs((int)a->list_value.size() - (int)b->list_value.size());
    }

    if (a->numeric_value == b->numeric_value) {
        return 0;
    }

    return (a->numeric_value - b->numeric_value) / abs(a->numeric_value - b->numeric_value);

}

void solve_v1(vector<Package*> &data) {
    int solution = 0;

    for (lui i = 0; i< data.size(); i+= 2) {
        Package *left = data[i], *right = data[i+1];

        if (compare(left, right) == -1) {
            solution += i/2 + 1;
        }
    }

    cout << "First answer: ";
    cout << solution << endl;
}

bool compareForSort(Package* a, Package* b) {
    return compare(a, b) < 0;
}

void solve_v2(vector<Package*> data, Package* a, Package* b) {
    sort(all(data), compareForSort);

    int solution = 1;
    for (lui i = 0; i< data.size(); i++) {
        if (data[i] == a || data[i] == b)
            solution *= i+1;
    }

    cout << "Second answer: ";
    cout << solution << endl;
}

void cleanUp(vector<Package*> &data) {
    for (auto p:data) {
        delete p;
    }
    data.clear();
}

vector<Package*> data;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string left_line, right_line;
    Package *left, *right;
    while (cin >> left_line) {
        cin >> right_line;

        left = parseData(left_line);
        right = parseData(right_line);

        data.pb(left);
        data.pb(right);
    }

    solve_v1(data);

    Package *p1 = parseData("[[2]]");
    Package *p2 = parseData("[[6]]");
    data.pb(p1);
    data.pb(p2);
    solve_v2(data, p1, p2);

    cleanUp(data);
    return 0;
}
