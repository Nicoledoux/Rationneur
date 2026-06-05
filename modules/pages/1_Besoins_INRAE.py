import math

RACES = {
    "Holstein": {
        "pv": 650,
        "tb": 38.5,
        "tp": 31.2,
        "pic": 45
    },
    "Montbéliarde": {
        "pv": 725,
        "tb": 38.4,
        "tp": 32.7,
        "pic": 37
    },
    "Normande": {
        "pv": 750,
        "tb": 41.6,
        "tp": 34.2,
        "pic": 31
    },
    "Jersiaise": {
        "pv": 430,
        "tb": 54.5,
        "tp": 37.8,
        "pic": 27
    },
    "Brune": {
        "pv": 700,
        "tb": 41.1,
        "tp": 33.7,
        "pic": 35
    },
    "Simmental": {
        "pv": 750,
        "tb": 39.8,
        "tp": 33.6,
        "pic": 33
    }
}

NEC_CORRECTION = {
    2.0: -50,
    2.5: -25,
    3.0: 0,
    3.5: 25,
    4.0: 50
}


def facteur_lactation(lactation):
    if lactation == 1:
        return 0.85
    elif lactation == 2:
        return 0.95
    return 1.0


def ufl_croissance(lactation):
    if lactation == 1:
        return 1.0
    elif lactation == 2:
        return 0.5
    return 0.0


def pdi_croissance(lactation):
    if lactation == 1:
        return 350
    elif lactation == 2:
        return 150
    return 0


def ufl_gestation(mois):
    if mois == 7:
        return 0.5
    elif mois == 8:
        return 1.0
    elif mois >= 9:
        return 1.8
    return 0.0


def pdi_gestation(mois):
    if mois == 7:
        return 100
    elif mois == 8:
        return 200
    elif mois >= 9:
        return 400
    return 0


def poids_vif(race, nec):
    return (
        RACES[race]["pv"]
        + NEC_CORRECTION[nec]
    )


def production_lait(
    race,
    lactation,
    dim,
    nec,
    mois_gestation
):

    pic = RACES[race]["pic"]

    courbe = (
        (dim ** 0.18)
        * math.exp(-0.0032 * dim)
    ) / (
        (60 ** 0.18)
        * math.exp(-0.0032 * 60)
    )

    facteur_nec = (
        1 - abs(nec - 3) * 0.03
    )

    if mois_gestation < 5:
        facteur_gestation = 1
    else:
        facteur_gestation = (
            1 - 0.015 * (mois_gestation - 4)
        )

    lait = (
        pic
        * facteur_lactation(lactation)
        * courbe
        * facteur_nec
        * facteur_gestation
    )

    return round(lait, 1)


def besoins_ufl(
    race,
    lactation,
    dim,
    nec,
    mois_gestation
):

    pv = poids_vif(race, nec)

    lait = production_lait(
        race,
        lactation,
        dim,
        nec,
        mois_gestation
    )

    tb = RACES[race]["tb"]
    tp = RACES[race]["tp"]

    entretien = (
        0.041
        * (pv ** 0.75)
    )

    production = (
        lait
        * (
            0.44
            + 0.0055 * (tb - 40)
            + 0.0033 * (tp - 31)
        )
    )

    croissance = ufl_croissance(lactation)

    gestation = ufl_gestation(
        mois_gestation
    )

    total = (
        entretien
        + production
        + croissance
        + gestation
    )

    return {
        "entretien": round(entretien, 2),
        "production": round(production, 2),
        "croissance": round(croissance, 2),
        "gestation": round(gestation, 2),
        "total": round(total, 2)
    }


def besoins_pdi(
    race,
    lactation,
    dim,
    nec,
    mois_gestation
):

    pv = poids_vif(race, nec)

    lait = production_lait(
        race,
        lactation,
        dim,
        nec,
        mois_gestation
    )

    tp = RACES[race]["tp"]

    entretien = (
        3.25
        * (pv ** 0.75)
    )

    production = (
        1.92
        * tp
        * lait
    )

    croissance = pdi_croissance(
        lactation
    )

    gestation = pdi_gestation(
        mois_gestation
    )

    total = (
        entretien
        + production
        + croissance
        + gestation
    )

    return {
        "entretien": round(entretien, 0),
        "production": round(production, 0),
        "croissance": round(croissance, 0),
        "gestation": round(gestation, 0),
        "total": round(total, 0)
    }
