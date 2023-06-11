FROM python:3.10-slim

WORKDIR /menu_api

RUN pip install Flask Flask-restful Flask-SQLAlchemy Flask-Cors psycopg2-binary

COPY . .

CMD python server.py runserver 0.0.0.0:5000