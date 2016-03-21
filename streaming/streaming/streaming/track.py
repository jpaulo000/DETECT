path = '/home/servidor/stream/actual.csv'
backupPath = '/home/servidor/stream/backups/'

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
            "eles")
    
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
              'in_reply_to_status_id_str' + s +
              'follower_count' + s +
              'retweet_count')
    return header    