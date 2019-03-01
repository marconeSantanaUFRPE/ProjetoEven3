
from datetime import datetime
import os
#Cria a pasta com data e hora atual e retorna dataehora
def criarPastaDataHora():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d%m%Y%H%M')
    #print(data_e_hora_em_texto)

    stringCriarPasta  = ('app\static\%s' % data_e_hora_em_texto)
    #print(stringCriarPasta)
    os.mkdir(stringCriarPasta)
                            
    stringCompac = ('app\static\%s' % data_e_hora_em_texto)
            

    return (stringCompac, data_e_hora_em_texto)