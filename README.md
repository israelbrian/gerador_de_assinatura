# Gerador de assinatura de e-mail teste
`(front-end) Html, css, javascript / (back-end) python, flask, Pillow (PIL),`

------------------------

Receber as seguintes informações da assinatura (via form):
```
Nome (obrigatório)
Cargo (obrigatório)
Orgão dentro da Secretaria	
Telefone Fixo (obrigatório)
Telefone Celular (opcional)	
e-mail no Governo (obrigatório)
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
    
App.py -> focado em receber os dados do user (chamar as funções para 'validar' 'normalizar' 'gerar_assinatura') e devolver a imagem gerada para o front (onde haverá outra manipulações de como a imagem será tratada).
    
Foi feita a declaração de consts para os valores estaticos foi adicionado o os.path para evitar erros de diretorio em diferentes maquinas (exemplo container docker)
Foi feita uma organização mais limpa e clara das variáveis, criando consts para valores estaticos e dicts para armazenar as fonts do projeto, cores, coordenadas da imagem e etc.
Foi adicionado o os.path.join no caminho das fontes / imagem para evitar erros no deploy no docker.

Todos os passos foram feitos pensando em:
- Método de organização de código limpo (clean code) e DRY (dont reapeat youself)

- Backend/ API 1.0 feito ✅
- Criar o frontend onde o usuario possa preencher os campos mencionados em um formulario e ter o retorno da imagem na tela. ✅  
- Estilizar o formulario com tailwind. ✅ 

```
comando para iniciar a compilação do tailwindcss:  
npx tailwindcss -i ./src/input.css -o ./static/css/output.css --watch  
comando para fazer antes do deploy no docker:  
npx tailwindcss -i ./src/input.css -o ./static/css/output.css --minify

```

Proximo passo 🎯:

- Criar um estilo mais atraente, versatil e robusto.
- Deploy em um container docker.


Esqueleto do front end:

    ```
    (Informações importantes sobre quais dados preencher e afins).
        <Form>
          <dados a serem preenchidos>
            <button gerar imagem>
              <imagem é exibida na tela>
                <o botão baixar imagem fica disponivel abaixo da imagem gerada.>
    ```

Instalar as libs na venv (pip install -r .\requirements.txt)                
