# Whois Simples

Um cliente Whois minimalista escrito em Python que consulta diretamente o servidor da IANA (Internet Assigned Numbers Authority) via sockets TCP.

## 🚀 Como funciona
A ferramenta estabelece uma conexão direta na porta **43** (padrão para o protocolo Whois) com o host `whois.iana.org`, envia o domínio desejado e retorna a resposta bruta do servidor.



## 🛠️ Requisitos
* Python 3.x
* Acesso à internet (porta 43/TCP liberada no firewall)

## 📦 Instalação
1. Clone este repositório:
   ```bash
   git clone [https://github.com/hofuman/whois.git](https://github.com/hofuman/whois.git)