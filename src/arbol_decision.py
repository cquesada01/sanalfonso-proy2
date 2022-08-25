from sklearn import tree
import pandas
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

datos = pandas.read_excel("dataset.xlsx")

print(datos)

caracteristicas = ["id_pregunta","id_cat","id_intencion"]

#variable dependiente a analizar para comprobar que pregunta tiene el usuario
x=datos[caracteristicas]

#variable independiente a recuperar , se respondio a la pregunta ?
y=datos["id_respuesta"]

print(x)
print(y)

arbol = DecisionTreeClassifier()
arbol = arbol.fit(x,y)
"""datos = tree.export_graphviz(arbol, out_file=None, feature_names=caracteristicas)
graph = pydotplus.graph_from_dot_data(datos)
graph.write_png("miarbol.png")

imagen=pltimg.imread("miarbol.png")
imgplot = plt.imshow(imagen)
plt.show()"""


#print(arbol.predict([[5,2,4]]))
def arbol_respuesta(p1,p2,p3):
    respuesta = arbol.predict([[p1,p2,p3]])