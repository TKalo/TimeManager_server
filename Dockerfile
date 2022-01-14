FROM python:3

RUN pip3 install psycopg2

RUN pip3 install Flask

RUN pip3 install python-dotenv

EXPOSE 7000

COPY /idb/user_idb.py /
COPY /postgres_db/connection.py /
COPY /postgres_db/postgres_functions.py /
COPY /postgres_db/user_db.py /
COPY /api/user_api.py /
COPY .env /

CMD python3 user_api.py