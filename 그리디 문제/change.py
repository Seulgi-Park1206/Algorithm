# 거스름돈 문제
'''
* 문제 *
  - 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재
  - 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수는?
  - 단, 거슬러 줘야 할 돈 N은 항상 10의 배수

* 아이디어 *
가장 큰 화폐 단위부터 처리
'''
n = 1260
count = 0

print("거슬러 줘야 할 돈 : %d" %(n))
print('-'*50)
# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]
coin_count = []

for coin in coin_types:
    c_count = n // coin
    count += c_count  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    coin_count.append(c_count)
    print(">> %d원짜리 %d개 | 남은 거스름돈 : %d" %(coin, c_count, n))
print('-'*50)
# 구해야 하는 개수 및 각 단위별 필요한 개수 출력
print(">>> 거슬러 줘야 할 동전의 개수 : %d개" %(count))
for i in range(len(coin_types)):
    print("- %d원짜리 %d개" %(coin_types[i], coin_count[i]))
