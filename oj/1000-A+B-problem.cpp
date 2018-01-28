#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

#define maxn 15

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
            cnt = (a[i] + b[i]) / 10;

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
            cnt = (a[i] + b[i]) / 10;
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

void minusAB(int* a, int len_a, int* b, int len_b)
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
        len_c = len_a;
        if(cnt) cout << "-";
        disArr(c,len_c);
    }
/*
    else if(len_a < len_b)
    {
        len_c = len_b;
        for(int k = len_a; k < len_b; ++k)
        {
            c[k] = 10 - cnt - b[k];
            cnt = 0;
        }
        cout << "-";
        disArr(c, len_c);
    }
*/
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
                cout << "-";
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
            //cout<<tmp[i];
        }
    }
    //cout <<endl;
    return tmp;
}

int main()
{
    char s1[maxn],s2[maxn];
    while(scanf("%s%s", s1,s2) != EOF)
    {
        //two positive int
        if(s1[0] != '-' && s2[0] != '-')
        {
            int len_a = strlen(s1);
            int len_b = strlen(s2);
            int *a, *b;
            a = transToInt(s1, len_a);
            b = transToInt(s2, len_b);
            add(a, len_a, b, len_b);
        }

        else if(s1[0] == '-' && s2[0] != '-')
        {
            int len_a = strlen(s2); //cout << len_a <<endl;
            int len_b = strlen(s1) - 1; //cout << len_b <<endl;
            int *a, *b;
            a = transToInt(s2, len_a);
            b = transToInt(s1, len_b + 1);
            minusAB(a, len_a, b, len_b);
        }

        else if(s1[0] != '-' && s2[0] == '-')
        {
            int len_a = strlen(s1)-1; //cout << len_a <<endl;
            int len_b = strlen(s2); //cout << len_b <<endl;
            int *a, *b;
            a = transToInt(s2, len_a + 1);
            b = transToInt(s1, len_b);
            if(len_a < len_b) minusAB(b, len_b, a, len_a);
            else minusAB(a, len_a, b, len_b);
        }

        else if(s1[0] == '-' && s2[0] == '-')
        {
            int len_a = strlen(s1)-1;
            int len_b = strlen(s2)-1;
            int *a, *b;
            a = transToInt(s2, len_a + 1);
            b = transToInt(s1, len_b + 1);
            cout<<"-";
            add(a, len_a, b, len_b);
        }

    }

    return 0;
}
