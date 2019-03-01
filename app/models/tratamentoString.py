#Tratamento da string das caixas de texto da pagina web
#trata a string e retorna uma lista
#com todos os participantes e as Tags 

def tratamentoStringListaParticipantes(texto):
    
    textoInformacao = texto.split("\r\n")
    tags = textoInformacao[0].split("\t")
        
    textoInformacao = textoInformacao[1::]

    retorno=[]
    for x in textoInformacao:
        dic = {}
        lista = x.split("\t")    
        try:
            for y in range(len(tags)):
                
                ## Removendo a / ou \ das informações da erro na hora de criar os crachas ##
                a = lista[y]
                b = a.replace("/","")
                c = b.replace("/","")

                dic[tags[y]] = c
            retorno.append(dic)
        except:
            pass
  
    return (retorno, tags)

def tagsDoCracha(texto):
    aux = texto.replace(" ", "")
    aux = aux.replace("{{","")
    aux = aux.replace("}}","")
    lista = aux.split(",")

    return lista


def tirarMaiorMenor(string):

    string = string.replace("<","" )
    string = string.replace(">","" )
    lista = string.split(",")

    return lista