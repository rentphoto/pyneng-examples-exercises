# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
mac_table = []
vlan_in = input('Enter VLAN number: ')
with open("CAM_table.txt", "r") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, intf = words
            mac_table.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(mac_table):
    if vlan_in == str(vlan):
        print(f"{vlan:<9}{mac:20}{intf}")