money = int(input('Сумма вложений на 1 год: '))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}


tkb = round(per_cent['ТКБ'] * money/100, 3)
skb = round(per_cent['СКБ'] * money/100, 3)
vtb = round(per_cent['ВТБ'] * money/100, 3)
sber = round(per_cent['СБЕР'] * money/100, 3)

deposit = [tkb, skb, vtb, sber]
print('Накопленные средства за год вклада в каждом из банков:', deposit)

deposit.sort()
print('Максимальная сумма, которую вы можете заработать:', max(deposit))