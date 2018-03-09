#include <iostream>
#include <cstring>
using namespace std;

bool is_equal(char a, char b)
{
    if(a != '\0' && (b == '.' || a == b)) return true;
    else return false;
}

bool isMatch(string s, string p) {
    //cout << "s: " << s << "-- p : " << p << endl;

    if(s[0] == '\0' && p[0] == '\0') return true;

    int len1 = s.length(), len2 = p.length();
    int i = 0, j = 0;

    while(i < len1 && j < len2)
    {
        if(p[j + 1] != '*')
        {
            if(is_equal(s[i], p[j]) == true) {i++; j++; continue;}
            else return false;
        }

        else
        {
            int k = 0;
            while(is_equal(s[i + k],p[j])) k++;
            int t;
            for(t = 0; t <= k; ++t)
            {
                string sub_s = s.substr(i + t, len1 - i - t), sub_p = p.substr(j + 2, len2 - j - 2);
                if(isMatch(sub_s, sub_p) == false) continue;
                else return true;
            }
            return false;
        }
    }

    if(i == len1)
    {
        if(p[j] == '\0') return true;
        else
        {
            while(p[j + 1] == '*' && p[j] != '\0') j += 2;
            if(p[j] == '\0') return true;
            else return false;
        }
    }
    else return false;
}

int main()
{
    string s, p;
    while(cin >> s >> p)
    {
        bool flag = isMatch(s, p);
        cout << flag <<endl;
    }
    return 0;
}

/*
abbabaaaaaaacaa
a*.*b.a.*c*b*a*c*
*/
