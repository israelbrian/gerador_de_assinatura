# Gerador de assinatura de e-mail
## (front-end) Html, css, javascript 
## (back-end) python, flask, Pillow (PIL),
font: Calibri (Corpo)
size: 11

Instalar as libs na venv (pip install -r .\requirements.txt)
------------------------

receber as seguintes informações da assinatura (via form):
Nome (obrigatório)
Cargo (obrigatório): 
Secretaria (obrigatório):
Orgão dentro da Secretaria:	
Telefone Fixo  (obrigatório):
Telefone Celular:	
e-mail no Governo (obrigatório):	nonomonom@nomonomon.mg.gov.br
Endereço do trabalho (obrigatório):	
andar(obrigatório):

------------------------

estrutura do projeto:
assinatura_app/
|-- app.py              # Nosso código Flask
├── static/
│   ├── assinatura_padrao.PNG # A imagem de fundo da assinatura
│   |── styles.css
│   └── calibri.ttf
├── templates/
│   └── index.html
└── requirements.txt

|-- Calibri (Corpo).ttf           # O arquivo da fonte que vamos usar
