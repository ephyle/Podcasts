#option 1 for converting data to linked data
#making triples manually 
#adapted fromhttps://rdflib.readthedocs.io/en/stable/gettingstarted.html
import csv
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

entity_list = []

graph = Graph()
with open('triples.csv','r') as file:
    tbuild = csv.reader(file)
    next(tbuild, None)
    for row in tbuild:
        if row[3] != None:
            Name = row[3]
        # if Type == "FOAF.Person":
            # Type = FOAF.Person
            Type = row[4] 
            URI = row[5]
            graph.add( (URIRef(URI), RDF.type, URIRef(Type)) )
            graph.add( (URIRef(URI), FOAF.name, Literal(Name)) ) 
            graph.add( (URIRef(URI), DC.identifier, URIRef(URI)) )
        if row[6] != None:
            P2 = row[6]
            O2 = row[7]
            graph.add( (URIRef(URI), URIRef(P2), URIRef(O2)) )
        if row[8] != None:
            P3 = row[8]
            O3 = row[9]            
            graph.add( (URIRef(URI), URIRef(P3), URIRef(O3)) )
       # print(Type, Name, URI)

for s, p, o in graph:
    print(s)
    print(p)
    print(o+'\n')
graph.bind("dc", DC)
graph.bind("foaf", FOAF)
print( graph.serialize(format='n3') )
