#!/usr/local/bin/python
# это простейший веб-сервер

import socket # сокеты беркли стандартная библиотека

server_socket = socket.socket()
server_socket.bind(('', 8080)) # где ''  - адрес подсети откуда разрешаем коннекты, если пустая строка - слушаем со всех; порт 8080
server_socket.listen(10) # 10 - размер очереди: макс 10 соединений могут стоять в очереди к серверу, остальные отбрасываются

# в цикле пытаемся заакцептить новое соеднинение:
while True:
    client_socket, remote_address = server_socket.accept()
    try:
        request = client_socket.recv(1024)
        client_socket.send(request.upper())
        print '{} : {}'.format(client_socket.getpeername(), request)
        client_socket.close()
    except:
        pass

server_socket.close()

# недостаток - однопоточность: пока полностью не обработает запрос одного человека, другой чел будет ждать, что для веб серверов не подходит
# fork.py - под каждого юзера выделяется свой процесс
