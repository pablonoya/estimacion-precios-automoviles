import streamlit as st
from joblib import load

model = load("model.joblib")


with st.sidebar:
    st.header("Estimación de precios de automóvil")
    st.caption("Sesión virtual 15/04/2023 - GDG Sucre")
    st.write(
        "[Código en Github](https://github.com/pablonoya/estimacion-precios-automoviles/)"
    )

st.subheader("Regresión lineal simple")
col1, col2 = st.columns(2, gap="medium")

with col1:
    sc1, sc2 = st.columns(2)
    with sc1:
        num_of_doors = st.radio("Núm. de puertas", ("Dos", "Cuatro"))
    with sc2:
        drive_wheel = st.radio("Tipo de tracción", ("Delantera", "Trasera", "4 ruedas"))

    length = st.slider(
        label="Largo",
        min_value=14.0,
        max_value=20.5,
        format="%f m.",
        value=15.1,
    )
    width = st.slider(
        label="Ancho",
        min_value=6.0,
        max_value=7.5,
        format="%f m.",
        value=6.2,
    )
    height = st.slider(
        label="Alto", min_value=4.9, max_value=6.0, format="%f m.", value=5.2
    )
    curb_weight = st.slider(
        label="Peso en vacío", min_value=1480, max_value=4070, value=2023
    )


with col2:
    city_mpg = st.slider(
        label="Millas por galón en ciudad",
        min_value=13,
        max_value=49,
        format="%d mpg",
        value=24,
    )
    highway_mpg = st.slider(
        label="Millas por galón en carretera",
        min_value=16,
        max_value=54,
        format="%d mpg",
        value=26,
    )
    horsepower = st.slider(
        label="Caballos de fuerza", min_value=48, max_value=200, value=123
    )
    peak_rpm = st.slider(
        label="Pico de revoluciones por minuto",
        min_value=4150,
        max_value=6600,
        step=50,
        format="%d rpm",
        value=5000,
    )
    sc1, sc2 = st.columns(2)
    with sc1:
        bore = st.slider(
            label="Diámetro del cilindro", min_value=2.5, max_value=4.0, value=2.8
        )
    with sc2:
        stroke = st.slider(label="Carrera", min_value=2.0, max_value=4.2, value=3.2)

_, center, _ = st.columns(3)

with center:
    data = [
        [
            num_of_doors == "Dos",
            length * 10,
            width * 10,
            height * 10,
            curb_weight,
            bore,
            stroke,
            horsepower,
            peak_rpm,
            city_mpg,
            highway_mpg,
            drive_wheel == "Delantera",
            drive_wheel == "Trasera",
            drive_wheel == "4 ruedas",
        ]
    ]
    price = model.predict(data)[0]
    formatted_price = f"$ { price : .2f}"

    st.metric("Precio estimado", formatted_price)
