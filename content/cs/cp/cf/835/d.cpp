#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int get_cost(int x) {
    if (x==0){
        return INT32_MAX;
    }
    return x & -x;
}

int main() {
	int t;
	scanf("%d",&t);
	for(int k=0;k<t;k++)
	{
		int n;
		scanf("%d",&n);
		int a[n];
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}

        int res = 0, i = 0, connected = 0;

        vector<bool> visited(n);
        priority_queue<pair<int, int>> pq;
        while (++connected < n) {
            visited[i] = true;
            for (int j = 0; j < n; ++j)
                if (!visited[j])
                    pq.push({get_cost(a[i] & a[j]), j});
            while (visited[pq.top().second])
                pq.pop();
            res -= pq.top().first;
            i = pq.top().second;
            pq.pop();
        }
        if (res == INT32_MAX){
            return -1;
        }
        return res;
		
	}
	return 0;
}