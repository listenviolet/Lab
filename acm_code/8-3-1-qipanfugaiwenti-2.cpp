#include<iostream>  
using namespace std;  
const int size = 8;  
static int tile = 1;  
static int board[size][size] = { 0 };  
  
  
class CHESSBOARD  
{  
public:  
    /* 
    分治法实现棋盘覆盖 
    */  
    static void chessBoard(int tr, int tc, int dr, int dc, int size)  
    {  
        //若棋盘大小小于1，则返回  
        if (1 == size)  
        {  
            return;  
        }  
        //L型骨牌  
        int t = tile++;  
        //分割棋盘  
        int s = size / 2;  
        //覆盖左上角子棋盘  
        if (dr < tr + s&&dc < tc + s)  
        {  
            //特殊方格再此棋盘中  
            chessBoard(tr, tc, dr, dc, s);  
        }  
        else  
        {  
            //此棋盘无特殊方格，用t号L型骨牌覆盖右下角  
            board[tr + s - 1][tc + s - 1] = t;  
            //递归其他方格  
            chessBoard(tr, tc, tr + s - 1, tc + s - 1, s);  
        }  
  
        //覆盖右上角棋盘  
        if (dr < tr + s&&dc >= tc + s)  
        {  
            //存在特殊方格  
            chessBoard(tr, tc + s, dr, dc, s);  
        }  
        else  
        {  
            //无特殊方格，用t号L型骨牌覆盖  
            board[tr + s - 1][tc + s] = t;  
            //覆盖其余方格  
            chessBoard(tr, tc + s, tr + s - 1, tc + s, s);  
        }  
  
        //覆盖左下角棋盘  
        if (dr >= tr + s&&dc < tc + s)  
        {  
            //存在特殊方格  
            chessBoard(tr + s, tc, dr, dc, s);  
        }  
        else  
        {  
            //否则，L型骨牌覆盖  
            board[tr + s][tc + s - 1] = t;  
            //覆盖剩余方格  
            chessBoard(tr + s, tc, tr + s, tc + s - 1, s);  
        }  
  
        //覆盖右下角棋盘  
        if (dr >= tr + s&&dc >= tc + s)  
        {  
            //存在特殊方格  
            chessBoard(tr + s, tc + s, dr, dc, s);  
        }  
        else  
        {  
            //L型骨牌覆盖  
            board[tr + s][tc + s] = t;  
            //递归遍历剩余棋盘空间  
            chessBoard(tr + s, tc + s, tr + s, tc + s, s);  
        }  
    }  
  
    //输出棋盘覆盖结果  
    static void output()  
    {  
        for (int i = 0; i<size; ++i)  
        {  
            for (int j = 0; j<size; ++j)  
            {  
                cout << board[i][j] << "\t";  
            }  
            cout << "\n";  
        }  
    }  
};  
  
int main()  
{  
    CHESSBOARD::chessBoard(0, 0, 3, 4, size);  
    CHESSBOARD::output();  
    return 0;  
}  