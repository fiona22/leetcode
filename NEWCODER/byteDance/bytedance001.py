import sys
N = int(sys.stdin.readline().strip())
sum = 1024
res = sum - N

n1 = res/64
res1 = res-n1*64

n2 = res1/16
res2 = res1-n2*16

n3 = res2/4
res3 = res2-n3*4

print n1+n2+n3+res3


'''
#include<iostream>
using namespace std;
int main(){
    int m;
    cin>>m;
    int n = 1024-m;
    int n1,n2,n3,n4;
    int m1,m2,m3,m4;
    m1 = n/64;
    n1 = n-m1*64;
    m2 = n1/16;
    n2 = n1-m2*16;
    m3 = n2/4;
    n3 = n2-m3*4;
    m4 = n3/1;
    cout<<m1+m2+m3+m4<<endl;
    return 0;
}


import sys
N = int(sys.stdin.readline().strip())
sum = 1024
count = []
if N <= 1024:
    res = sum - N
    if res >= 64:
        res1 = res % 64
        count.append(res / 64)
        if res1 >= 16:
            res2 = res1%16
            count.append(res1/16)
            if res2 >= 4:
                res3 = res2 % 4
                count.append(res2/4)
                count.append(res3)
result = 0
for i in count:
    result += i
print result
'''