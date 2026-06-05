import streamlit as st
import pandas as pd

from modules.database import (
    charger_bibliotheque_complete,
    ajouter_matiere_premiere
)

st.title("📚 Bibliothèque MP")

df = charger_bibliotheque_complete()

st.subheader("Recherche")

recherche = st.text_input(
    "Nom matière première"
)

if recherche:

    df = df[
        df["Matière première"]
        .astype(str)
        .str.contains(
            recherche,
            case=False,
            na=False
        )
    ]

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

st.subheader(
    "Ajouter une matière première"
)

with st.form("ajout_mp"):

    categorie = st.text_input(
        "Catégorie"
    )

    sous_categorie = st.text_input(
        "Sous-catégorie"
    )

    mp = st.text_input(
        "Matière première"
    )

    ms = st.number_input("MS")

    ufl = st.number_input("UFL")

    ufv = st.number_input("UFV")

    pdin = st.number_input("PDIN")

    pdie = st.number_input("PDIE")

    mat = st.number_input("MAT")

    amidon = st.number_input(
        "Amidon"
    )

    sucres = st.number_input(
        "Sucres"
    )

    ndf = st.number_input(
        "NDF"
    )

    adf = st.number_input(
        "ADF"
    )

    mg = st.number_input(
        "MG"
    )

    ca = st.number_input(
        "Ca"
    )

    p = st.number_input(
        "P"
    )

    k = st.number_input(
        "K"
    )

    na = st.number_input(
        "Na"
    )

    cout = st.number_input(
        "Cout €/t"
    )

    submit = st.form_submit_button(
        "Ajouter"
    )

    if submit:

        ajouter_matiere_premiere([
            categorie,
            sous_categorie,
            mp,
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
        ])

        st.success(
            "Matière première ajoutée"
        )

        st.rerun()
