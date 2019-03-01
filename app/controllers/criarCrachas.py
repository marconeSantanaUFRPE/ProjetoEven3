import pdfkit
from shutil import make_archive

def criarCrachasPastaZip(listaDados,tags,tagsdaPlanilha,data_e_hora_em_texto,stringCompac):                   
    contador = 0 
    for x in listaDados:
        string = ""
        contador += 1
        cont = str(contador)
        for y in tags:
            if y in tagsdaPlanilha:
                    string+=x[y] + ","
                    stringEnderecoSalvar = ('app\static\%s\Cracha-%s.pdf'  % (data_e_hora_em_texto,cont))
                    #print(stringEnderecoSalvar)
                    pdfkit.from_url('http://127.0.0.1:5000/pdf/<'+string+'>', stringEnderecoSalvar)

    make_archive('app\static\pastaCompac','zip',stringCompac)