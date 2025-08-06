# Gerador de assinatura de e-mail
`(front-end) Html, css, javascript / (back-end) python, flask, Pillow (PIL),`

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
|
|-- app.py                        // Arquivo principal do Flask, apenas com as rotas.
|-- data_validation.py            // Validar os dados recebidos do formulário.
|-- normalizer.py                 // Formatar os dados recebidos do formulário.
|-- signature_generator.py        // Gerar a imagem da assinatura.
|-- routes.py                     # Define todas as rotas (endpoints) da API.
|-- requirements.txt              # Dependências Python (Flask, Pillow, etc.).

|-- .dockerignore                 // Arquivos a serem ignorados ao construir a imagem Docker.
|-- docker-compose.yml            // Orquestra os serviços da aplicação (ex: app e nginx).
|-- Dockerfile                    // Instruções para construir a imagem Docker da aplicação Python.
|-- entrypoint.sh                 // Script executado quando o container inicia.
|-- package.json                  // Dependências e scripts do Node.js (para o front-end).
|-- package-lock.json             // Versões exatas das dependências do Node.js.
|-- .gitattributes                // Atributos de arquivos para o Git.
|-- .gitignore                    // Arquivos e pastas a serem ignorados pelo Git.
|-- README.md                     // Documentação do projeto (este arquivo).
|
|-- nginx/                        // Arquivos de configuração do Nginx (usado como reverse proxy).
|
|-- src/                          // Pasta contendo os arquivos de front-end.
|   |-- static/
|   |   |-- css/                  // Pasta para folhas de estilo CSS.
|   |       |-- output.css
|   |       └── style.css
|   |   |-- fonts/                // Contém as fontes usadas para gerar a assinatura.
|   |   |   |-- arial.ttf
|   |   |   |-- arialnb.ttf
|   |   |   └── ariblk.ttf
|   |   |-- icons/                // Ícones usados na interface.
|   |   |   └── icon-signature.png
|   |   |-- images/               // Imagens gerais da interface.
|   |   |   |-- default_signature.png
|   |   |   └── signature_example_ses.png
|   |   └── js/                   // Arquivos JavaScript para a lógica do client-side.
|   |       |-- apiService.js     // Lida com as chamadas para a API do back-end.
|   |       |-- formatter.js      // Funções para formatar dados no front-end em tempo real.
|   |       |-- script.js         // Script principal de que orquestra os outros scripts e armazena os dados do form.
|   |       |-- uiHandler.js      // Manipula os elementos da interface (UI).
|   |       └── validator.js      // Valida os dados no formulário antes do envio utilizando regex.
|   |
|   └── templates/
|       └── index.html            // Arquivo HTML principal da aplicação.
|
└── venv/                         // Pasta do ambiente virtual do Python (geralmente ignorada).

assinatura_app/
|-- app.py                  
|-- validacao_dados.py      
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
Todos os passos foram feitos pensando em método de organização de código limpo (clean code) e DRY (dont reapeat youself)
    
Histórico de desenvolvimento:

- Lógica de geração de assinatura Backend/ rotas de requisição / API 1.0 feito ✅
> Teste da rota /api método POST através do POSTMAN. ✅
- Reorganização da estrutura do projeto 
> Refatoração na nomenclatura das variáveis como um todo. ✅
> Criando consts para valores estáticos e Dicts para armazenar as fonts do projeto, cores, coordenadas da imagem e etc. ✅
> os.path adicionado para evitar erros de diretorio em diferentes maquinas (exemplo container docker/ servidor linux). ✅
- Criar o front-end onde o usuario possa preencher os campos mencionados em um formulario e ter o retorno da imagem na tela. ✅  
> Estilizar o formulario com Tailwindcss. Estilo 1.0 feito ✅ 
> Criar um estilo mais atraente, versatil e robusto focando em (mobile first e responsividade em diversas resoluções). Estilo 2.0 feito na branch feature-style-grayscale ✅ 
- Remover os comentarios feitos durante o desenvolvimento da aplicação. ✅
- Implementação da aplicação em um container docker.(Feito na branch feature-container-implementation ) ✅
> Configuração do docker-compose, .dockerignore e Dockerfile. 
> Implementar WSGI. ✅
> Gunicorn / NGINX. ✅
> Teste de deploy em um container docker. ✅

- Add um botão para "como usar" onde será baixado o manual descrevendo o passo a passo. ✅
- Implementar o nginx. ✅
- Deploy em container Docker institucional. ✅
- Deploy em uma servidor institucional (linux/nutanix). ✅

Refatoração 🎯:
- main.py -> apenas iniciar o projeto utilizar o (blueprints/routes) para separar a lógica do projeto em outros arquivos. ✅
- Estruturar melhor a lógica das pastas e arquivos em geral.✅
- Variáveis em inglês e camelcase. ✅
- Adicionar regex na validações do back-end. ✅ 
- Adicionar regex na validações do front-end. ✅
- Modularizar a logica em funções separadas em arquivos diferentes. ✅
- Orientação a objetos criando classes para cada funções no back e no front.

Esqueleto do front end:

    ```
    (Nome da aplicação / assessoria de tecnologia da informação).
        <Form>
          <dados a serem preenchidos>
            <button gerar imagem>
              <imagem é exibida na tela>
                <o botão "baixar imagem" e "como usar" fica disponivel abaixo da imagem gerada.>
    ```
             
```

Obs: 

Instalar as libs na venv (pip install -r .\requirements.txt)

(comando pra baixar as bibliotecas npm 'tailwind') npm init

adicionar ao app.py o seguinte comando para rodar localmente:
if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

comando para iniciar a compilação do tailwindcss:  
npx tailwindcss -i ./src/input.css -o ./static/css/output.css --watch  
comando para fazer antes do deploy no docker:  
npx tailwindcss -i ./src/input.css -o ./static/css/output.css --minify

docker:
docker compose up --build -d

```