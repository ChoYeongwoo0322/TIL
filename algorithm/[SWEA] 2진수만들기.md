#### 2진수만들기

```python
'''
3
0.625
0.1
0.125
'''

for tc in range(1, int(input())+1):
    num=float(input())
    result=""
    while True:
        num*=2
        result+=str(int(num))
        num-=int(num)

        if not num%2:
            break
        elif len(result)>13:
            result="overflow"
            break
    print("#{} {}".format(tc, result))
```

