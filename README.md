# Gerador de assinatura de e-mail
`(front-end) Html, css, javascript / (back-end) python, flask, Pillow (PIL),`

Instalar as libs na venv (pip install -r .\requirements.txt)
------------------------

Receber as seguintes informações da assinatura (via form):
```
Nome (obrigatório)
Cargo (obrigatório)
Orgão dentro da Secretaria (obrigatório)
Telefone Fixo (obrigatório)
Telefone Celular (opcional)	
e-mail institucional (obrigatório)
andar(obrigatório)
```
------------------------

## Estrutura do projeto:

```
assinatura_app/
|-- app.py                  // Arquivo principal do Flask, apenas com as rotas.
|-- validacao_dados.py      // Função para validar os dados recebidos
|-- normalizacao.py         // Função para normalizar os dados(lowercase, upper, captalize)
|-- gerador_assinatura.py   // Função para gerar a imagem nos padrões pré-determinados
├── static/
│   ├── assinatura_padrao.PNG # A imagem de fundo da assinatura
│   ├── styles.css
│   ├── arial.ttf 
│   ├── arialnb.ttf 
│   └── arialbd.ttf
├── templates/
│   └── index.html
└── requirements.txt
```


Todas as funções do app foram migradas para arquivos externos melhorando a legibilidade do projeto como um todo e de sua logica.
    
App.py -> Focado apenas em inicializar o projeto e ser um orquestrador das rotas.

Api.py - > Focado em receber os dados do user e chamar as funções 'validateData' (valida se os campos foram preenchido de forma correta), 'normalizeData'(manipula o texto para uppercase, lowercase e etc) e 'signatureGenerator' (onde é feita a lógica de 'impressão' dos dados do usuario na 'assinatura_pradrao_ses')

Após executar as funções a rota /api devolve a imagem gerada para o front (onde há outras manipulações de como a imagem será tratada).
    
Foi feita a declaração de consts para os valores estaticos foi adicionado o os.path para evitar erros de diretorio em diferentes maquinas (exemplo container docker)
Foi feita uma organização mais limpa e clara das variáveis, criando consts para valores estaticos e dicts para armazenar as fonts do projeto, cores, coordenadas da imagem e etc.
Foi adicionado o os.path.join no caminho das fontes / imagem para evitar erros no deploy no docker.

Todos os passos foram feitos pensando em:
- Método de organização de código limpo (clean code) e DRY (dont reapeat youself)

Finalizei as seguintes etapas de forma satisfatorias:
- Backend/ rotas de requisição / API 1.0 feito ✅
- Criar o frontend onde o usuario possa preencher os campos mencionados em um formulario e ter o retorno da imagem na tela. ✅  
- Estilizar o formulario com Tailwindcss. ✅ 
- Criar um estilo mais atraente, versatil e robusto focando em (mobile first e responsividade em diversas resoluções). ✅ 
- Remover os comentarios feitos durante o desenvolvimento da aplicação. ✅
- Configuração do docker-compose, .dockerignore e Dockerfile. ✅
- Implementar WSGI. ✅
- Gunicorn. ✅
- Teste de deploy em um container docker. ✅
- Add um botão para "Add a assinatura no e-mail" onde será baixado o manual descrevendo o passo a passo. ✅
- Implementar o nginx. ✅
- Deploy em container Docker institucional. ✅

Proximo passo 🎯:
Colocar a aplicação online em uma maquina virtual institucional.

Refatoração 🎯:
- O arquivo main.py deve só iniciar o projeto (utilizar o routes "blueprints" para separar a lógica do projeto em outros arquivos). ✅
- Estruturar melhor a lógica das pastas e arquivos em geral.✅
- Variáveis em inglês e camelcase. ✅
- Adicionar regex na validações do back-end. ✅ 
- Adicionar regex na validações do front-end. 
- Orientação a objetos criando classes para cada funções no back e no front.
- Cada função deve ter uma ação (separar funções em arquivos diferentes).

Esqueleto do front end:

    ```
    (Nome da aplicação / assessoria de tecnologia da informação).
        <Form>
          <dados a serem preenchidos>
            <button gerar imagem>
              <imagem é exibida na tela>
                <o botão baixar imagem fica disponivel abaixo da imagem gerada.>
                  <o botão "com usar" fica disponivel ao lado.>
    ```

             
```
Obs: 

Antes do deploy lembrar de ...

desativar modo de debbug do flask

comando para iniciar a compilação do tailwindcss:  
npx tailwindcss -i ./src/input.css -o ./static/css/output.css --watch  
comando para fazer antes do deploy no docker:  
npx tailwindcss -i ./src/input.css -o ./static/css/output.css --minify

docker:
docker compose up --build -d

```