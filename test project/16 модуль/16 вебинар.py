# у объекта есть 2 характеристики
# 1) атрибуты
# 2) поведение
# объект - попугай
# свойства: имя, возраст - атрибуты
# попугай поет и танцует - поведение
# DRY
# Класс - шаблон объекта

# class Parrot:
#     pass
#
#
# # Объект - экземпляр класса
# obj = Parrot()
#
# class Parrot:
#     species = 'птица'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # создаем экземпляр класса
#
# kesha = Parrot('кеша', 10)
# cookie = Parrot('Куки', 15)
# # получаем доступ к атрибутам класса
# print(f'кеша - {kesha.__class__.species} ')
# print(f'Куки тоже  {cookie.__class__.species} ')
# # получаем доступ к атрибутам экземпляра
# print(f'{kesha.name} - {kesha.age}')
# print(f'{cookie.name} - {cookie.age}')

# # методы == функции == действие
#
# class Parrot:
#     def  __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sing(self, song):
#         return f'{self.name} поет {song}'
#     def dance(self,):
#         return f'{self.name} танцует '
# kesha = Parrot('Кеша', 10)
# print(kesha.sing('песенки'))
# print(kesha.dance())

# # Наследование
# # Родительский класс
# class Bird:
#     def __init__(self):
#         print('птица готова')
#     def whoIsThis(self):
#         print('птица')
#     def swim(self):
#         print('плывет быстрее')
#
# # Дочерний класс
# class Penguin(Bird):
#     def __init__(self):
#         super().__init__()
#         print('пингвин готов')
#     def whoIsThis(self):
#         print('пингвин')
#     def run(self):
#         print('бежит быстрее')
#
# peggy = Penguin()
# peggy.whoIsThis()
# peggy.swim()
# peggy.run()