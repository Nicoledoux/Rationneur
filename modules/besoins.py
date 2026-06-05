import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from modules.besoins import (
    RACES,
    poids_vif,
    production_lait,
    besoins_ufl,
    besoins_pdi
)

st.set_page_config(
    page_title="Besoins INRAE",
    layout="wide"
)

st.title("🐄 Besoins INRAE")

st.markdown("---")

# ==========================
# SAISIE
# ==========================

col1, col2 = st.columns(2)

with col1:

    race = st.selectbox(
        "Race",
        list(RACES.keys())
    )

    nec = st.selectbox(
        "Note d'état corporel (NEC)",
        [2.0, 2.5, 3.0, 3.5, 4.0],
        index=2
    )

    lactation = st.selectbox(
        "Numéro de lactation",
        [1, 2, 3, 4, 5]
    )

with col2:

    dim = st.number_input(
        "Jours en lait (DIM)",
        min_value=1,
        max_value=400,
        value=100
    )

    gestation = st.number_input(
        "Mois de gestation",
        min_value=0,
        max_value=9,
        value=0
    )

# ==========================
# CALCULS
# ==========================

pv = poids_vif(race, nec)

tb = RACES[race]["tb"]
tp = RACES[race]["tp"]

lait = production_lait(
    race,
    lactation,
    dim,
    nec,
    gestation
)

ufl = besoins_ufl(
    race,
    lactation,
    dim,
    nec,
    gestation
)

pdi = besoins_pdi(
    race,
    lactation,
    dim,
    nec,
    gestation
)

st.markdown("---")

# ==========================
# INDICATEURS
# ==========================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Poids vif",
        f"{pv:.0f} kg"
    )

with c2:
    st.metric(
        "TB",
        f"{tb:.1f}"
    )

with c3:
    st.metric(
        "TP",
        f"{tp:.1f}"
    )

with c4:
    st.metric(
        "Production laitière",
        f"{lait:.1f} kg/j"
    )

st.markdown("---")

# ==========================
# TABLEAU UFL
# ==========================

st.subheader("Besoins énergétiques (UFL)")

df_ufl = pd.DataFrame({
    "Poste": [
        "Entretien",
        "Production",
        "Croissance",
        "Gestation",
        "TOTAL"
    ],
    "UFL": [
        ufl["entretien"],
        ufl["production"],
        ufl["croissance"],
        ufl["gestation"],
        ufl["total"]
    ]
})

st.dataframe(
    df_ufl,
    use_container_width=True,
    hide_index=True
)

# ==========================
# TABLEAU PDI
# ==========================

st.subheader("Besoins protéiques (PDI)")

df_pdi = pd.DataFrame({
    "Poste": [
        "Entretien",
        "Production",
        "Croissance",
        "Gestation",
        "TOTAL"
    ],
    "PDI (g)": [
        pdi["entretien"],
        pdi["production"],
        pdi["croissance"],
        pdi["gestation"],
        pdi["total"]
    ]
})

st.dataframe(
    df_pdi,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================
# GRAPHIQUE UFL
# ==========================

col1, col2 = st.columns(2)

with col1:

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df_ufl["Poste"],
            y=df_ufl["UFL"]
        )
    )

    fig.update_layout(
        title="Répartition des besoins UFL"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig2 = go.Figure()

    fig2.add_trace(
        go.Bar(
            x=df_pdi["Poste"],
            y=df_pdi["PDI (g)"]
        )
    )

    fig2.update_layout(
        title="Répartition des besoins PDI"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

# ==========================
# EXPORT
# ==========================

resultats = pd.DataFrame({
    "Indicateur": [
        "Race",
        "Poids vif",
        "TB",
        "TP",
        "Lait",
        "UFL total",
        "PDI total"
    ],
    "Valeur": [
        race,
        pv,
        tb,
        tp,
        lait,
        ufl["total"],
        pdi["total"]
    ]
})

csv = resultats.to_csv(index=False)

st.download_button(
    "📥 Export CSV",
    csv,
    "besoins_inrae.csv",
    "text/csv"
)
