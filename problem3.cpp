#include<iostream>
#include<cmath>
#include<cstring>
#define ll long long
using namespace std;
int const SIZE = 1e5+10;
bool arr[SIZE];

void BuildSeive(){
	for(int i = 2; i*i < SIZE; i++){
		if(arr[i]){
			for(int j = i*2; j < SIZE; j+=i) arr[j] = 0;
		}
	}
}

int main(){
	ll value = 600851475143, ans = 1;
	memset(arr, 1, sizeof(arr));
	BuildSeive();
	for(int i = 1; i < SIZE; i++) {
		if(arr[i]){
			if(value%i == 0) ans = i;
		}
	}

	cout<<ans<<endl;
	return 0;
}