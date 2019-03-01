from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class formulario(FlaskForm):

    texto = TextAreaField("texto" , validators = [DataRequired()])

class formu(FlaskForm):

    tag = TextAreaField("tag", validators= [DataRequired()])
