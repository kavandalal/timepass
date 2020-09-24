#include<bits/stdc++.h>
using namespace std;
int main(){
	vector<int> a;
	int target,c=0;
	do{
		int num;
		cin >> num;
		a.push_back(num);
		c++;
	}while(getchar()!= '\n');
	cin >> target;
	for (int i=0;i<c;i++){
		for(int j=0;j<c;j++){
			if (i==j){
				break;
			}
			if((a[i] + a[j]) == target){
				cout << j <<" "<<i;
			}
		}
	}
	return 0;
}