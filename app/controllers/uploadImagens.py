#.py Para carregar Imagem de Fundo e Logo (Opcional)


import os
from app import app
from flask import request,redirect
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'app\static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def carregarImagem():
    filename  = None
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):   
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
    return filename