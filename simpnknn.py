import numpy as np
M=1000
t=np.array([[ 1.0,1.0,  5.0,  0.0,  0.0,-M, 0.0],
            [ 0.0,3.0,  4.0,  1.0,  0.0, 0.0,  6.0 ],
            [ 0.0,1.0,  3.0,  0.0, -1.0, 1.0, 2.0]])
dict={}
for i in range(len(t[0])):
    if t[0][i]==-M:
        k=i
        print(k)
        for j in range(3):
            if t[j][k]==1:
                rr=j
        print(rr)
for i in range(1,7):
     t[0][i] =t[rr][i]*(-M)-t[0][i] 
print(t)
while True:
    if np.min(t[0]) >= 0:
        break
    m = np.argmin(t[0][:-1])
    min=t[0][m]
    print(min)
    n= 1e6
    for i in range(1,3):
        if t[i][-1]/t[i][m] > 0 and n > t[i][-1]/t[i][m]:
                n=t[i][-1]/t[i][m]
                c =i
    print("Pivot number: ",t[c][m])
    t[c] = t[c] / t[c][m]
    print(t[c])
    print()
    for i in range(3):
        if i == c:
            pass
        else:
            t[i] =t[i]-t[c] * t[i][m]
        print(t[i])
    print()
    for i in range(6):
        only_one_one = 0
        one=0
        for m in range(3):
            if t[m][i] == 1:
                one+= 1
                row =m
            only_one_one += t[m][i]
        if (one == 1) and (only_one_one== 1):
            dict[f"x_{i}"] = t[row][-1]
        else:
            dict[f"x_{i}"] = 0
            
        
print()
print(dict)
'''print(dict.items())
print(dict.values())
x2=dict.get('x_2')
print(5*x2)
#z=x1+5*x2+0*x3+0*x4-M*x5'''
