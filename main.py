# -*- coding: utf-8 -*-

import socket

def fanc1():
    a = ("[+]")
    print("~"*50)
    host = input(a + "Host --> ")
    port = int(input(a + "Port --> "))
    print("~"*50)

    scan = socket.socket()

    b = ("[!]")
    c = ("[!]")

    try:
        scan.connect((host,port))
    except scan.error:
        print(b + "Port -- ", port, " -- [CLOSED]")
    else:
        print(c + "Port -- ", port, " -- [OPEN]")

def fanc2():
    a = ("[+]")
    b = ("[!]")
    c = ("[!]")

    host = input(a + " Host --> ")
    print("\n")
    port = [21,22,80,443,1337]

    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.5)
            scan.connect((host, i))
        except socket.error:
            print(b + "Port -- ", i, " -- [CLOSED]")
        else:
            print(c + "Port -- ", i, " -- [OPEN]")

print("~"*55, "\n")

print("\t[1] --- Сканировать единичный порт")
print("\t[2] --- Сканировать список популярных портов", "\n")

print("~"*55, "\n")

text_a = input("[scan] --> ")

if text_a == "1":
    fanc1()
elif text_a == "2":
    fanc2()
else:
    print("Ошибка, неверный параметр!")
