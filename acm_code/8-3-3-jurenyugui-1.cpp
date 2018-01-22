#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
using namespace std;
typedef long long ll;

typedef struct node
{
    int id;
    int x;
    int y;
    int type;
    double angle;
}NODE;
NODE p[1000];//结构体数组，用来储存每个人的信息
int ans[1000];//结构，ans[i]=j代表编号i和编号为j的相连
void sovel(int l,int r);

int main(int argc, char const *argv[])
{
    memset(ans,0,sizeof(ans));
    int x,y,t,len=1;
    while(scanf("%d%d%d",&t,&x,&y)!=EOF)// 录入数据
    {
        p[len].x   =x;
        p[len].y   =y;
        p[len].id  =len;//对应ID
        if(t==1)
            p[len].type=1;//表示类型
        else
            p[len].type=-1;
        len++;
    }
    len--;

    sovel(1,len);

    for(int i=1;i<=len;i++)
        printf("%d ",ans[i]);
    return 0;
}

void sovel(int l,int r)//递归求解，分治思想
{
    NODE t;
    if(l>=r)  return ;
    int pos=l;//初始化为第一个
    /************步骤1**************/
    for(int i=l+1;i<=r;i++)//找编号l-r区域内左下角节点
        if(p[i].y<p[pos].y||p[i].y==p[pos].y&&p[i].x<p[pos].x)
            pos=i;

    t=p[l];//交换
    p[l]=p[pos];
    p[pos]=t;

    int cnt=p[l].type;//从第一个开始
    /**************步骤2*************/
    for(int i=l+1;i<=r;i++)//计算点与左下角点的角度大小
        p[i].angle=atan2(p[i].y-p[l].y, p[i].x-p[l].x);

    /*for(int i=l;i<=r;i++)
    {
        printf("%d %d %d %lf\n",p[i].id,p[i].x,p[i].y,p[i].angle);
    }*/

    for(int i=l+1;i<=r;i++)//按角度大小，把除左下角的元素排序
    {
        for(int j=i;j<=r;j++)
        {
            if(p[i].angle>p[j].angle)
            {
                t=p[i];
                p[i]=p[j];
                p[j]=t;
            }
        }
    }

    /*for(int i=l;i<=r;i++)
    {
        printf("%d %d %d %lf\n",p[i].id,p[i].x,p[i].y,p[i].angle);
    }*/
    /**************步骤3***************/
    for(int i=l+1;i<=r;i++)//排序后，从小到大遍历
    {
        cnt+=p[i].type;
        if(cnt==0)//当遍历过后的区域巨人和鬼的数量相同时
        {
            ans[p[l].id]=p[i].id;//链接左下角点和当前点
            ans[p[i].id]=p[l].id;
            sovel(l+1,i-1);//分治，递归求解左边区域
            sovel(i+1,r);//分治，递归求解右边区域
            break;
        }
    }
    return ;
}

