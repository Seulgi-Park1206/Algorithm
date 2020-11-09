# 큰 수의 법칙
'''
* 저자(나동빈)의 큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만든느 법칙.
(단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음.)

* 문제 *
[입력 조건]
    - 첫째 줄에 N(2<=N<=10,000), M(1<=M<=10,000), K(1<=K<=10,000)의 자연수가 주어지며,
      각 자연수는 공백으로 구분한다.
    - 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 
      단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
    - 입력으로 주어지는 k는 항상 M보다 작거나 같다.

[출력 조건]
    - 첫째 줄에 저자의 큰 수의 법칙에 따라 더해진 답을 출력한다.

[입력 예시]
5 8 3
2 4 5 4 6

[출력 예시]
46
'''
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

m2 = m  # m2 : 2번에서 사용할 m

data.sort() # 입력 받은 수 정렬하기
first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

# 1. 반복문을 사용하여 단순하게 구하기
result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second    # 두 번째로 큰 수를 한 번 더하기
    m -= 1

print(result)   # 최종 결과 출력

# 2. 가장 큰 수가 더해지는 횟수를 계산해서 구하기
print("m : %d, k : %d, first : %d, second : %d" %(m2, k, first, second))
count = int(m2 / (k + 1)) * k
count += m2 % (k + 1)    # m을 (k + 1)로 나눈 나머지가 존재할 때 그 나머지만큼 가장 큰 수가 더해지므로
print("count :", count)
result2 = 0
result2 += (count) * first   # 가장 큰 수 더하기
result2 += (m2 - count) * second # 두 번째로 큰 수 더하기

print(result2)  # 최종 결과 출력
