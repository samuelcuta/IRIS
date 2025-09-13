import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mpl_toolkits.mplot3d import Axes3D

# ----------------------
# 1. Cargar dataset
# ----------------------
iris = load_iris()
X = iris.data[:, :3]   # 3 características: sepal length, sepal width, petal length
y = iris.target        # 0=setosa, 1=versicolor, 2=virginica

# Dividir en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ----------------------
# 2. Entrenar clasificadores One-vs-Rest
# ----------------------
models = {}
for clase in np.unique(y):
    y_binary = (y_train == clase).astype(int)  # Clase actual vs resto
    model = LinearRegression()
    model.fit(X_train, y_binary)
    models[clase] = model

# ----------------------
# 3. Función para clasificar nueva planta
# ----------------------
def clasificar_nueva_planta(features):
    scores = [models[c].predict([features])[0] for c in models]
    clase_predicha = np.argmax(scores)
    return clase_predicha, scores

# ----------------------
# 4. Entrada del usuario
# ----------------------
print("Ingrese las características de la planta:")
sepal_length = float(input("Sepal length (cm): "))
sepal_width = float(input("Sepal width (cm): "))
petal_length = float(input("Petal length (cm): "))

nueva_planta = [sepal_length, sepal_width, petal_length]
clase_predicha, scores = clasificar_nueva_planta(nueva_planta)

print(f"\nLa planta fue clasificada como: {iris.target_names[clase_predicha]}")
print(f"Puntajes de regresión: {scores}")

# ----------------------
# 5. Graficar datos + plano de regresión + nueva planta
# ----------------------
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar dataset real
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.Set1, edgecolor="k", alpha=0.6)

# Graficar punto nuevo
ax.scatter(nueva_planta[0], nueva_planta[1], nueva_planta[2],
           c="gold", s=200, edgecolor="black", marker="*", label="Nueva planta")

# Dibujar plano de la clase predicha
model = models[clase_predicha]
x_surf, y_surf = np.meshgrid(
    np.linspace(X[:, 0].min(), X[:, 0].max(), 20),
    np.linspace(X[:, 1].min(), X[:, 1].max(), 20)
)
z_surf = (-model.intercept_ - model.coef_[0]*x_surf - model.coef_[1]*y_surf) / model.coef_[2]
ax.plot_surface(x_surf, y_surf, z_surf, color="lightblue", alpha=0.4)

# Etiquetas
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
ax.set_title(f"Clasificación con Regresión Lineal → {iris.target_names[clase_predicha]}")
ax.legend()

plt.show()
