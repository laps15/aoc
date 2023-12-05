#include<bits/stdc++.h> 

using namespace std;
using lui = long unsigned int;


int solve_v1(int int1[2], int int2[2], int total) {
    if ((int1[0] <= int2[0] && int1[1] >= int2[1]) || (int2[0] <= int1[0] && int2[1] >= int1[1])) {
        return total + 1;
    }
    
    return total;
}

int solve_v2(int int1[2], int int2[2], int total) {
    if (int1[0] <= int2[0] && int1[1] >= int2[0]) {
        return total + 1;
    }
    
    if (int1[0] <= int2[1] && int1[1] >= int2[1]) {
        return total + 1;
    }
    
    if (int2[0] <= int1[0] && int2[1] >= int1[0]) {
        return total + 1;
    }
    
    if (int2[0] <= int1[1] && int2[1] >= int1[0]) {
        return total + 1;
    }

    return total;
}

int main () {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    int total1 = 0, total2 = 0;
    
    int int1[2], int2[2];
    char dump;
    while ((cin >> int1[0] >> dump >> int1[1] >> dump >> int2[0] >> dump >> int2[1])) {
        total1 = solve_v1(int1, int2, total1);
        total2 = solve_v2(int1, int2, total2);
    }
    cout << "First answer: " << total1 << endl;
    cout << "Second answer: " << total2 << endl;
}