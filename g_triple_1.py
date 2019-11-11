#option 1 for converting data to linked data
#making triples manually 
#adapted fromhttps://rdflib.readthedocs.io/en/stable/gettingstarted.html

from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

g = Graph()

# Create an identifier to use as the subject for entity.
Hillard = BNode()

# Add triples using store's add method.
g.add( (Hillard, RDF.type, FOAF.Person) )
g.add( (Hillard, FOAF.name, Literal("Asa Hillard")) )
g.add( (Hillard, DC.identifier, URIRef("https://en.m.wikipedia.org/wiki/Asa_Grant_Hilliard_III#")) )

# Iterate over triples in store and print them out.
print("--- printing triples ---")
for s, p, o in g:
    print(s)
    print(p)
    print(o+'\n')

# For each foaf:Person in the store print out its mbox property.
print("--- printing identifiers ---")
for person in g.subjects(RDF.type, FOAF.Person):
    for identifier in g.objects(person, DC.identifier):
        print(identifier+'\n')
 
# Bind a few prefix, namespace pairs for more readable output
g.bind("dc", DC)
g.bind("foaf", FOAF)

print( g.serialize(format='n3') )
