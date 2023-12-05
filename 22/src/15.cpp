#include "common.h"
#include <cstdlib>

#define r_coordinate regex("x=(-?\\d+), y=(-?\\d+):.+x=(-?\\d+), y=(-?\\d+)")

#define TARGET_ROW 2000000
#define MAX_SIZE 4000000
// #define TARGET_ROW 10
// #define MAX_SIZE 20

typedef long long int lli;
typedef p<lli> pii;

lli getDist(pii a, pii b) {
    return abs(a.fi-b.fi) + abs(a.se-b.se);
}

bool compareRange(pii a, pii b) {
    return (a.fi == b.fi) ? (a.se < b.se) : (a.fi < b.fi);
}

bool mergeTwoRanges(pii &a, pii b) {
    if (a.se + 1 == b.fi) {
        a.se = b.se;
        return true;
    }
    if (b.se + 1 == a.fi) {
        a.fi = b.fi;
        return true;
    }

    if (b.fi < a.fi && b.se >= a.fi && b.se <= a.se) {
        a.fi = b.fi;
        return true;
    }
    
    if (b.se > a.se && b.fi <= a.se && b.fi >= a.fi) {
        a.se = b.se;
        return true;
    }
    
    if (b.fi <= a.fi && b.se >= a.se) {
        a = b;
        return true;
    }
    
    if (a.fi <= b.fi && a.se >= b.se) {
        return true;
    }

    return false;
}

void addReachRange(vector<pii> &reach, pii range) {
    bool consumed = false;
    for (lui i = 0; i < reach.size(); i++) {
        consumed = mergeTwoRanges(reach[i], range);
    }

    if (!consumed)
        reach.pb(range);
}

vector<pii> unifyReachRanges(vector<pii> &reach) {
    vector<pii> result;
    pii range = reach[0];

    for (lui i = 1; i< reach.size(); i++) {
        if (!mergeTwoRanges(range, reach[i])) {
            result.pb(range);
            range = reach[i];
        }
    }
    result.pb(range);

    return result;
}

vector<pii> getReach(vector<pii> &sensors, vector<pii> &beacons, int row) {
    vector<pii> reach;
    for (lui i = 0; i < sensors.size(); i++) {
        lli range = getDist(sensors[i], beacons[i]);
        lli distY = getDist(sensors[i], pii(sensors[i].fi, row));
        
        lli delta = range - distY;
        if (delta < 0) {
            continue;
        }

        addReachRange(reach, pii(sensors[i].fi-delta, sensors[i].fi+delta));
    }

    return unifyReachRanges(reach);
}

void solve_v1(vector<pii> &sensors, vector<pii> &beacons, int target) {
    unordered_map<lli,bool> beaconsOnTarget;

    for (auto &beacon:beacons) {
        if (beacon.se == target)
            beaconsOnTarget[beacon.fi] = true;
    }

    vector<pii> reach = getReach(sensors, beacons, target);

    lli solution = 0;
    for (auto &range:reach) {
        solution += range.se - range.fi + 1;
    }

    cout << "First answer: ";
    cout <<  solution - beaconsOnTarget.size() << endl;
}

lli getGap(vector<pii> &ranges) {
    pii range = ranges[0];
    for (lui i = 1; i < ranges.size(); i++) {
        if (!mergeTwoRanges(range, ranges[i])) {
            return ranges[i].fi - 1;
        }
    }

    return -1;
}

void solve_v2(vector<pii> &sensors, vector<pii> &beacons) {
    lli solution = -1;

    for (lli row = 0; row <= MAX_SIZE; row++) {
        vector<pii> reach = getReach(sensors, beacons, row);

        lli result_x = getGap(reach);
        if (result_x != -1) {
            solution = result_x * MAX_SIZE + row;
            break;
        }
    }

    cout << "Second answer: ";
    cout << solution << endl;
}

vector<pii> sensors;
vector<pii> beacons;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string line;
    smatch matches;
    while (getline(cin, line)) {
        regex_search(line, matches, r_coordinate);
        pii sensor(stoi(matches[1]), stoi(matches[2])), beacon(stoi(matches[3]), stoi(matches[4]));
        sensors.pb(sensor);
        beacons.pb(beacon);
    }

    solve_v1(sensors, beacons, TARGET_ROW);
    solve_v2(sensors, beacons);
    return 0;
}
