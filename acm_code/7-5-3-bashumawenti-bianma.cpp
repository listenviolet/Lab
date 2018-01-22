int vis[362880], fact[9];

void init_lookup_table()
{
	fact[0] = 1;
	for(int i = 1; i < 9; i++)
	{
		fact[i] = fact[i-1] * i;
	}
}

int try_to_insert(int s)
{
	int code;
	for(int i = 0; i < 9; i++)
	{
		int cnt = 0;
		for(int j = i+1; j < 9; j++)
		{
			if(st[s][j] < st[s][i]) cnt++;
		}
		code += fact[8-i] * cnt;
	}

	if(vis[code]) return 0;
	return vis[code] = 1;
}