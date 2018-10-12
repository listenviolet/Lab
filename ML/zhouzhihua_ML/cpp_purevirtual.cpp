#include <iostream>
#include <cstdio>
using namespace std;

class CShape
{
public:
	virtual void Show()= 0;
};

class  CPoint2D: public CShape
{
public:

	void Msg()
	{
		printf("CPoint2D.Msg() is invoked.\n");
	}

	void Show()
	{
		printf("Show() from CPoint2D.\n");
	}
};

int main()
{
	CPoint2D p2d;
	p2d.Msg();
	CPoint2D *pShape = &p2d;
	pShape -> Show();
	return 0;
}

/* Output:
CPoint2D.Msg() is invoked.
Show() from CPoint2D.
*/