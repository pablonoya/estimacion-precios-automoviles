import streamlit as st
from joblib import load
import matplotlib.pyplot as plt

model_simple = load("model_simple.joblib")

with st.sidebar:
    st.header("Estimación de precios de automóvil")
    st.caption("Sesión virtual 15/04/2023 - GDG Sucre")
    st.write(
        "[Código en Github](https://github.com/pablonoya/estimacion-precios-automoviles/)"
    )

st.subheader("Características")
col1, col2 = st.columns(2, gap="medium")

with col1:
    highway_mpg = st.slider(
        label="Millas por galón en carretera",
        min_value=16,
        max_value=54,
        format="%d mpg",
        value=26,
    )

with col2:
    data = [[highway_mpg]]
    price = max(model_simple.predict(data)[0], 2000)
    formatted_price = f"$ { price : .2f}"

    st.metric("Precio estimado", formatted_price)

fig, ax = plt.subplots()

ax.plot([15, 55], model_simple.predict([[15], [55]]))
ax.plot([highway_mpg], [price], "ko")

ax.set_xlim(15, 55)
ax.set_ylim(1000, 25000)
ax.axhline(y=2000, color="black", linestyle="--")

ax.set_title("Relación precio y millas por galón en carretera")

st.pyplot(fig)
