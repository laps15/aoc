#include<bits/stdc++.h> 

using namespace std;

/*
  X Y Z
A 4 8 3
B 1 5 9
C 7 2 6
*/
int pmap_v1[3][3] = {
    {4, 8, 3},
    {1, 5, 9},
    {7, 2, 6}
};


/*
  X Y Z
A 3 4 8
B 1 5 9
C 2 6 7
*/
int pmap_v2[3][3] = {
    {3, 4, 8},
    {1, 5, 9},
    {2, 6, 7}
};


void solve1(int solution) {
    cout << "First answer: ";
    cout << solution << endl;
}

void solve2(int solution) {
    cout << "Second answer: ";
    cout << solution << endl;
}

int main () {
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    char o, m;
    int total1 = 0, total2 = 0;

    while (cin >> o >> m) {
        int oi, mi;
        oi = o - 'A';
        mi = m - 'X';

        total1 += pmap_v1[oi][mi];
        total2 += pmap_v2[oi][mi];
    }

    solve1(total1);
    solve2(total2);
}