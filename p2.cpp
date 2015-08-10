#include <iostream>
#include <unordered_set>
#include <math.h>
#include <vector>

const int MAXN = 1000000000;
const int sqrtMXN = sqrt(MAXN);

using namespace std;

unordered_set<int> gen_prime_set(int M)
{
    unordered_set<int> p;
    vector<bool> isPrime(M, true);

    isPrime[0] = isPrime[1] = false;
    for (auto i = 2; i < M; i++) {
        if (!isPrime[i]) continue;
        p.insert(i);
        for (auto j = i * 2; j < M; j += i)
            isPrime[j] = false;
    }
    return p;
}

bool isPri(unordered_set<int>& pset, int k)
{
    if (k <= sqrtMXN) return (pset.find(k) != pset.end());
    else {
        for (auto it = pset.begin(); it != pset.end(); it ++)
            if (k%(*it) == 0) return false;
        return true;
    }
 }

void work(unordered_set<int>& pset, int a, int b)
{
    for (auto i = a; i <= b; i ++) {
        if (isPri(pset, i)) {
            cout << i << endl;
        }
    }
}

int main()
{
    unordered_set<int> pset = gen_prime_set(sqrt(MAXN)+1);
    //cout << pset.size() << endl;
    int n;
    cin >> n;
    for (auto i=0;i<n;i++) {
        int a, b;
        cin >> a >> b;
        work(pset, a, b);
        if (i < n - 1) cout << endl;
    }
    return 0;
}
