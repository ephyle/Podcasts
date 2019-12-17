#adapted fromhttps://rdflib.readthedocs.io/en/stable/gettingstarted.html
import csv
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF
from rdflib.serializer import Serializer

graph = Graph()
with open('triplesV7.csv','r') as file:
    tbuild = csv.reader(file)
    next(tbuild, None)
    #read every entity in spreadsheet
    for row in tbuild:
        #if an entity exsists, create basic triples (name, type, uri)
        if row[6] != "":
            Subject = row[6]
            Type = row[7] 
            URI = row[8]
            Episode = row[3]
            graph.add( (URIRef(URI), RDF.type, URIRef(Type)) )
            graph.add( (URIRef(URI), FOAF.name, Literal(Subject)) ) 
            graph.add( (URIRef(URI), URIRef('http://gephi.org/label'), Literal(Subject)) )
            # graph.add( (URIRef(URI), DC.identifier, URIRef(URI)) )
            graph.add( (URIRef(URI), DC.isPartOf, URIRef(Episode)) )

            # if an entity has another statement, add it
            if row[9] != "":
                P2 = row[9]
                O2 = row[11]
                graph.add( (URIRef(URI), URIRef(P2), URIRef(O2)) )
                #test for correct row numbers and skipping
                print(f"Subject:{Subject} Predicate:{P2} Object:{O2}\n")
            
            #if an entity has ANOTHER statement, add it
            if row[13] != "":
                P3 = row[13]
                O3 = row[15]            
                graph.add( (URIRef(URI), URIRef(P3), URIRef(O3)) )
            #test for correct row numbers and skipping
                print(f"Subject:{Subject} Predicate:{P3} Object:{O3}\n")
            
            #if an entity has ANOTHER statement, add it
            if row[17] != "":
                P4 = row[17]
                O4 = row[19]            
                graph.add( (URIRef(URI), URIRef(P4), URIRef(O4)) )
                #test for correct row numbers and skipping
                print(f"Subject:{Subject} Predicate:{P4} Object:{O4}\n")

# for s, p, o in graph:
#     print(s)
#     print(p)
#     print(o+'\n')
graph.bind("dc", DC)
graph.bind("foaf", FOAF)
print( graph.serialize(format='xml') )
graph.serialize(destination='RDFtripleOUT7.rdf', format='xml')