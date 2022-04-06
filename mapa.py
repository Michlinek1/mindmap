import pydot
import os





def mindMap():
    listaslow = []
    pyt1 = int(input("Ile chcesz dodać strzałek?"))
    for x in range(pyt1):
        pyt2 = input("Co chcesz dodać?")
        listaslow.append(pyt2)
        print(listaslow)
    konwerter = ' '.join(listaslow)
    with open("cos.txt", "w") as f:
        f.write(konwerter + "\n")
        f.close()
    os.environ["PATH"] += os.pathsep + "C:\\Program Files (x86)\\Graphviz\\bin"
    graph = pydot.Dot(graphtype="Dot", rankdir="UD")
    def dodawanie(pierwszy, drugi):
        for x in range(pyt1):
            edge = pydot.Edge(pierwszy, drugi )
            graph.add_edge(edge)   
    dodawanie(listaslow[0], listaslow[1])
    

    graph.write_png("map.png")
    os.startfile("map.png")
      
mindMap()

