#  Clasificación de Plantas Iris con Regresión Lineal
Samuel Cuta y Gina Alvarado
##  Descripción del Proyecto
Este proyecto implementa un **sistema de clasificación de plantas del dataset Iris** usando el algoritmo de **Regresión Lineal en un esquema One-vs-Rest (OvR)**.  

El sistema permite que el usuario ingrese las características de una nueva planta (longitud de sépalo, ancho de sépalo y longitud de pétalo) y el modelo determina a qué especie pertenece:  
- **Setosa**  
- **Versicolor**  
- **Virginica**  

Además, se generan **gráficas 3D** que muestran:  
- Los datos originales del dataset.  
- El plano de regresión lineal de la clase predicha.  
- El nuevo punto ingresado por el usuario.  

---

## Metodología

1. **Dataset Iris**  
   Se utilizó el clásico dataset de **Iris** de `sklearn.datasets`, que contiene 150 registros de 3 especies de flores con sus características.

2. **Selección de Features**  
   Se escogieron **3 características** para entrenar y visualizar el modelo:  
   - Longitud del sépalo (*sepal length*)  
   - Ancho del sépalo (*sepal width*)  
   - Longitud del pétalo (*petal length*)  

3. **Regresión Lineal One-vs-Rest**  
   - Se entrenó un modelo de **regresión lineal** para cada clase (Setosa, Versicolor, Virginica).  
   - Cada modelo aprende a distinguir **su clase vs las demás**.  
   - Para clasificar una nueva planta, se calculan los **puntajes de predicción** de cada modelo y se selecciona el más alto.

4. **Clasificación Interactiva**  
   - El usuario ingresa manualmente los valores de la planta.  
   - El sistema calcula la especie predicha.  
   - Se muestran los resultados en consola y en una gráfica 3D.  

5. **Visualización 3D**  
   Se utiliza `matplotlib` con proyección 3D para representar:  
   - Los puntos del dataset con colores según la especie real.  
   - El plano de regresión lineal correspondiente a la clase predicha.  
   - El nuevo punto del usuario resaltado con un **asterisco dorado**.

---

## Ejemplo de Uso

### Entrada del usuario:
```
Sepal length (cm): 5.1
Sepal width (cm): 3.5
Petal length (cm): 1.4
```

### Salida esperada:
```
La planta fue clasificada como: setosa
Puntajes de regresión: [0.92, -0.10, 0.05]
```

### Gráfica generada:
- Muestra todo el dataset.  
- El plano de la clase **Setosa**.  
- El nuevo punto resaltado.  

---

##  Tecnologías Utilizadas
- **Python 3.13**  
- **scikit-learn** → para regresión lineal y dataset Iris  
- **matplotlib** → para visualizaciones 3D  

---

##  Cómo ejecutar
1. Clonar el repositorio o copiar el script `Iris.py`.  
2. Instalar dependencias:
   ```bash
   pip install numpy matplotlib scikit-learn
   ```
3. Ejecutar el script:
   ```bash
   python Iris.py
   ```
4. Ingresar los valores de la planta cuando se solicite.  

---

##  Conclusiones
- Aunque la **Regresión Lineal** no es un algoritmo diseñado originalmente para clasificación, al usarla bajo el enfoque **One-vs-Rest** es posible clasificar correctamente las plantas del dataset Iris.  
- Este enfoque es una introducción sencilla a cómo se pueden transformar problemas de clasificación en tareas de regresión.  
- Las gráficas permiten **visualizar los planos de decisión** y cómo se ubican los nuevos puntos en relación al dataset.  
