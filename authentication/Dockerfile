FROM python:3

RUN pip3 install psycopg2

RUN pip3 install Flask

RUN pip3 install python-dotenv

EXPOSE 5001

COPY /resources/connection.py /
COPY /resources/postgres_functions.py /
COPY /authentication/token_generator.py /
COPY /authentication/authentication_db.py /
COPY /authentication/authentication_api.py /
COPY .env /

CMD python3 authentication_api.py