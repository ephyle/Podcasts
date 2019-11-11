#option 1 for converting data to linked data
#making triples manually 
#adapted fromhttps://rdflib.readthedocs.io/en/stable/gettingstarted.html

from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

class GEntity:
    def __init__(entity, RDFtype, name, identifier):
        entity.type = RDFtype
        entity.name = name
        entity.id = identifier
        entity.g =  Graph()
        entity.node = BNode()
    def triple(node):
        entity.g.add( (entity.node, RDF.type, entity.type) )
        entity.g.add( (entity.node, FOAF.name, Literal(entity.name)) )
        entity.g.add( (entity.node, DC.identifier, URIRef(entity.id)) )
        for s, p, o in entity.g:
            print(s)
            print(p)
            print(o+'\n')
        ## Bind a few prefix, namespace pairs for more readable output
        # entity.g.bind("dc", DC)
        # entity.g.bind("foaf", FOAF)
        # print( entity.g.serialize(format='n3') )


node1 = GEntity(FOAF.Person, "Asa Hillard", "https://en.m.wikipedia.org/wiki/Asa_Grant_Hilliard_III#")
node1.triple()



