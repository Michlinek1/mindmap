import glob
import pydot
import os

class Error(Exception):
    pass
class NazwaPliku(Error):
    """Plik nie ma nazwy!"""
    pass


def mindMap():
    listaslow = []
    nazwplik = input("Jak chcesz, żeby plik się nazywał?")
    zdjecia = [f for f in glob.glob("*.png")]
    if nazwplik == "":
        raise NazwaPliku("Plik nie ma nazwy!")
    elif nazwplik in zdjecia:
        print("Taki plik już istnieje!")
        mindMap()
    elif ".png" not in nazwplik:
        print("Niepoprawny format pliku!")
        mindMap()
    
    for x in range(4):
        pyt = input("Co chcesz dodać?")
        listaslow.append(pyt)
 
    with open("cos.txt", "w") as f:
        konw = "\n".join(listaslow)
        f.write(konw + "\n")
        f.close()
        
        
    os.environ["PATH"] += os.pathsep + "C:\\Program Files (x86)\\Graphviz\\bin"
    graph = pydot.Dot(graphtype="Dot", rankdir="UD")
    graph.set_node_defaults(shape="box")
    edge = pydot.Edge(listaslow[0], listaslow[1])
    edge2 = pydot.Edge(listaslow[2], listaslow[3])
    graph.add_edge(edge)   
    graph.add_edge(edge2)
    

    graph.write_png(f"{nazwplik}")
    os.startfile(f"{nazwplik}")
    os.startfile("cos.html")
      
mindMap()

