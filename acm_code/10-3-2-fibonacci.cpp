 #include <iostream>
 using namespace std;

 int fibonacci(int n)
 {
    if(n == 0) return 1;
    if(n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
 }

 int main()
 {
     int f;
     int n;
     cout << "Please input n:" << endl;
     cin >> n;
     f = fibonacci(n);
     cout << f << endl;
     return 0;
 }
