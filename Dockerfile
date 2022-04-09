FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

RUN chmod +x 'scripts/backend_entrypoint.sh'
CMD run backend_entrypoint.sh