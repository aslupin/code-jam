#include <iostream>
//#include <math.h>
//#include <stdlib.h>
//#include <iomanip>
#include <queue>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        long long n,k;
        cin >> n >> k;
        priority_queue<long long> pq;
        pq.push(n);
        long long l,r;
        while(k>=1)
        {
            long long t = pq.top();
            pq.pop();
            l = t/2;
            r = t-t/2-1;
            pq.push(l);
            pq.push(r);
            k--;
        }

       //Answer
        cout << "Case #" << i+1 << ": ";
        cout << l << " " << r << endl;
    }
    return 0;
}
