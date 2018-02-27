#include <iostream>
#include <cstring>
using namespace std;

const int maxn = 1000;
int lch[maxn], rch[maxn];
char op[maxn];
int nc = 0;

int build_tree(string s, int x, int y)
{
    int c1 = -1, c2 = -1;
    int p = 0;
    int u;
    if(y - x == 1)
    {
        u = ++nc;
        lch[x] = rch[x] = 0;
        op[u] = s[x];
        return u;
    }

    for(int i = x; i < y; ++i)
    {
        switch(s[i])
        {
            case '(' : p++; break;
            case ')' : p--; break;
            case '+' : case '-' : if(!p) c1 = i; break;
            case '*' : case '/' : if(!p) c2 = i; break;
        }
    }

    if(c1 < 0) c1 = c2;
    if(c1 < 0) return build_tree(s, x + 1, y - 1);
    u = ++nc;
    lch[u] = build_tree(s, x, c1);
    rch[u] = build_tree(s, c1 + 1, y);
    op[u] = s[c1];
    return u;
}

void display(int root)
{
    if(root) cout << op[root] << endl;
    if(lch[root]) display(lch[root]);
    if(rch[root]) display(rch[root]);
}

int main()
{
    string str;
    cin >> str;
    int root = build_tree(str, 0, str.size());
    display(root);
    for(int i = 1; i <= str.size(); ++i)
    {
        cout << op[i] << " ";
    }
    cout << endl;
    return 0;
}