from socket import socket, AF_INET, SOCK_STREAM
import ssl
import base64
from sendEmail.extras import status, getMessage, getSubject


def sendEmail(messageType, var):
    #Declara a codifica��o utilizada na convers�o necess�ria de strings para bytes
    cod = 'UTF-8'

    # Escolhe um servidor SMTP, e sua respectiva porta.
    mailserver = "smtp.gmail.com"
    port = 465

    # Cria um socket chamado clientSocket e estabiliza a conex�o TCP.
    clientSocket = socket(AF_INET, SOCK_STREAM)
    ssl_clientSocket = ssl.wrap_socket(clientSocket)
    ssl_clientSocket.connect((mailserver, port))

    recv = ssl_clientSocket.recv(1024)

    # Se o SMTP retornar uma mensagem 220, significa que a conex�o foi estabelecida com o servidor SMTP.
    status(recv)

    # Envia o comando EHLO (sauda��es)
    heloCommand = 'EHLO\r\n'
    ssl_clientSocket.send(bytes(heloCommand, cod))
    recv = ssl_clientSocket.recv(1024)

    # Se o SMTP retornar uma mensagem 250, significa que a resposta para a sauda��o EHLO foi recebida e aceita.
    status(recv)

    # Nome do usu�rio e senha, e em seguida s�o convertidos para base64.
    username = bytes('emailtesteredes1@gmail.com', cod)
    password = bytes('a9b8c7d6e5', cod)

    username64 = base64.b64encode(username)
    password64 = base64.b64encode(password)


    # Inicia o processo de autentica��o
    #authCommand = 'AUTH LOGIN' + str(username64,cod) + '\r\n'
    authCommand = 'AUTH LOGIN\r\n'
    ssl_clientSocket.send(bytes(authCommand, cod))
    recv = ssl_clientSocket.recv(1024)

    #Verifica se o comando de autentica��o foi recebido
    status(recv)

    authCommand = str(username64, cod) + '\r\n'
    ssl_clientSocket.send(bytes(authCommand, cod))

    authCommand = str(password64, cod) + '\r\n'
    ssl_clientSocket.send(bytes(authCommand, cod))
    recv = ssl_clientSocket.recv(1024)

    #Verifica se foi autenticado com sucesso
    status(recv)

    #Dados da mensagem
    sender = 'Servidor'
    receiver = 'jpaulocpm@gmail.com'
    cc = ''
    cco = ''
    subject = getSubject(messageType)
    message = getMessage(messageType, var)    


    # Send MAIL FROM command and print server response.
    mailFromCommand = 'MAIL FROM: <'+ sender +'>\r\n'
    ssl_clientSocket.send(bytes(mailFromCommand, cod))
    recv = ssl_clientSocket.recv(1024)

    # Verifica se est� OK
    status(recv)

    # Send RCPT TO command and print server response.
    rcptToCommand = 'RCPT TO: <'+ receiver + '>\r\n'
    ssl_clientSocket.send(bytes(rcptToCommand, cod))
    recv = ssl_clientSocket.recv(1024)

    # Verifica se est� OK
    status(recv)

    # Send DATA command and print server response.
    dataCommand = 'DATA\r\n'
    ssl_clientSocket.send(bytes(dataCommand, cod))
    recv = ssl_clientSocket.recv(1024)

    # Verifica se est� OK
    status(recv)

    # Enviando a mensagem

    ssl_clientSocket.send(bytes('From: ' + sender + '\r\n', cod))
    ssl_clientSocket.send(bytes('To: ' + receiver + '\r\n', cod))
    ssl_clientSocket.send(bytes('Cc: ' + cc + '\r\n', cod))
    ssl_clientSocket.send(bytes('Cco: ' + cco + '\r\n', cod))
    ssl_clientSocket.send(bytes('Subject: ' + subject + '\r\n', cod))
    ssl_clientSocket.send(bytes(message + '\r\n', cod))

    # Encerra a mensagem com apenas um ponto numa linha
    ssl_clientSocket.send(bytes('.\r\n', cod))
    recv = ssl_clientSocket.recv(1024)

    status(recv)

    # Fechando a conex�o
    quitCommand = 'QUIT\r\n'
    ssl_clientSocket.send(bytes(quitCommand,cod))
    recv = ssl_clientSocket.recv(1024)

    status(recv)
    


