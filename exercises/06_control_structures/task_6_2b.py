# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
correct_ip = False
while not correct_ip:
    ip_address = input("Enter ip address: ")
    octets = ip_address.split(".")

    if len(octets) != 4:
        correct_ip = False
    else:
        correct_ip = True
        for octet in octets:
            if not (octet.isdigit() and int(octet) in range(256)):
                correct_ip = False
                break

    if not correct_ip:
        print("Неправильный IP-адрес")
        continue
    else:
        octets_num = [int(i) for i in octets]

        if octets_num[0] in range(1, 224):
            print("unicast")
        elif octets_num[0] in range(224, 240):
            print("multicast")
        elif ip_address == "255.255.255.255":
            print("local broadcast")
        elif ip_address == "0.0.0.0":
            print("unassigned")
        else:
            print("unused")
