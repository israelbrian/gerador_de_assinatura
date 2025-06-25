#!/bin/sh

set -e

echo "Entrypoint: Ambiente preparado. Nenhuma migração necessária por enquanto."
# No futuro, se você adicionar um banco de dados com Flask-Migrate, o comando viria aqui:
# flask db upgrade

echo "Entrypoint: Iniciando o servidor Gunicorn..."
exec "$@"