#adapted fromhttps://rdflib.readthedocs.io/en/stable/gettingstarted.html
import csv
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

graph = Graph()
with open('triplesV2.csv','r') as file:
    tbuild = csv.reader(file)
    next(tbuild, None)
    #read every entity in spreadsheet
    for row in tbuild:
        #if an entity exsists, create basic triples (name, type, uri)
        if row[5] != "":
            Subject = row[5]
            Type = row[6] 
            URI = row[7]
            Episode = row[3]
            graph.add( (URIRef(URI), RDF.type, URIRef(Type)) )
            graph.add( (URIRef(URI), FOAF.name, Literal(Subject)) ) 
            graph.add( (URIRef(URI), DC.identifier, URIRef(URI)) )
            graph.add( (URIRef(URI), DC.isPartOf, Literal(Episode)) )
            # URIRef("http://purl.org/dc/terms/isPartOf")
            #if an entity has another statement, add it
            if row[8] != "":
                P2 = row[8]
                O2 = row[10]
                graph.add( (URIRef(URI), URIRef(P2), URIRef(O2)) )
            #if an entity has ANOTHER statement, add it
            if row[12] != "":
                P3 = row[12]
                O3 = row[14]            
                graph.add( (URIRef(URI), URIRef(P3), URIRef(O3)) )
                #test for correct row numbers and skipping
                #print(f"Subject:{Subject} Predicate:{P3} Object:{O3}\n")

for s, p, o in graph:
    print(s)
    print(p)
    print(o+'\n')
graph.bind("dc", DC)
graph.bind("foaf", FOAF)
print( graph.serialize(format='xml') )
graph.serialize(destination='tripleOUT.xml', format='xml')