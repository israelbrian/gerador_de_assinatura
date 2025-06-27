# Dockerfile do backend
FROM python:3.10-slim

# Definir variáveis de ambiente para proxy (PEGUE OS VALORES CORRETOS COM SUA EQUIPE DE TI)
ENV http_proxy=http://200.198.59.244:8080
ENV https_proxy=http://200.198.59.244:8080
ENV no_proxy=localhost,127.0.0.1,nginx 
# Adicione o nome do serviço nginx aqui

# Variáveis de ambiente padrão do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt .
# O 'pip config' pode ser necessário para o pip usar o proxy
RUN pip config set global.proxy $http_proxy
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Torna o seu entrypoint executável
# RUN chmod +x ./entrypoint.sh

# Expõe a porta que o Gunicorn vai usar internamente
EXPOSE 5000

# Define o entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# Define o comando PADRÃO que será passado para o entrypoint
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "app:app"]