#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>

using namespace std;
const int N = 100 + 10;

#include<cmath>
struct Point {
    int x, y;
    Point() {}
    Point(int x, int y) : x(x), y(y) {}
    double angle(const Point& p) const {
        return atan2(y - p.y, x - p.x);
    }
    bool operator < (const Point &rhs) const {
        return y < rhs.y || (y == rhs.y && x < rhs.x);
    }
    void read() {
        scanf("%d%d", &x, &y);
    }
};

int n;
struct Node {
    Point p;
    int id;
    double ang;

    bool operator < (const Node &rhs) const {
        return ang < rhs.ang;
    }

    void getangle(const Point& p0) {
        ang = p.angle(p0);
    }

    int type() const {
        return id <= n ? 1 : -1;
    }
}p[N * 2];

int ans[N * 2];

void solve(int l, int r) {
    if(l > r) return;
    int pos = l;
    for(int i = l + 1; i <= r; i++) {
        if(p[i].p < p[pos].p) pos = i;
    }
    swap(p[pos], p[l]);
    int cnt = p[l].type();
    for(int i = l + 1; i <= r; i++) {
        p[i].getangle(p[l].p);
    }
    sort(p + l + 1, p + r + 1);
    for(int i = l + 1; i <= r; i++) {
        cnt += p[i].type();
        if(!cnt) {
            ans[p[l].id] = p[i].id;
            ans[p[i].id] = p[l].id;
            solve(l + 1, i - 1);
            solve(i + 1, r);
            return;
        }
    }
}

int main() {
    while(scanf("%d", &n) == 1) {
        for(int i = 1; i <= (n << 1); i++) {
            p[i].p.read();
            p[i].id = i;
        }

        solve(1, n << 1);
        for(int i = 1; i <= n; i++) {
            printf("%d\n", ans[i] - n);
        }
    }

    return 0;
}

