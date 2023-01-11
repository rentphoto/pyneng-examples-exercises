# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
from pprint import pprint

addresslist = ['8.8.8.8', '0.0.0.0', '172.16.17.17']

def ping_ip_addresses(addrlist):
    alive = []
    unreachable = []
    for addr in addrlist:
        reply = subprocess.run(['ping', '-c', '3', '-n', addr], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            alive.append(addr)
        else:
            unreachable.append(addr)
    return alive, unreachable

if __name__ == "__main__":
    pprint(ping_ip_addresses(addresslist))