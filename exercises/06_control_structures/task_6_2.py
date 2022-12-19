# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
address = input("Введите IP адрес: ")
first_byte = int(address.strip().split('.')[0])

if first_byte >= 1 and first_byte <= 223:
    print('unicast')
elif first_byte >= 224 and first_byte <= 239:
    print('multicast')
elif address == '255.255.255.255':
    print('local broadcast')
elif address == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
