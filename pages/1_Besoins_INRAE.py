import streamlit as st
import pandas as pd

from modules.besoins import (
    RACES,
    poids_vif,
    production_lait,
    besoins_ufl,
    besoins_pdi
)

st.title("🐄 Besoins INRAE")

col1, col2 = st.columns(2)

with col1:
    race = st.selectbox(
        "Race",
        list(RACES.keys())
    )

    nec = st.selectbox(
        "NEC",
        [2.0, 2.5, 3.0, 3.5, 4.0],
        index=2
    )

    lactation = st.selectbox(
        "Lactation",
        [1, 2, 3, 4, 5]
    )

with col2:
    dim = st.number_input(
        "DIM",
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
    
    temperature = st.number_input(
    "Température moyenne (°C)",
    min_value=-10,
    max_value=50,
    value=20
    )

    humidite = st.number_input(
    "Humidité (%)",
    min_value=0,
    max_value=100,
    value=60
    )

pv = poids_vif(race, nec)

lait = production_lait(
    race,
    lactation,
    dim,
    nec,
    gestation
)
# Estimation ingestion MS
ingestion_ms = (
    0.025 * pv
    + 0.10 * lait
)

# Besoin en eau
eau_base = (
    4 * lait
    + 4 * ingestion_ms
)

correction_temperature = max(
    0,
    (temperature - 20) * 2
)

eau_totale = (
    eau_base
    + correction_temperature
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

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Poids vif",
        f"{pv:.0f} kg"
    )

with c2:
    st.metric(
        "Production laitière",
        f"{lait:.1f} kg"
    )

with c3:
    st.metric(
        "UFL totales",
        f"{ufl['total']:.2f}"
    )

st.markdown("---")

df = pd.DataFrame({
    "Poste": [
        "Entretien",
        "Production",
        "Croissance",
        "Gestation",
        "Total"
    ],
    "UFL": [
        ufl["entretien"],
        ufl["production"],
        ufl["croissance"],
        ufl["gestation"],
        ufl["total"]
    ],
    "PDI": [
        pdi["entretien"],
        pdi["production"],
        pdi["croissance"],
        pdi["gestation"],
        pdi["total"]
    ]
})

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
