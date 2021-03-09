## 동명이인 찾기 2021-03-09

name = ["Tom", 'Jerry', 'Mike', 'Tom','Mike','Tom']

def find_some_name(lst):
    num = len(lst)
    result = set() # set을 사용하는 이유 : 중복방지
    for i in range(0,num-1):
        target = lst[i]
        for j in range(i+1,num):
            if lst[i] == lst[j]:
                result.add(lst[i])
    return result

print(find_some_name(name))

# 연습문제 3-1 : n명 중 두 명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는
# 모든 조합을 출력하는 알고리즘을 만들어 보세요

name2 = ["Tom","Jerry","Mike","Tim"]

def mating(lst):
    num = len(lst)
    for i in range(0,num-1):
        for j in range(i+1, num):
            print(lst[i]+"-"+lst[j])

mating(name2)

"""
연습문제 3-2 : 다음 식을 각각 대문자 O 표기법으로 표현해 보세요.
A. 65536 : O(n^16) x 답 : O(1) n값의 변화와 상관없음
B. n-1 : O(n) o
C. 2/3*n^2 + 10000n : O(n^2) o
D. 3n^4 - 4n^3 + 5n^2 -6n + 7 : O(n^4) o 
"""