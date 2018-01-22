set<int> vis;
void init_lookup_table() {vis.clear();}
int try_to_insert(int s){
	int v=0;
	for(int i=0;i<9;i++) v = v*10 + st[s][i];                   
	if(vis.count(v)) return 0;
	vis.insert(v);
	return 1;
}