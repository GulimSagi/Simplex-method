import numpy as np
M=1000
t=np.array([[1,-M-1, -M+1,-2*M-3, 0.0, 0.0, M,0,0],
            [0,1,1,0,1,0,0,0,20 ],
            [0,1,0,1,0,1,0,0,5],
            [0,0,1,1,0,0,-1,1,10]])
dict={}
while True:
    if np.min(t[0]) >= 0:
        break
    m = np.argmin(t[0][:-1])
    min=t[0][m]
    print(min)
    n= 1e17
    for i in range(4):
        if t[i][-1]/t[i][m] > 0:
              if n > t[i][-1]/t[i][m]:
                n=t[i][-1]/t[i][m]
                c =i
    print("Pivot number: ",t[c][-1]/t[c][m])
    t[c] = t[c] / t[c][m]
    print(t[c])
    print()
    for i in range(4):
        if i == c:
            pass
        else:
            t[i] =t[i]-t[c] * t[i][m]
        print(t[i])
    print()
    for i in range(9):
        only_one_one = 0
        one=0
        for m in range(4):
            if t[m][i] == 1:
                one += 1
                row =m
            only_one_one += t[m][i]
        if (one == 1) and (only_one_one== 1):
            dict[f"x_{i}"] = t[row][-1]
        
print()
print(dict)
print(dict.items())
print(dict.values())
x2=dict.get('x_2')
print(5*x2)
#z=x1+5*x2+0*x3+0*x4-M*x5

