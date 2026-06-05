import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

FICHIER_REFERENCE = (
    DATA_DIR /
    "Tableur_Rationnement_Formulation(10).xlsx"
)

FICHIER_UTILISATEUR = (
    DATA_DIR /
    "Bibliotheque_Utilisateur.xlsx"
)

COLONNES = [
    "Catégorie",
    "Sous-catégorie",
    "Matière première",
    "MS",
    "UFL",
    "UFV",
    "PDIN",
    "PDIE",
    "MAT",
    "Amidon",
    "Sucres",
    "NDF",
    "ADF",
    "MG",
    "Ca",
    "P",
    "K",
    "Na",
    "Cout €/t"
]


def charger_reference():

    df = pd.read_excel(
        FICHIER_REFERENCE,
        sheet_name="Bibliothèque MP INRA"
    )

    mapping = {}

    for col in df.columns:

        col_clean = (
            str(col)
            .replace("%", "")
            .replace("/kg MS", "")
            .replace("(", "")
            .replace(")", "")
            .strip()
        )

        mapping[col] = col_clean

    df = df.rename(columns=mapping)

    return df


def creer_bibliotheque_utilisateur():

    if not FICHIER_UTILISATEUR.exists():

        pd.DataFrame(
            columns=COLONNES
        ).to_excel(
            FICHIER_UTILISATEUR,
            index=False
        )


def charger_utilisateur():

    creer_bibliotheque_utilisateur()

    return pd.read_excel(
        FICHIER_UTILISATEUR
    )


def sauvegarder_utilisateur(df):

    df.to_excel(
        FICHIER_UTILISATEUR,
        index=False
    )


def charger_bibliotheque_complete():

    df_ref = charger_reference()

    df_user = charger_utilisateur()

    df_ref["Source"] = "INRAE"

    df_user["Source"] = "Utilisateur"

    return pd.concat(
        [df_ref, df_user],
        ignore_index=True
    )


def ajouter_matiere_premiere(data):

    df = charger_utilisateur()

    df.loc[len(df)] = data

    sauvegarder_utilisateur(df)
