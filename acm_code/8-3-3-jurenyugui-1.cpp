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
NODE p[1000];//�ṹ�����飬��������ÿ���˵���Ϣ
int ans[1000];//�ṹ��ans[i]=j������i�ͱ��Ϊj������
void sovel(int l,int r);

int main(int argc, char const *argv[])
{
    memset(ans,0,sizeof(ans));
    int x,y,t,len=1;
    while(scanf("%d%d%d",&t,&x,&y)!=EOF)// ¼������
    {
        p[len].x   =x;
        p[len].y   =y;
        p[len].id  =len;//��ӦID
        if(t==1)
            p[len].type=1;//��ʾ����
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

void sovel(int l,int r)//�ݹ���⣬����˼��
{
    NODE t;
    if(l>=r)  return ;
    int pos=l;//��ʼ��Ϊ��һ��
    /************����1**************/
    for(int i=l+1;i<=r;i++)//�ұ��l-r���������½ǽڵ�
        if(p[i].y<p[pos].y||p[i].y==p[pos].y&&p[i].x<p[pos].x)
            pos=i;

    t=p[l];//����
    p[l]=p[pos];
    p[pos]=t;

    int cnt=p[l].type;//�ӵ�һ����ʼ
    /**************����2*************/
    for(int i=l+1;i<=r;i++)//����������½ǵ�ĽǶȴ�С
        p[i].angle=atan2(p[i].y-p[l].y, p[i].x-p[l].x);

    /*for(int i=l;i<=r;i++)
    {
        printf("%d %d %d %lf\n",p[i].id,p[i].x,p[i].y,p[i].angle);
    }*/

    for(int i=l+1;i<=r;i++)//���Ƕȴ�С���ѳ����½ǵ�Ԫ������
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
    /**************����3***************/
    for(int i=l+1;i<=r;i++)//����󣬴�С�������
    {
        cnt+=p[i].type;
        if(cnt==0)//�����������������˺͹��������ͬʱ
        {
            ans[p[l].id]=p[i].id;//�������½ǵ�͵�ǰ��
            ans[p[i].id]=p[l].id;
            sovel(l+1,i-1);//���Σ��ݹ�����������
            sovel(i+1,r);//���Σ��ݹ�����ұ�����
            break;
        }
    }
    return ;
}

