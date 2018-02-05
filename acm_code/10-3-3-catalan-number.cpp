 #include <iostream>
 using namespace std;

 int catalan(int n)
 {
     if(n == 3) return 1;
     return catalan(n - 1) * (4 * n - 10) / (n - 1);
 }

 int main()
 {
     int c;
     int n;
     cout << "Please input n:" << endl;
     cin >> n;
     if(n >= 3)
     {
          c = catalan(n);
        cout << c << endl;
     }
     else cout << "No triangle." << endl;
     return 0;
 }
