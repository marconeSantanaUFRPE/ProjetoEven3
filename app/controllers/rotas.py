#Classe com as rotas da aplicação

import os
from flask import render_template , make_response ,request, redirect, url_for,flash
from werkzeug.utils import secure_filename

from app import app
from app.models.forms import formulario,formu
from app.models.tratamentoString import tratamentoStringListaParticipantes,tagsDoCracha,tirarMaiorMenor
from app.controllers.pastas import criarPastaDataHora
from app.controllers.tags import verificaTagsTextoPlanilha
from app.controllers.criarCrachas import criarCrachasPastaZip
from app.controllers.uploadImagens import carregarImagem

BackGround = None
LOGO = None

@app.route("/" , methods = ["GET","POST"])
def Max():
        
        exemplo = "Exemplo: {{Nome}},{{Email}}"
        form = formulario()
        formularioTags = formu()
        
        if formularioTags.validate_on_submit():

                textoForm = formularioTags.tag.data
                tags = tagsDoCracha(textoForm)   
        
        if form.validate_on_submit():
              
                stringDataHora_StringCompactar = criarPastaDataHora()
                stringCompac = stringDataHora_StringCompactar[0]
                dataHoraTexto = stringDataHora_StringCompactar[1]

                listaDeIntegrantes = tratamentoStringListaParticipantes(form.texto.data)
                tagsdaPlanilha = listaDeIntegrantes[1]
                listaDados = listaDeIntegrantes[0]

                tagVerificasdas = verificaTagsTextoPlanilha(tags,tagsdaPlanilha)
                if tagVerificasdas == False:
                         return render_template("Erro.html")
                global BackGround
                if BackGround == None:
                        return render_template('ErroSemBack.html')

                criarCrachasPastaZip(listaDados,tags,tagsdaPlanilha,dataHoraTexto,stringCompac)                    
              
                return redirect(url_for('static', filename='pastaCompac.zip'))
                
        return render_template('index.html' , form=form, formularioTags = formularioTags,exemplo = exemplo)

        
@app.route('/pdf/<string>')
def pdf_template2(string):
        
        lista = tirarMaiorMenor(string)
        
        a = BackGround
        b = LOGO
          
        if b == None:
                return render_template("crachaPadrao.html", lista = lista, a  = a)
        else:
                return render_template("crachaComLogo.html", lista = lista, a  = a , b = b  )
        
@app.route('/carregar', methods=['GET', 'POST'])
def upload_file():
        nomeDoArquivo = None
        nomeDoArquivo = carregarImagem()
        global BackGround 
        BackGround = nomeDoArquivo
        
        if nomeDoArquivo != None:    
                return render_template("MostrarImagemCarregada.html" , a = nomeDoArquivo)
        return render_template('carregarImagem.html')

@app.route('/carregarLogo', methods=['GET', 'POST'])
def upload_fileLogo():  
        nomeDoArquivo = None
        nomeDoArquivo = carregarImagem()   
        global LOGO 
        LOGO = nomeDoArquivo
        
        if nomeDoArquivo != None:        
                return render_template("MostrarImagemCarregadaLogo.html" , a = nomeDoArquivo)
        return render_template('carregarLogo.html')