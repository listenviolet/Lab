#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int myints[] = {10, 20, 30, 40};
    vector<int> myvector (myints, myints + 4);  //vector∏≥≥ı÷µ
    vector<int>::iterator it;
    it = find(myvector.begin(), myvector.end(), 30);
    if(it != myvector.end())
        cout << "Element found in myvector: " << *it << endl;
    else
        cout << "Element not found in myvector.\n";

    for(int i = 0; i < 4; ++i)
    {
        cout << myvector[i] <<endl;
    }

    cout << "myvector.end : " << *(myvector.end()) << endl; //0
    return 0;
}
