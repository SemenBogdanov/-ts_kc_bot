import psycopg2
from sqlalchemy import create_engine
from key import db_user, db_pass, db_ip, db_port, db_name


def db_connect(type):
    conn = None
    try:
        if type == 'psy':
            engine = psycopg2.connect(
                user=db_user,
                password=db_pass,
                host=db_ip.split(':')[0],
                port=db_port,
                dbname=db_name
            )
            return engine
        if type == 'alh':
            engine = create_engine(
                f'postgresql://{db_user}:{db_pass}@{db_ip.split(":")[0]}:5432/{db_name}'
            )
            return engine
    except (Exception, psycopg2.DatabaseError):
        print(psycopg2.DatabaseError)
        exit()
    return conn
