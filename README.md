# ProjetoEven3
Projeto para Seleção de Estágio da Even3



1 - Instalação do Python 3

    instalador disponível em:
    https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe
    Configure o python nas variáveis de ambiente (PATH) - https://python.org.br/instalacao-windows/

2 - Instalação/Inicialização virtualenv

     Instalação
     Com o python configurado nas variáveis de ambiente execute o comando:
     >pip3 install virtualenv
     Iniciar
     Navegue até a pasta venv\Scripts do projeto e execute o comando activate
     \venv\Scripts>activate
3 - Instalar bibliotecas 

    com a venv ativada executar o comando na pasta raiz do Projeto '\ProjetoEven3'
     
      > pip3 install -r requirements.txt
      aguarde a instalação das bibliotecas 
4 - Instalando o pdfkit

    a instalação da biblioteca pdfkit precisa do wkhtmltopdf disponível em : https://wkhtmltopdf.org/downloads.html

    instale e configure o wkhtmltopdf nas variaveis de ambiente (PATH) - adicione ao PATH (C:\Program Files\wkhtmltopd\bin)->local onde o wkhtmltopdf é instalado
        
    

5 - Iniciar Aplicação

    com a venv ativada e na pasta raiz do projeto execute o arquivo run.py com o comando:
    > python run.py
    
6 - acessar aplicação.
 
    no navegador acesse http://localhost:5000/

# Requisitos não atendidos

Requisito - 3

    Deverá permitir as opções de negrito, itálico e ajustar o tamanho do texto.
