
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# set path to our python api file
ENV MODULE_NAME="rgapi.server"

# copy contents of project into docker
COPY ./ /app

# install poetry
RUN pip install -r requirements.txt
