path = '/home/jpaulo/server/csv/actual.csv'
backupPath = '/home/jpaulo/server/csv/backups/'

def getTrack():
    s = ","
    return  ("o" + s + 
            "a" + s + 
            "os" + s + 
            "as" + s + 
            "um" + s + 
            "uma" + s + 
            "uns" + s + 
            "umas" + s + 
            "ao" + s + 
            "aos" + s + 
            "de" + s + 
            "do" + s + 
            "da" + s + 
            "dos" + s + 
            "das" + s + 
            "em" + s + 
            "no" + s + 
            "na" + s + 
            "nos" + s + 
            "nas" + s + 
            "por" + s + 
            "pelo" + s + 
            "pela" + s + 
            "pelos" + s + 
            "pelas" + s + 
            "que" + s + 
            "ele" + s + 
            "ela" + s + 
            "eles" + s + 
            "elas" + s + 
            "q" + s + 
            "pq" + s + 
            "eu" + s + 
            "tu" + s + 
            "ele" + s + 
            "nos" + s + 
            "vos" + s + 
            "eles" + s +
            "ser" + s +
            "ter" + s +
            "fazer" + s +
            "estar" + s +
            "ficar" + s +
            "dar" + s +
            "haver" + s +
            "isto" + s +
            "isso" + s +
            "aquilo" + s +
            "aquela" + s +
            "aquele" + s +
            "dele" + s +
            "dela" + s +
            "com" + s +
            "como" + s +
            "assim" + s +
            "tipo" + s +
            "for" + s +
            "tenho" + s +
            "mas" + s +
            "mais" + s +
            "qual" + s +
            "quem" + s +
            "exceto" + s +
            "fui" + s +
            "estava" + s +
            "você" + s +
            "vocês" + s +
            "vc" + s +
            "tudo" + s +
            "então" + s +
            "tão" + s +
            "tanto" + s +
            "também" + s +
            "nenhum" + s +
            "nenhuma" + s +
            "lá" + s +
            "quando" + s +
            "algum" + s +
            "alguma" + s +
            "alguns" + s +
            "algumas")
    
def getPath():
    return path

def getBackupPath():
    return backupPath

def getHeader():
    s = ";"
    header = ('id_str' + s + 
              'text' + s +
              'geo' + s +
              'created_at' + s +
              'user_id' + s +
              'in_reply_to_status_id_str' + s +
              'follower_count' + s +
              'retweet_count')
    return header    