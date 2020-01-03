#include <cstdio>

bool isInc(int n)
{
	if (n < 10) return true;
	
	int v = n % 10;
	n /= 10;
	
	while (n)
	{
		if (v <= n%10)
		{
			v = n % 10;
			n /= 10;
		}
		else return false;
	}
	
	return true;
}
bool isDec(int n)
{
	if (n < 10) return true;
	
	int v = n % 10;
	n /= 10;
	
	while (n)
	{
		if (v >= n%10)
		{
			v = n % 10;
			n /= 10;
		}
		else return false;
	}
	
	return true;
}
int main()
{
	int law = 21780;
	int high = 10000000;
	int mid;
	
	while (law < high)
	{
		int cnt = 0;
		mid = (law + high) / 2;

		for (int i = 1; i <= mid; ++i)
			cnt += !isInc(i) && !isDec(i);
		
		if (1e2 * cnt / mid == 99) break;
		else if (1e2 * cnt / mid < 99) law = mid;
		else high = mid;
	}
	
	printf("%d", mid);
	return 0;
}

 
