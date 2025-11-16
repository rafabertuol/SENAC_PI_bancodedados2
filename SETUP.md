## Rodando o projeto

Existe duas formas de rodar o projeto local na sua máquina ou dentro de um container docker

### Opção 1: Utilizando Docker (Recomendada)

> **Pré requisito**
> Ter o `docker` e `docker-desktop` instalado

docker-compose up

agora vá para http://localhost:8501

### Opção 2: local na sua máquina

> **Pre requisito**
> 1. Ter o python 3.12.1
> 2. Git

**Instalando dependencias do projeto**

1. pip install -r requirements.txt
2. pipx install poetry==1.8.3
3. Modificar a variável de ambiente PATH para ter o poetry
4. Digite `poetry --version` para validar se tudo ocorreu bem
5. Ative o ambiente virtual do poetry utilizando `poetry shell`
6. Instale as dependencias do projeto `poetry install`
7. Verifique se o streamlit está instalado com `streamlit --version`
8. Rode o projeto com o comando `streamlit run Homepage.py`

Acesse `http://localhost:8501` para visualizar os dashboard