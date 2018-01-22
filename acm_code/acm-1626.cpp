#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<time.h>
using namespace std;
typedef long lld;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define eps 1e-8
#define pi acos(-1.0)
int Sig(double a) //初始化信号
{
	if(a < -eps)
	return -1;
	return a > eps; //大于无限小值
}
struct Point 
{
double x,y; 
Point(){} 
Point(double x0,double y0):x(x0),y(y0){} //点的横纵坐标
void in()
{
scanf("%lf %lf",&x,&y); //读入DOUBLE型数据
}
double len()
{
return sqrt(x*x+y*y); //开方
}
Point operator -(Point pt)
{
return Point(x-pt.x,y-pt.y); //重载-；定义新的X Y 。
}
};
struct Edge
{
int v,next;
}edge[1000010]; //元素个数
int head[110];// 前进；用头顶；作为…的首领；站在…的前头；给…加标题
int pos; //点；人名
void insert(int x,int y) 
{
edge[pos].v=y; //边缘
edge[pos].next=head[x];
head[x]=pos++;
}


bool in[20];
struct Event
{
double s;
int flag,id;// 标志；旗子vt. 标记；插旗vi. 标记；衰退；枯萎
Event(){}
Event(double s0,int flag0,int id0):s(s0),flag(flag0),id(id0){}
}pp[110];
int qq;
bool cmp(Event a,Event b)
{
return a.s < b.s;
}
Point p[110];
int T1,T2;
int dp[1<<16][2]; //位运算，将这个变量的二进制数值左移
int dfs(int mask,int flag) 
{
if(dp[mask][flag] != -1)
return dp[mask][flag];
if(flag == 0)
{
if(!(mask&T1))
return 0;
for(int k=0;k<8;k++)
if(mask&(1<<k))//取k的第i位 - 是否为0,不为0则为真,为0则假
{
for(int i=head[k];i;i=edge[i].next)
{
int to=edge[i].v;
int next=mask;
next|=1<<k; 
next^=1<<k; 
next|=to;
next^=to;
if(!dfs(next,flag^1))
{
dp[mask][flag]=1;
return 1;
}
}
}
dp[mask][flag]=0;
return 0;
}
else
{
if(!(mask&T2))
return 0;
for(int k=8;k<16;k++)
if(mask&(1<<k))
{
for(int i=head[k];i;i=edge[i].next)
{
int to=edge[i].v;
int next=mask;
next|=1<<k;
next^=1<<k;
next|=to;
next^=to;
if(!dfs(next,flag^1))
{
dp[mask][flag]=1;
return 1;
}
}
}
dp[mask][flag]=0;
return 0;
}
return (int)"you are so pretty";
}
int main()
{
T1=T2=0;
for(int i=0;i<8;i++)
T1+=1<<i;
for(int i=8;i<16;i++)
T2+=1<<i;
while(scanf("%lf %lf",&p[0].x,&p[0].y)!=EOF)
{
for(int i=1;i<16;i++)
p[i].in();
memset(head,0,sizeof(head));
pos=1;
for(int i=0;i<16;i++)
{
qq=0;
int T=0;
memset(in,false,sizeof(in));
for(int j=0;j<16;j++)
{
if(i == j)
continue;
double d=(p[i]-p[j]).len();
double add=asin(0.8/d);
double angle=atan2(p[j].y-p[i].y,p[j].x-p[i].x);
pp[qq++]=Event(angle-add-eps,-1,j);
pp[qq++]=Event(angle+add+eps,1,j);
}
for(int j=0;j<qq;j++)
{
while(pp[j].s < 0)
pp[j].s+=pi*2;
while(pp[j].s > pi*2)
pp[j].s-=pi*2;
}
sort(pp,pp+qq,cmp);
for(int j=0;j<qq;j++)
{
int id=pp[j].id;
if(pp[j].flag == -1)
in[id]=true;
else
in[id]=false;
}
int mask;
for(int j=0;j<qq;j++)
{
int id=pp[j].id;
mask=0;
for(int k=0;k<16;k++)
if(in[k])
mask|=1<<k;
insert(i,mask+T);
if(pp[j].flag == -1)
in[id]=true;
else
in[id]=false;

}
}
memset(dp,-1,sizeof(dp));
if(dfs((1<<16)-1,0))
printf("RED\n");
else
printf("WHITE\n");
}
return 0;
}