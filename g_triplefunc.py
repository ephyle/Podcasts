#option 1 for converting data to linked data
#making triples manually 
#adapted fromhttps://rdflib.readthedocs.io/en/stable/gettingstarted.html
import csv
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

entity_list = []

graph = Graph()
with open('triplebuild_test.csv','r') as file:
    tbuild = csv.reader(file)
    next(tbuild, None)
    for row in tbuild:
        Type = row[0]
        if Type == "FOAF.Person":
            Type = FOAF.Person
        Name = row[1] 
        URI = row[2]
        graph.add( (URIRef(URI), RDF.type, Type) )
        graph.add( (URIRef(URI), FOAF.name, Literal(Name)) ) 
        graph.add( (URIRef(URI), DC.identifier, URIRef(URI)) )
       # print(Type, Name, URI)

for s, p, o in graph:
    print(s)
    print(p)
    print(o+'\n')
graph.bind("dc", DC)
graph.bind("foaf", FOAF)
print( graph.serialize(format='n3') )


