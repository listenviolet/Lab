#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <stack>
using namespace std;

static const char list[] = {
	0,0,0,
    0,0,1,0,0,2,0,0,3,0,1,0,0,2,0,0,3,0,1,0,0,2,0,0,
    0,1,1,0,1,2,0,1,3,0,2,1,0,2,2,0,2,3,0,3,1,0,3,2,0,3,3,
    1,0,1,1,0,2,1,0,3,2,0,1,2,0,2,2,0,3,
    1,1,0,1,2,0,1,3,0,2,1,0,2,2,0,2,3,0,
    1,1,1,1,1,2,1,1,3,1,2,1,1,2,2,1,2,3,1,3,1,1,3,2,1,3,3,
    2,1,1,2,1,2,2,1,3,2,2,1,2,2,2,2,2,3,2,3,1,2,3,2,2,3,3
};

class hypos {
public:
	virtual int insert(int cur) = 0;
};

class hypo: public hypos
{
public:
	hypo(int a, int b, int c)
	{
		hypo_const = 0;
		vector<char> p[3];
		if(a == 0)
		{
			p[0].push_back(1);
			p[0].push_back(2);
		}
		else p[0].push_back(a);

		if(b == 0)
		{
			p[1].push_back(1);
			p[1].push_back(2);
			p[1].push_back(3);
		}
		else p[1].push_back(b);

		if(c == 0)
		{
			p[2].push_back(1);
			p[2].push_back(2);
			p[2].push_back(3);
		}
		else p[2].push_back(c);

		for(unsigned int i = 0; i < p[0].size();i++)
			for(unsigned int j = 0; j < p[1].size(); j++)
				for(unsigned int k = 0; k < p[2].size(); k++)
					hypo_const |= (1 << (p[0][i] * 9 + p[1][j] * 3 + p[2][k]) - 13);
	}

	int insert(int cur)
	{
		return (hypo_const & cur);
	}
	

private:
	int hypo_const;
};

class hypo_ss: public hypos
{
public:
	hypo_ss(int _ptr, int tmp)
	{
		hypo_tmp = tmp;
		ptr = _ptr;
	}

	int insert(int cur)
	{
		return 0;
	}

	int hypo_tmp;
	int ptr;
};

class Traversal : public hypos
{
public:
	Traversal()
	{
		hypos_cur = 0x3ffff;
		for(int i = 0; i < 48; ++i)
		{
			hyposs.push_back(hypo(list[3 * i], list[3 * i + 1], list[3 * i + 2]));
		}
	}
	int insert(int cur)
	{
		int ptr = cur;
		while(1)
		{
			if(ptr > 47 && !ss.size()) break;

			if(hypos_cur == 0 || ptr > 47)
			{
				hypo_ss hypo_tmp = ss.top();
				hypos_cur ^= hypo_tmp.hypo_tmp;
				ptr = hypo_tmp.ptr + 1;
				ss.pop();
				continue;
			}

			if(int tmp = hyposs[ptr].insert(hypos_cur))
			{
				hypos_cur ^= tmp;
				ss.push(hypo_ss(ptr, tmp));
				if(sum.size() < ss.size())
					sum.push_back(0);
				sum[ss.size() - 1]++;
			}
			ptr++;
		}
		return 1;
	}

	void print()
	{
		for(unsigned int i = 0; i < sum.size(); ++i)
			printf("length %d : %d\n", i + 1, sum[i]);
	}

private:
	vector<int> sum;
	stack<hypo_ss> ss;
	int hypos_cur;
	vector<hypo> hyposs;
};

int main()
{
	Traversal traversal;
	traversal.insert(0);
	traversal.print();
	system("pause");
	return 0;
}