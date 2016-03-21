__author__ = 'jpaul_000'
import os

def status(recv):
    situation = str(recv[:3], 'utf-8')
    if situation == "220":
        print('Conexao com servidor SMTP foi estabelecida com sucesso (Codigo 220)')
    elif situation == "221":
        print('Conexao com servidor SMTP foi encerrada (Codigo 221)')
    elif situation == "235":
        print('Autenticacao realizada com sucesso. (Codigo 235)')
    elif situation == "250":
        print('O servidor SMTP aceitou o pedido requisitado pelo cliente. (Codigo 250)')
    elif situation == "502":
        print('Comando nao-implementado. (Codigo 502)')
    elif situation == "334":
        print('Autenticacao necessaria. (Codigo 334)')
    elif situation == "354":
        print('O servidor SMTP espera uma resposta do cliente. (Codigo 354)')
    elif situation == "530":
        print('Acesso negado pelo servidor SMTP para esta acao, autenticacao necessaria. (Codigo 530)')
    elif situation == "535":
        print('Acesso negado pelo servidor SMTP para esta acao, verifique o login e/ou senha (Codigo 535)')
        
def getSubject(messageType):
    if messageType == 0: 
        subject = 'Servidor: arquivo gerado com sucesso'    
    elif messageType == 1:
        subject = 'Situacao do servidor'  
    else:
        subject = 'Erro no servidor'
        
    return subject

def getMessage(messageType, var):
    if messageType == 0:        
        message = ('Ola\n' + 
               'O servidor acaba de criar um novo arquivo totalizando ' + str(os.path.getsize(var)) + 'bytes.' + 
               '\n\n' + 
               'A quantidade de tweets no arquivo e de ' + str(countRows(var)) + '\n' + 
               'Nos iremos mante-lo informado sobre mais novidades.\n' + 'Abracos.\n')
    
    elif messageType == 1:
        message = ('Ola\n' + 
               'O servidor esta funcionando normalmente!' + 
               '\n\n' + 
               'Nos iremos mante-lo informado sobre mais novidades.\n' + 'Abracos.\n')
    
    else:
        message = ('Ola\n' + 
               'O servidor permaneceu inativo por um periodo de ' + str(var) + ' (hmm). Apesar disto,' + 
               'o servidor voltou a operar normalmente a partir do envio deste email. O arquivo atual' +
	       'foi movido para uma pasta nova com segurança.' + 
               '\n\n' + 
               'Nos iremos mante-lo informado sobre mais novidades.\n' + 'Abracos.\n')
    
    return message 
               
               
def countRows(filePath):
    count = 0
    with open (filePath, 'rb') as f:
        for line in f:
            count += 1
            line
            
    f.close()
    return count
