import streamlit as st
import joblib
import numpy as np

st.title("🎯 Predição de desempenho — Brasileirão")

model = joblib.load('model_rf.pkl')

st.header("Informe os valores:")

points = st.number_input("Points", min_value=0)
goals_diff = st.number_input("Goal Difference", min_value=-100, max_value=100)
loss = st.number_input("Losses", min_value=0)
won = st.number_input("Wins", min_value=0)
played = st.number_input("Matches Played", min_value=0)
goals_taken = st.number_input("Goals Taken", min_value=0)
goals = st.number_input("Goals Scored", min_value=0)
draw = st.number_input("Draws", min_value=0)

X = np.array([[points, goals_diff, loss, won, played, goals_taken, goals, draw]])

if st.button("Prever"):
    pred = model.predict(X)[0]
    st.success(f"Previsão: {pred}")

