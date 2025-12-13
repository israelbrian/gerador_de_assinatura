# Dockerfile do backend
FROM python:3.10-slim

# Variáveis de ambiente padrão do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY requirements.txt .
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