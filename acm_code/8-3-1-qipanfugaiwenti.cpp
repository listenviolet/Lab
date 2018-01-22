#include<iostream>  
#include<vector>  
#include<stack>  
  
using namespace std;  
  
vector<vector<int> > board(4);//棋盘数组，也可以作为参数传递进chessBoard中去，作为全局变量可以减少参数传递  
stack<int> stI;   //记录当前所使用的骨牌号码，使用栈顶元素填充棋盘数组  
int sL = 0;     //L型骨牌序号  
  
//所有下标皆为0开始的C C++下标  
void chessBoard(int uRow, int lCol, int specPosR, int specPosC, int rowSize)  
{  
    if(rowSize ==1) return;  
    //static int sL = 0;棋牌和骨牌都可以用static代替，如果不喜欢用全局变量的话。  
    sL++;     
    stI.push(sL); //每递归深入一层，就把一个骨牌序号入栈  
    int halfSize = rowSize/2;//拆分  
  
    //注意：下面四个if else，肯定是只有一个if成立，然后执行if句，而肯定有三个else语句要执行的，因为肯定有一个是特殊位置，而其他三个是空白位置，需要填充骨牌。  
  
    //1如果特殊位置在左上角区域，则继续递归，直到剩下一个格子，并且该格子已经填充，遇到函数头一句if(rowSize == 1) return;就跳出一层递归。  
    //注意是一个区域或子棋盘，有一个或者多个格子，并不是就指一个格子。  
    if(specPosR<uRow+halfSize && specPosC<lCol+halfSize)  
        chessBoard(uRow, lCol, specPosR, specPosC, halfSize);  
    //如果其他情况  
    else  
    {  
        board[uRow+halfSize-1][lCol+halfSize-1] = stI.top();  
        //因为特殊位置不在，所以可以选择任意一个空格填充，但是本算法只填充左上角（也许不止一个格，也许有很多个格子）区域的右下角。大家仔细查一下，就知道下标[uRow+halfSize-1][lCol+halfSize-1]是本区域中最右下角的一个格子的下标号。  
        chessBoard(uRow, lCol, uRow+halfSize-1, lCol+halfSize-1, halfSize);  
        //然后是递归填充这个区域的其他空白格子。因为上一句已经填充了[uRow+halfSize-1][lCol+halfSize-1]这个格子，所以，这个下标作为特殊位置参数传递进chessBoard中。  
    }     
  
    //2右上角区域，解析类上  
    if(specPosR<uRow+halfSize && specPosC>=lCol+halfSize)  
        chessBoard(uRow, lCol+halfSize, specPosR, specPosC, halfSize);  
    else  
    {  
        board[uRow+halfSize-1][lCol+halfSize] = stI.top();  
        chessBoard(uRow, lCol+halfSize, uRow+halfSize-1, lCol+halfSize, halfSize);  
    }         
  
    //3左下角区域，类上  
    if(specPosR>=uRow+halfSize && specPosC<lCol+halfSize)  
        chessBoard(uRow+halfSize, lCol, specPosR, specPosC, halfSize);  
    else  
    {  
        board[uRow+halfSize][lCol+halfSize-1] = stI.top();  
        chessBoard(uRow+halfSize, lCol, uRow+halfSize, lCol+halfSize-1, halfSize);  
    }     
  
    //4右下角区域，类上  
    if(specPosR>=uRow+halfSize && specPosC>=lCol+halfSize)  
        chessBoard(uRow+halfSize, lCol+halfSize, specPosR, specPosC, halfSize);  
    else  
    {  
        board[uRow+halfSize][lCol+halfSize] = stI.top();  
        chessBoard(uRow+halfSize, lCol+halfSize, uRow+halfSize, lCol+halfSize, halfSize);  
    }     
  
    stI.pop();//本次骨牌号填充了三个格，填充完就出栈  
}  
  
void test()  
{  
    //初始化数组  
    for(int i=0; i<4; i++)  
    {  
        board[i].resize(4);  
    }  
  
    chessBoard(0, 0, 3, 3, 4);  
  
    //特殊位置填充0  
    board[3][3] = 0;  
  
    //序列输出  
    for(int j=0; j<4; j++)  
    {  
        for(int i=0; i<4; i++)  
            cout<<board[j][i]<<"\t";  
        cout<<endl;  
    }  
    cout<<endl;  
}  
  
  
int main()  
{  
    test();  
    return 0;  
} 