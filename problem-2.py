## 최댓값 찾기 2021-03-02

def func1(lst):
    max = 0
    for i in lst:
        if max < i:
            max = i
    return max

lst1 = [17,92,33,58,7,33,42]

print(func1(lst1))

## 모범답안 : 내가 짠 코드가 for문을 더 깊게 사용했다고 생각함 복잡도는 같음

def func2(lst):
    n = len(lst)
    max_v = lst[0]
    for i in range(1,n):
        if lst[i] > max_v:
            max_v = lst[i]
    return max_v

print(func2(lst1))

## 응용문제 : 리스트에 숫자가 n개 있을 때 가장 큰값이 있는 위치 번호를 돌려주는 알고리즘을 만들어 보세요

def func3(lst):
    max = 0
    for i in lst:
        if max < i:
            max = i
    return(lst.index(max))

print(func3(lst1))

## index 함수 안쓰고 짜기

def func4(lst):
    lst_len = len(lst)
    max_idx = 0
    for i in range(1,lst_len):
        if lst[i] > lst[max_idx]:
            max_idx = i
    return max_idx

print(func4(lst1))

## 연습문제 2-1 : 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들어 보세요.

def func5(lst):
    min = lst[0];
    for i in lst:
        if min > i:
            min = i
    return min

print(func5(lst1))