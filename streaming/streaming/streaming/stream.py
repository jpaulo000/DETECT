# Fun��o que trata um item da API. Algumas vezes a requisi��o n�o poder� ser feita, e a fun��o n�o ir� retornar uma 
# mensagem de erro, mas um objeto vazio.

import streaming.track as track
import sendEmail.sendEmail as email
import os
import time
import shutil

def return_item(item, variable):
    temp_item = item[variable] if variable in item else None
        
    if temp_item is None:
        return ''
    else:
        return str(temp_item)
    
def create_csv():  
    csv = open(track.getPath(), 'w', encoding="utf-8" )
    csv.write(track.getHeader())
    return csv

def generate_rows(item, s, csv):
    # Cria��o das vari�veis dos dados
    id_str = return_item(item, 'id_str')
    text = return_item(item, 'text')
    geo = return_item(item, 'geo')
    created_at = return_item(item, 'created_at')
    in_reply_to_status_id_str = return_item(item, 'in_reply_to_status_id_str')
    user_id = return_item(item, 'user_id')
    follower_count = return_item(item, 'follower_count')
    retweet_count = return_item(item, 'retweet_count')
    
    # Tratamento dos tweets: retira os par�grafos e retweets para melhor leitura dos tweets em outros sistemas
    text = text.replace("\r"," ")
    text = text.replace("\n"," ")
    text = text.replace("\"","")
    text = text.replace("\'","")
    retweet_checker = text[0:2]    
    
    # Verifica se existe elemento nulo para o id. Caso exista, a linha ser� ignorada
    if id_str != '' and retweet_checker != 'RT':
        # Gera a linha do CSV 
        row = str((id_str + s +
              '\"' +  text + '\"' + s + 
              geo + s + 
              created_at + s + 
              in_reply_to_status_id_str + s + 
              user_id + s + 
              follower_count + s +
              retweet_count + '\n')) 
        
        # Insere a linha no arquivo csv definido em track.getPath      
        csv.write(str(row))

#Fun��o para gerenciar o arquivo csv. Serve para dividir o arquivo a cada 250MB, criar uma nova pasta para este arquivo
#e enviar um log para o sendEmail.        
def manage_csv(csv, check):
    bar = '/'
    #Verifica o tamanho do arquivo definido em track
    size = os.path.getsize(track.getPath()) 
    
    #Define o nome da nova pasta a ser criada com o arquivo de backup
    date = time.strftime("%d-%m-%Y_%Hh%Mmin%Ss")
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")    
    path = (track.getBackupPath() + date + '/') 
    
    if size >= 262144000 or check == 1:
        #Cria��o de uma nova pasta
        os.mkdir(path)
        
        #Copia o arquivo para a nova pasta
        shutil.copy(track.getPath(), path)
        
        #Renomeia o arquivo para a data na qual foi gerado.
        old = (path + bar + 'actual.csv')
        new = (path + bar + date + '.csv')
        os.renames(old, new)
        
        #Fecha o arquivo atual antigo e o remove. Um novo arquivo � criado a partir de uma chamada da fun��o create_csv
        #na fun��o principal
        csv.close()
        os.remove(track.getPath())
        
        if size >= 262144000:            
            email.sendEmail(0,new)        
        
        #Retorna verdadeiro se toda esta opera��o fora concluida com sucesso         
        return True
    
    elif int(hour) % 4 == 0 and (int(minute)+int(second)) == 0:
        email.sendEmail(1,"")
        return False       
    
    else: 
        return False           
             
        
    