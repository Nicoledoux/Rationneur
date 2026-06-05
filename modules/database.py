import sqlite3
import pandas as pd

DB_NAME = "rationneur.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS matieres_premieres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categorie TEXT,
        sous_categorie TEXT,
        matiere_premiere TEXT UNIQUE,
        ms REAL,
        ufl REAL,
        ufv REAL,
        pdin REAL,
        pdie REAL,
        mat REAL,
        amidon REAL,
        sucres REAL,
        ndf REAL,
        adf REAL,
        mg REAL,
        ca REAL,
        p REAL,
        k REAL,
        na REAL,
        cout REAL
    )
    """)

    conn.commit()
    conn.close()


def lire_mp():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM matieres_premieres",
        conn
    )

    conn.close()

    return df


def ajouter_mp(data):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO matieres_premieres(
        categorie,
        sous_categorie,
        matiere_premiere,
        ms,
        ufl,
        ufv,
        pdin,
        pdie,
        mat,
        amidon,
        sucres,
        ndf,
        adf,
        mg,
        ca,
        p,
        k,
        na,
        cout
    )
    VALUES(
        ?,?,?,?,?,?,?,?,?,?,
        ?,?,?,?,?,?,?,?,?
    )
    """, data)

    conn.commit()
    conn.close()
