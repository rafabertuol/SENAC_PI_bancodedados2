FROM python:3.12.1

WORKDIR /app

COPY . .

# 1. pip install -r requirements.txt
RUN python3 -m pip install -r requirements.txt

# 2. pipx install poetry==1.8.3
RUN pipx install poetry==1.8.3

# 3. Modificar a variável de ambiente PATH para ter o poetry disponível globalmente
ENV PATH=/root/.local/bin:$PATH

# 4. Instalar dependências do projeto
RUN poetry config virtualenvs.create false; \
    poetry install --no-interaction --no-ansi