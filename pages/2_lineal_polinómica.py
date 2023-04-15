import streamlit as st
from joblib import load
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

poly = PolynomialFeatures(degree=2, include_bias=False)

model_poly = load("model_poly.joblib")

with st.sidebar:
    st.header("Estimación de precios de automóvil")
    st.caption("Sesión virtual 15/04/2023 - GDG Sucre")

st.subheader("Regresión lineal polinómica")
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
    data = poly.fit_transform([[highway_mpg]])
    price = max(model_poly.predict(data)[0], 5000)
    formatted_price = f"$ { price : .2f}"

    st.metric("Precio estimado", formatted_price)

fig, ax = plt.subplots()
x = np.linspace(15, 55, num=100)

ax.plot(x, model_poly.predict(poly.transform(x.reshape(-1, 1))))
ax.plot([highway_mpg], [price], "ko")

ax.set_xlim(15, 55)
ax.set_ylim(4000, 32000)
ax.set_title("Relación precio y millas por galón en carretera")

st.pyplot(fig)
