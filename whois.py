#!/usr/share/python

import socket,sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.connect(("whois.iana.org", 43))
    
    query = sys.argv[1]+"\r\n"
    s.send(query.encode())
    
    resposta = s.recv(1024)
    
    print(resposta.decode('utf-8', errors='ignore'))

except Exception as e:
    print(f"Erro de conexão: {e}")

finally:
    s.close()
