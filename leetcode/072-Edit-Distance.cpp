#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
#define maxn 1010
int d[maxn][maxn];
int main()
{
    string word1, word2;
    while(cin >> word1 >> word2)
    {
        char c = '#';
        word1 = c + word1;
        word2 = c + word2;
        for(int i = 1; i < word1.size(); ++i)
            d[i][0] = i;
        for(int j = 1; j < word2.size(); ++j)
            d[0][j] = j;


        for(int i = 1; i < word1.size(); ++i)
        {
            for(int j = 1; j < word2.size(); ++j)
            {
                d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1);
                int temp = (word1[i] == word2[j]) ? d[i - 1][j - 1] : d[i - 1][j - 1] + 1;
                d[i][j] = min(d[i][j], temp);
            }
        }
        cout << d[word1.size() - 1][word2.size() - 1] << endl;
    }


    return 0;
}
