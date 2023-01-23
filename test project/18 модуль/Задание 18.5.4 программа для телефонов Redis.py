import redis  # импортируем библиотеку
import json

red = redis.Redis(
    host='redis-18052.c270.us-east-1-3.ec2.cloud.redislabs.com',
    # ваш хост, если вы поставили Redis к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
    port=18052,
    # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегд разный, по этому его надо копировать оттуда же, что и host.
    password='bSIjyrkx8NFJPIkaNg6uWBKZhKmW0LwI'
    # для локальной машины пароль не требуется (если вы устанавливали Redis к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password.


cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break