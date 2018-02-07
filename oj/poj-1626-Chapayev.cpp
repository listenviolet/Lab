#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <iostream>
using namespace std;
/**
 *  博弈论 + 计算几何 + 记忆化搜索
 *
 *博弈论：
 *  必胜态 ： 当前状态按照"某个"策略走一步， 能够走到对方的必败态， 那么当前状态就是必胜态
 *  必败态 ： 当前状态"无论"用什么策略走， 都只能走到对方的必胜态， 那么当前状态是必败态
 *  
 *记忆化搜索：
 *  那么如何能够判断走一步之后的状态是什么呢， 那么就要用记忆化搜索，不断走，直到走到最简单的边界状态，就能走很容易判断出是是必胜还是必败,
 *  然后递归返回
 *
 *计算几何:
 *  要用计算几何算出，每个棋子所具有的策略， 也即每个棋子可能怎么走。
 *	因为每个棋子都能够任意走，所以不能去枚举棋子所走的角度，因为角度是小数， 是无限的。
 *	由于棋子个数很少，所以移动第i个棋子时，可以枚举其要不要撞第j个棋子， 如果要撞， 那么还要判断在该过程中能不能撞到其它的棋子
 *
 *	第i个圆要撞第j个圆， 设它们的两条内公切线的极角为r1 = base - angle, r2 = base + angle,  那么第i个圆沿着区间[r1,r2]内的角度走，能是可以
 *	撞到第j个圆的； 设第i个圆和第k个圆的公切线极角为[r3, r4],  如果r3 in [r1, r2] or r4 in [r1, r2], 那么说明i能够同时撞到j和k。
 *	
 *	所以第i个圆所有可能的走法就是： 求出第i个圆和其他圆的公切线， 共30条， 排序， 然后扫描一圈， 加加减减，就能够求出所有的策略。 
 *
 */
void printStatus(int idx, int mask)
{
	printf("%d---\n", idx);
	for(int i = 0; i < 16; ++i)
	{
		if((mask) & (1 << i))
		{
			printf("%d ", i);
		}
	}
	printf("\n");
}

struct Point
{
	double x, y;
	Point(){}
	Point(double _x, double _y) : x(_x), y(_y){}
	Point operator - (const Point& rhs)
	{
		return Point(x - rhs.x, y - rhs.y);
	}
	double len()
	{
		return sqrt(x * x + y * y);
	}
};

class Direction
{
public:
	double angle;
	int id, flag;
	Direction(){}
	Direction(double _angle, int _id, int _flag) : angle(_angle), id(_id), flag(_flag){}
};
bool cmp(const Direction& lhs, const Direction& rhs)
{
	return lhs.angle < rhs.angle;
}

Point p[16];
Direction dir[30];
int can_hit[16];
int status[16][30];
const int red_status = (1 << 8) - 1;
const int white_status = (1 << 16) - 1 - red_status;

//00000000 11111111, 11111111 00000000
const int STATUS[] = {(1 << 8) - 1, (1 << 16) - (1 << 8)};

const int L[] = {0, 8};
const int R[] = {8, 16};

int dp[1 << 16][2];

int transfer(int, int);
/*
 * color = 0 : red
 * color = 1 : white
 * */
int dfs(int sta, int color)
{
	if(dp[sta][color] != -1)
		return dp[sta][color];
	return transfer(sta, color);
}

int transfer(int sta, int color)
{
	if(!(sta & (STATUS[color])))
			return 0;
	int l = L[color], r = R[color];
	for(int i = l; i < r; ++i)
	{
		if(sta & (1 << i))
		{
			for(int j = 0; j < 30; ++j)
			{
				int next_sta = sta;
				//第i个棋子移动后，消失
				next_sta ^= 1 << i;
				//其撞到的那些棋子也消失
				next_sta |= status[i][j];
				next_sta ^= status[i][j];
				//如果dfs返回0， 那么说明对方处于必败态
				//也即说明从当前状态走一步走到了对方的必败态，所以自己的必胜态
				if(!dfs(next_sta, color^1))
					return dp[sta][color] = 1;
			}
		}
	}
	//走到这里，说明当前状态是必败态
	return dp[sta][color] = 0;
}
int main()
{
	while(scanf("%lf %lf", &p[0].x, &p[0].y) != EOF)
	{
		for(int i = 1; i < 16; ++i)
		{
			scanf("%lf %lf", &p[i].x, &p[i].y);
		}

		for(int i = 0; i < 16; ++i)
		{
			int cnt = 0;
			for(int j = 0; j < 16; ++j)
			{
				if(i == j) continue;
				double dis = (p[i] - p[j]).len(); //圆心距
				double base = atan2(p[j].y - p[i].y, p[j].x - p[i].x); // 两圆内切线的极角，也即切线与水平方向的夹角
				double angle = asin(0.8 / dis); //// 第i个圆沿着角度base - angle或base + angle 走， 那么刚好切到第j个圆的边缘
				dir[cnt++] = Direction(base - angle, j, -1);
				dir[cnt++] = Direction(base + angle, j, 1);
			}

			sort(dir, dir + cnt, cmp);
			memset(can_hit, 0, sizeof(can_hit));

			//将角度排序之后，找出第i个圆的所有可能的走法
			//使用逆时针扫描线，扫出第i个圆不同策略下， 能撞到的棋子的状态
			for(int j = 0; j < cnt; ++j)
			{
				int id = dir[j].id;
				can_hit[id] += dir[j].flag;
				int sta = 0;
				for(int k = 0; k < 16; ++k)
					if(can_hit[k] != 0)
						sta |= 1 << k;

				/* if(i == 0) */
					/* printStatus(i, sta); */

				/* 第i个圆能够杀死由状态sta所表示的那些棋子 */	
				status[i][j] = sta;
			}
		}
		memset(dp, -1, sizeof(dp));
		if(dfs((1 << 16) - 1, 0))
			printf("RED\n");
		else
			printf("WHITE\n");
	}
	return 0;
}
