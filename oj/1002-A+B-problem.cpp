#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

#define maxn 22

void disArr(int* c, int len_c)
{
    for(int i = len_c - 1; i >=0; --i)
        cout << c[i];
    cout <<endl;
}

void add(int* a, int len_a, int* b, int len_b)
{
    int c[maxn], len_c;
    memset(c, 0, sizeof(c));
    if(len_a <= len_b)
    {
        int cnt = 0;
        for(int i = 0; i < len_a; ++i)
        {
            c[i] = (a[i] + b[i] + cnt)%10;
            cnt = (a[i] + b[i] + cnt) / 10;

        }
        for(int i = len_a; i < len_b; ++i)
        {
            c[i] = (b[i] + cnt) % 10;
            cnt = (b[i] + cnt) / 10;
        }
        if(cnt) c[len_b] = cnt;
        len_c = len_b + cnt;
    }

    else if(len_a > len_b)
    {
        int cnt = 0;
        for(int i = 0; i < len_b; ++i)
        {
            c[i] = (a[i] + b[i] + cnt)%10;
            cnt = (a[i] + b[i] + cnt) / 10;
        }

        for(int i = len_b; i < len_a; ++i)
        {
            c[i] = (a[i] + cnt) % 10;
            cnt = (a[i] + cnt) / 10;
        }

        if(cnt) c[len_a] = cnt;
        len_c = len_a + cnt;
    }
    for(int i = len_c - 1; i >= 0; --i)
    {
        cout<<c[i];
    }
    cout<<endl;
}

void minusAB(int* a, int len_a, int* b, int len_b)  //big - small
{
    int i = 0, j = 0, cnt = 0,len_c = 0;
    int c[maxn];
    memset(c, 0, sizeof(c));

    while(i < len_a && j < len_b)
    {
        int tmp = a[i] - b[i] - cnt;
        c[i] = (tmp + 10) % 10;
        cnt = tmp < 0 ? 1 : 0;
        i++;
        j++;
    }

    if(len_a == len_b)
    {
        int k = 0; len_c = len_a;
        while(c[len_a - 1 - k] == 0)
        {
            len_c--;
            k++;
        }
        if(cnt) cout << "-";
        disArr(c,len_c);
    }

    else if(len_a > len_b)
    {
        if(len_a > len_b + 1)
        {
            len_c = len_a;
            for(int k = len_b; k < len_a; ++k)
            {
                c[k] = a[k] - cnt;
                cnt = 0;
            }
            disArr(c, len_c);
        }
        else if(len_a == len_b + 1)
        {
            c[len_b] = a[len_b] - cnt;
            if(c[len_b] == 0)
            {
                len_c = len_b;
            }
            else len_c = len_a;
            disArr(c, len_c);
        }
    }
}

int* transToInt(char* s, int len)
{
    int *tmp;
    tmp = new int [maxn];
    if(s[0] == '-')
    {
        for(int i = 0; i < len - 1; ++i)
        {
            tmp[len - 2 - i] = s[i + 1] - '0';
        }
    }
    else if(s[0] != '-')
    {
        for(int i = 0; i < len; ++i)
        {
            tmp[i] = s[len - i - 1] - '0';
        }
    }
    return tmp;
}

int cmp(int* a, int len_a, int* b, int len_b)
{
    int flag = 0;
    if(len_a > len_b) return 1; //a > b
    else if(len_a < len_b) return -1; // a < b
    else if(len_a == len_b)
    {
        for(int i = len_a; i >= 0 ; --i)
        {
            if(a[i] > b[i]) return flag = 1;
            else if(a[i] < b[i]) return flag = -1;
        }
        if(flag == 0) return 0; //a = b
    }
}

int main()
{
    char s1[maxn],s2[maxn];
    while(scanf("%s%s", s1,s2) != EOF)
    {
        int len_a , len_b;
        int *a, *b;
        len_a = (s1[0] == '-') ? strlen(s1) - 1 : strlen(s1);
        len_b = (s2[0] == '-') ? strlen(s2) - 1 : strlen(s2);
        a = transToInt(s1, strlen(s1));
        b = transToInt(s2, strlen(s2));
        int flag = cmp(a, len_a, b, len_b);
        if(flag == 0) {cout << "0" <<endl;}
        else if(s1[0] != '-' && s2[0] != '-')
        {
            add(a, len_a, b, len_b);
        }
        else if(s1[0] != '-' && s2[0] =='-')
        {
            if(flag == 1) { minusAB(a, len_a, b, len_b);}
            //else if(flag == 0) {cout << "0" <<endl;}
            else if(flag == -1) {cout << "-"; minusAB(b, len_b, a, len_a);}
        }
        else if(s1[0] == '-' && s2[0] != '-')
        {
            if(flag == 1) {cout << "-"; minusAB(a, len_a, b, len_b);}
            else if(flag == -1)  {minusAB(b, len_b, a, len_a);}
        }
        else if(s1[0] == '-' && s2[0] == '-')
        {
            cout << "-";
            add(a, len_a, b, len_b);
        }
    }
    return 0;
}
