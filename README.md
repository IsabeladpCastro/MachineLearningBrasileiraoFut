# 🎩 Machine Learning para Futebol — Predição com Dados do Brasileirão

Este repositório contém um projeto de **Machine Learning aplicado ao futebol**, desenvolvido para análise de dados relacionados a desempenho de equipes, previsão de métricas e explicação do modelo com técnicas de interpretabilidade.

A aplicação possui uma interface interativa em **Streamlit**, onde o usuário pode inserir valores e visualizar a predição do modelo em tempo real 🚀

---

## 📌 Objetivo do Projeto

O objetivo é construir um modelo capaz de **prever variáveis contínuas** de desempenho esportivo (ex: finalizações, posse de bola, gols esperados, etc.), utilizando dados de partidas.  
Além disso, foram empregados frameworks de interpretabilidade (SHAP) para tornar o modelo explicável.

---

## 📊 Dados Utilizados

O dataset contém estatísticas de desempenho dos times em uma temporada do campeonato, com as seguintes colunas:

| Feature        | Descrição                             
|----------------|-------------------------------------------------
| `season`       | Ano da temporada 
| `place`        | Posição do time na tabela 
| `team`         | Nome do time 
| `points`       | Pontuação total (3 por vitória, 1 por empate) 
| `played`       | Total de partidas disputadas 
| `won`          | Número de vitórias 
| `draw`         | Número de empates 
| `loss`         | Número de derrotas 
| `goals`        | Total de gols marcados 
| `goals_taken`  | Total de gols sofridos 
| `goals_diff`   | Saldo de gols (`goals - goals_taken`) 

Essas features representam indicadores clássicos de desempenho esportivo e permitem prever métricas relacionadas à performance ao longo da temporada.

Antes do treinamento, o dataset passou por:

✅ Verificação de valores ausentes  
✅ Tratamento de discrepâncias numéricas  
✅ Conversão de tipos quando necessário  
✅ Engenharia de features contextual (ex.: saldo de gols)  

Isso garante maior consistência e robustez ao modelo.

---

## 🤖 Modelo

O modelo principal escolhido foi um **Random Forest Regressor**, por motivos:

- ✅ Estável em datasets com ruído
- ✅ Não exige normalização explícita
- ✅ Trabalha bem com interações não-lineares
- ✅ Explicável via SHAP

## 🧠 Interpretabilidade (Explainability)
- Foi utilizado SHAP (SHapley Additive Explanations):
- Identificação de features mais impactantes
- Explicações individuais para predições
- Violin/summary plot para visualizar influência global
Exemplo de código:
```
explainer = shap.Explainer(model, X)
shap_values = explainer(X, check_additivity=False)
shap.summary_plot(shap_values.values, X)
```
---

## 🖥️ Aplicação (Streamlit)
A aplicação permite:
- ✅ Inserir valores manualmente
- ✅ Predizer um output do modelo
- ✅ Mostrar importância das features

Para rodar:
```
streamlit run app.py
```
Interface simples e amigável 👇
<img width="1919" height="1071" alt="image" src="https://github.com/user-attachments/assets/b1dab5cf-b791-4dd0-a978-83ffa32b921a" />

---

## 🛠️ Como Rodar o Projeto
1️⃣ Clone o repositório:
```
git clone https://github.com/seu-usuario/seu-repo.git
```
2️⃣ Crie um ambiente virtual:
```
python -m venv .venv
source .venv/bin/activate     # Linux/Mac
.venv\Scripts\activate        # Windows
```
3️⃣ Instale as dependências:
```
pip install -r requirements.txt
```
4️⃣ Execute a aplicação:
```
streamlit run app.py
```

---

## 🧩 Arquitetura / Módulos
Dentro do projeto, os notebooks estão separados por:

- 📌 Notebook 01 — Análise exploratória
- 📌 Notebook 02 — Pré-processamento
- 📌 Notebook 03 — Treinamento
- 📌 Notebook 04 — Interpretabilidade + SHAP

Cada seção possui texto explicativo contextualizando:

- ✅ Por que limpar?
- ✅ Por que escolher Random Forest?

---

👨‍🏫 Justificativa das Decisões Técnicas

- Random Forest → ótimo desempenho sem tuning pesado
- SHAP → interpretabilidade é crítica em esportes
- Streamlit → prototipação rápida de aplicações ML
- Padronização modular → facilita reprodutibilidade

---

✅ Conclusão

Este projeto demonstra:
- ✅ Aplicação real de machine learning no futebol
- ✅ Interpretabilidade prática com SHAP
- ✅ Protótipo funcional para uso imediato

---

🔗Referências e Créditos

- Streamlit Docs
- SHAP Paper (Lundberg & Lee, 2017)
- Scikit-learn Documentation
- Dados do Brasileirão (Kaggle)

---

🧑‍💻 Desenvolvedora

Isabela Castro
- 📚 Ciência da Computação
- ⚽ Estratégia + análise com dados
- 💻 ML / IA aplicada
