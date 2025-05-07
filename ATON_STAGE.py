# 1 Задача:
coin = 5
nikel_cost = 100000/1000000
nikel_weight = 5/4
result = nikel_cost * nikel_weight
result2 = result * 100
print(f'Стоимость никеля в монете: Доллары - {result}, центы - {result2}')


# 2 Задача:
# Без использования оконных функций
# SELECT *
# FROM accounts
# WHERE phone IN (
#     SELECT phone
#     FROM accounts
#     GROUP BY phone
#     HAVING COUNT(*) > 1
# );


# С использованием оконных функций
# SELECT acc, name, email, phone
# FROM (
#     SELECT acc, name, email, phone,
#            COUNT(*) OVER (PARTITION BY phone) AS phone_counter
#     FROM accounts
# ) AS aton
# WHERE phone_counter > 1;



