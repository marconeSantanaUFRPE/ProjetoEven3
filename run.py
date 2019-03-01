from app import app

app.config['SECRET_KEY'] = 'chave-de-seguranca'


if __name__ == "__main__":
    app.run()