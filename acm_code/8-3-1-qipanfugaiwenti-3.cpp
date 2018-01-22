#include <iostream>
using namespace std;

const int size=8;
static int tile = 1;
static int board[size][size] = {0};

class  ChessBoard
{
public:

	static void chessBoard(int tr, int tc, int dr, int dc, int size)
	{
		if(1==size) return;
		int t = tile++;
		int s = size / 2;

		//left top
		if(dr < tr + s && dc < tc + s)
		{
			chessBoard(tr, tc, dr, dc, s);
		}
		else
		{
			board[tr + s - 1][tc + s - 1] = t;
			chessBoard(tr, tc, tr + s -1, tc +s -1, s);
		}

		//right top
		if(dr < tr + s && dc >= tc + s)
		{
			chessBoard(tr, tc + s, dr, dc, s);
		}
		else
		{
			board[tr + s - 1][tc + s] = t;
			chessBoard(tr, tc + s, tr + s -1, tc + s, s);
		}

		//left bottom
		if(dr >= tr + s && dc < tc + s)
		{
			chessBoard(tr + s , tc, dr, dc, s);
		}
		else
		{
			board[tr + s][tc + s -1] = t;
			chessBoard(tr + s, tc, tr +s, tc + s - 1, s);
		}

		//right bottom
		if(dr >= tr + s && dc >= tc + s)
		{
			chessBoard(tr + s, tc + s, dr, dc, s);
		}
		else
		{
			board[tr + s][tc + s] = t;
			chessBoard(tr + s, tc + s, tr + s, tc + s,s);
		}
	}

	static void output()
	{
		for(int i = 0; i < size; ++i)
		{
			for(int j = 0; j < size; ++j)
			{
				cout << board [i][j] << " ";
			}
			cout<<endl;
		}
	}
};

int main()
{
	ChessBoard::chessBoard(0,0,3,4,size);
	ChessBoard::output();
	return 0;
}
