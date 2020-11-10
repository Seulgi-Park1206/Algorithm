# 숫자 카드 게임
'''
* 문제 *
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임.
[룰]
    1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. (N : 행, M : 열)
    2. 먼저 뽑고자 하는 카드가 있는 행을 선택한다.
    3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
    4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 
        고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.


[입력 조건]
    - 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.
      (1 <= N, M <= 100)
    - 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.
    - 입력으로 주어지는 k는 항상 M보다 작거나 같다.

[출력 조건]
    - 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

[입력 예시1]
3 3
3 1 2
4 1 4
2 2 2

[출력 예시1]
2

[입력 예시2]
2 4
7 3 1 8
3 3 3 4

[출력 예시2]
3

* 아이디어 *
1. 각 행을 입력받아서 행의 최솟값을 구하기.
2. 구한 최솟값들 중에서 가장 큰 수를 출력.
'''
import time
#from ..check_memory.check_usage_of_memory import check_usage_of_memory
# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())
#t = 0   # 최솟값을 구하고 그들 중 최댓값을 찾는 시간
#end_t = 0   # 마지막 for문 끝나는 시간
result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
#    start_time = time.time()
    # 입력받은 행에서 최솟값 구하기
    min_value = min(data)
    # 최솟값들 중에서 가장 큰 수 구하기
    result = max(result, min_value)
#    end_time = time.time()
#    end_t = end_time
#    t += end_time - start_time

print(result)   # 최종 답 출력
#end_time = time.time() - end_t
#t += end_time
#print("시간:", t)
#check_usage_of_memory()