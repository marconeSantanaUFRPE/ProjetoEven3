from app import app
from flask import render_template , make_response ,request, redirect, url_for,flash
from app.models.forms import formulario,formu
from app.models.tratamentoString import tratamentoStringListaParticipantes,tagsDoCracha
import os
from werkzeug.utils import secure_filename
from app.controllers.pastas import criarPastaDataHora
from app.controllers.tags import verificaTagsTextoPlanilha
from app.controllers.criarCrachas import criarCrachasPastaZip

UPLOAD_FOLDER = 'app\static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
BackGroudLogo = ""
LOGO = ""

@app.route("/" , methods = ["GET","POST"])
def Max():
        
        exemplo = "Exemplo: {{Nome}},{{Email}}"
        form = formulario()
        formularioTags = formu()
        
        if formularioTags.validate_on_submit():

                textoForm = formularioTags.tag.data
                tags = tagsDoCracha(textoForm)   
        
        if form.validate_on_submit():
              
                a = criarPastaDataHora()
                stringCompac = a[0]
                data_e_hora_em_texto = a[1]

                listaDeIntegrantes = tratamentoStringListaParticipantes(form.texto.data)
                tagsdaPlanilha = listaDeIntegrantes[1]
                listaDados = listaDeIntegrantes[0]

                tagsveri = verificaTagsTextoPlanilha(tags,tagsdaPlanilha)
                if tagsveri == False:
                         return render_template("Erro.html")

                criarCrachasPastaZip(listaDados,tags,tagsdaPlanilha,data_e_hora_em_texto,stringCompac)                    
              
                return redirect(url_for('static', filename='pastaCompac.zip'))
                
        return render_template('index.html' , form=form, formularioTags = formularioTags,exemplo = exemplo)

        
@app.route('/pdf/<string>')
def pdf_template2(string):
        
        string = string.replace("<","" )
        string = string.replace(">","" )
        lista = string.split(",")
        
        a = BackGroudLogo
        b = LOGO

        if b == "":
                return render_template("crachaPadrao.html", lista = lista, a  = a)
        else:
                return render_template("crachaComLogo.html", lista = lista, a  = a , b = b  )
        

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/carregar', methods=['GET', 'POST'])
def upload_file():
        
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
                
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
                global BackGroudLogo 
                BackGroudLogo = filename
                
                return render_template("MostrarImagemCarregada.html" , a = filename)
                
    
    return render_template('carregarImagem.html')


@app.route('/carregarLogo', methods=['GET', 'POST'])
def upload_fileLogo():
        
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
                
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                global LOGO 
                LOGO = filename
                
                return render_template("MostrarImagemCarregadaLogo.html" , a = filename)
                
    return render_template('carregarLogo.html')