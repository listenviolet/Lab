#include <iostream>
#include <map>
#include <cstring>
using namespace std;

int main()
{
    map<char, int> sub;
    string str;
    while(cin >> str)
    {
        for(int i = 0; i < str.size();)
        {
            char key = str[i];
            int len = 0;
            for(int j = i; j < str.size(); ++j)
            {
                if(str[j] == key) len++;
                else break;
            }
            if(sub.count(key))
            {
                int curlen = sub[key];
                sub[key] = (curlen > len) ? curlen : len;
            }
            else
            {
                sub.insert(pair<char, int>(key, len));
            }

            i += len;
        }

        int sum = 0;
        map<char, int>::iterator iter;
        for(iter = sub.begin(); iter != sub.end(); iter++)
        {
            sum += iter->second;
        }
        cout << sum << endl;
    }
    return 0;
}
