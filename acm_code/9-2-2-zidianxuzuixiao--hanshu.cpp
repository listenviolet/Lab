void print_ans(int i)
{
	printf("%d ", i);
	for(int j = 1;j <= n; j++)
		if(G[i][j] && (d[i] == d[j] + 1))
		{
			print_ans(j);
			break;
		}
}