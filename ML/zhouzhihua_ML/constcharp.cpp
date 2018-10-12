#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	char ch[3] = {'a','b','c'};
	char* const cp = ch;
	printf("char* const cp: \n %c\n", *cp);
	/* 
	** cp point to a fixed address
	**
	cp++;  //error: increment of read-only variable ‘cp’
	printf("char* const cp: \n %c\n", *cp);
	**
	*/

	const char ca = 'a';
	const char* p1 = &ca;

	/* 
	** 2. Only const char* pointer can point to a const char
	**
	const char cb = 'b';
	char* p2 = &cb; //error: invalid conversion from ‘const char*’ to ‘char*’
	**
	**/

	/*
	** 3. p1 points to a const char, the char be pointed has to be const, 
	**    p1 can point to a different const char
	*/ 
	printf("const char* p1: \n %c\n", *p1);
	const char cb = 'b';
	p1 = &cb;
	printf(" %c\n", *p1);
	return 0;
}

/*
** Output:
char* const cp: 
 a
const char* p1: 
 a
 b
**
*/