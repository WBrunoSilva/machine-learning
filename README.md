# Classificador de Espécies da Íris com Random Forest

Este projeto utiliza o famoso *Iris Dataset* e aplica técnicas de **visualização**, **pré-processamento**, **análise de componentes principais (PCA)** e **classificação com o algoritmo Random Forest**.

O objetivo é construir, avaliar e salvar um modelo preditivo capaz de identificar a espécie de uma flor íris com base em suas medidas.

---

## Tecnologias utilizadas

- Python 3  
- Pandas & NumPy  
- Matplotlib, Seaborn & Plotly  
- Scikit-learn  
- Pickle  

---

## Etapas do projeto

- **Carregamento dos dados**  
  Usa o `load_iris` da biblioteca `sklearn.datasets`.

- **Visualização exploratória**  
  - Boxplots e histogramas por espécie com Plotly  
  - Scatter matrix para visualização multivariada

- **Normalização**  
  As variáveis numéricas são padronizadas com `MinMaxScaler`.

- **Redução de Dimensionalidade (PCA)**  
  Aplica PCA para reduzir o número de dimensões a dois componentes principais.

- **Treinamento do modelo**  
  Classificador Random Forest com profundidade máxima de 2.

- **Avaliação**  
  - Acurácia  
  - Precisão  
  - Revocação  
  - F1-score  
  - Matriz de confusão  
  - Validação cruzada (5 folds)

- **Serialização**  
  O modelo final é salvo e carregado usando `pickle`.

