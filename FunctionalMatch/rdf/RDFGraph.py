__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2025, Functional Match"
__credits__ = ["Giacomo Bergami", "Oliver Robert Fox"]
__license__ = "GPLv3"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"

from rdflib import Namespace
from rdflib import Graph, URIRef, BNode, Literal, XSD
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from rdflib.namespace import OWL, RDF, RDFS, FOAF

def literal(s: str):
    return Literal(s, datatype=XSD.string)


def boolean(s: bool):
    return Literal(s, datatype=XSD.boolean)

def integer(s: bool):
    return Literal(s, datatype=XSD.integer)

def double(s: float):
    return Literal(s, datatype=XSD.double)

def onta(ns, s: str):
    import urllib
    return URIRef(ns[urllib.parse.quote_plus(s)])

class RDFGraph(object):
    """
    This class provides PostgreSQL support for RDF graphs via RDFLib and SQLAlchemy.
    This allows to load
    """
    def __init__(self, name, namespace, user, password, hostame, port, database):
        self.database = database
        self.port = port
        self.hostame = hostame
        self.password = password
        self.user = user
        self.namespace = Namespace(namespace)
        assert isinstance(name, str)
        self.ident = URIRef(name)
        self.name = name
        self.graph = None
        self.uri = Literal(f'postgresql+psycopg2://{user}:{password}@{hostame}:{port}/{database}')
        # self.filename = filename
        self._started = False
        self._stopped = True
        self.names = None
        self.classes = None
        self.relationships = None

    def start(self):
        if self._started:
            return False
        if not self._actual_start():
            return False
        self._started = True
        self._stopped = False

    def clear(self):
        if self._started and self.uri is not None:
            self.graph.destroy(self.uri)
            return True
        return False

    def create_property(self, name, comment=None):
        if name not in self.relationships:
            d_object = URIRef(self.namespace[name])
            self.graph.add((d_object, RDF.type, OWL.ObjectProperty))
            self.relationships[name] = d_object
            if comment is not None:
                self.graph.add((d_object, RDFS.comment, Literal(comment)))
        return self.relationships[name]

    def create_relationship(self, name, comment=None):
        if name not in self.relationships:
            self.relationships[name] = URIRef(self.namespace[name])
            if comment is not None:
                self.graph.add((self.relationships[name], RDFS.comment, Literal(comment)))
        return self.relationships[name]

    def create_relationship_instance(self, src: str, rel: str, dst: str, refl=False):
        assert src in self.names
        assert dst in self.names
        rel = self.create_relationship(rel)
        self.graph.add((self.names[src], rel, self.names[dst]))
        if refl:
            self.graph.add((self.names[dst], rel, self.names[src]))

    def extract_properties(self, obj_src, kwargs):
        for k, val in kwargs.items():
            if val is not None:
                if k not in self.relationships:
                    rel = URIRef(self.namespace[k])
                    self.graph.add((rel, RDF.type, OWL.ObjectProperty))
                    self.relationships[k] = rel
                result = literal(str(val))
                if isinstance(val, dict):
                    src_bnode = BNode()
                    self.graph.add((obj_src, self.relationships[k], src_bnode))
                    self.extract_properties(src_bnode, val)
                elif isinstance(val, list) or isinstance(val, tuple):
                    for x in val:
                        if isinstance(x, bool):
                            result = boolean(x)
                        elif isinstance(x, str):
                            result = literal(x)
                        elif isinstance(x, int):
                            result = integer(x)
                        elif isinstance(x, float):
                            result = double(x)
                        self.graph.add((obj_src, self.relationships[k], result))
                elif isinstance(val, bool):
                    result = boolean(val)
                    self.graph.add((obj_src, self.relationships[k], result))
                elif isinstance(val, str):
                    result = literal(val)
                    self.graph.add((obj_src, self.relationships[k], result))
                elif isinstance(val, int):
                    result = integer(val)
                    self.graph.add((obj_src, self.relationships[k], result))
                elif isinstance(val, float):
                    result = double(val)
                    self.graph.add((obj_src, self.relationships[k], result))

    def create_entity(self, name: str, clazzL=None, label=None, comment=None,
                       **kwargs):
        if label is None:
            label = name
        if name not in self.names:
            self.names[name] = onta(self.namespace, name)
        if (clazzL is not None):
            if isinstance(clazzL, list):
                for clazz in clazzL:
                    assert clazz in self.classes
                    clazz = self.classes[clazz]
                    self.graph.add((self.names[name], RDF.type, clazz))
            elif isinstance(clazzL, str):
                clazz = self.classes[clazzL]
                self.graph.add((self.names[name], RDF.type, clazz))
            self.graph.add((self.names[name], RDFS.label, literal(label)))
        self.extract_properties(self.names[name], kwargs)
        if comment is not None:
            self.graph.add((self.names[name], RDFS.comment, Literal(comment)))
        return self.names[name]

    def create_class(self, name, subclazzOf=None, comment=None):
        if name not in self.classes:
            clazz = onta(self.namespace, name)
            self.graph.add((clazz, RDF.type, OWL.Class))
            if (subclazzOf is not None):
                if isinstance(subclazzOf, str):
                    subclazzOf = self.create_class(subclazzOf)
                    self.graph.add((clazz, RDFS.subClassOf, subclazzOf))
                elif isinstance(subclazzOf, list):
                    for x in subclazzOf:
                        x = self.create_class(x)
                        self.graph.add((clazz, RDFS.subClassOf, x))
            self.classes[name] = clazz
        if comment is not None:
            self.graph.add((self.classes[name], RDFS.comment, Literal(comment)))
        return self.classes[name]

    def create_concept(self, full_name, type,
                       hasAdjective=None,
                       entryPoint=None,
                       subject=None,
                       d_object=None,
                       entity_name=None,
                       composite_with=None,comment=None,
                       **kwargs):
        if entity_name == None:
            entity_name = full_name
        ref = self.create_entity(full_name, type, label=entity_name)
        if entryPoint == None:
            entryPoint = ref
        else:
            assert entryPoint in self.names
            entryPoint = self.names[entryPoint]
        self.graph.add((ref, self.relationships["entryPoint"], entryPoint))
        from collections.abc import Iterable
        if (hasAdjective != None) and (isinstance(hasAdjective, Iterable)):
            assert hasAdjective in self.names
            self.graph.add((ref, self.relationships["hasAdjective"], self.names[hasAdjective]))
        if (d_object is not None):
            assert subject is not None
        if composite_with is not None:
            assert isinstance(composite_with, list)
            for composite in composite_with:
                assert composite in self.names
                self.graph.add((ref, self.relationships["composite_form_with"], self.names[composite]))
        if subject is not None:
            assert subject in self.names
            self.graph.add((ref, self.relationships["subject"], self.names[subject]))
            if d_object is not None:
                self.graph.add((ref, self.relationships["d_object"], self.names[d_object]))
        for k, val in kwargs.items():
            if k not in self.relationships:
                d_object = URIRef(self.namespace[k])
                self.graph.add((d_object, RDF.type, OWL.ObjectProperty))
            result = literal(str(val))
            if isinstance(val, bool):
                result = boolean(val)
            elif isinstance(val, str):
                result = literal(val)
            elif isinstance(val, float):
                result = double(val)
            self.graph.add((ref, self.relationships[k], result))
        if comment is not None:
            self.graph.add((ref, RDFS.comment, Literal(comment)))
        return ref

    def serialize(self, filename):
        self.graph.serialize(destination=filename)

    def stop(self):
        if (self._stopped) or (not self._started):
            self._stopped = True
            return True
        if not self._actual_stop():
            return False
        self._started = False
        self._stopped = True
        return True

    def _actual_start(self):
        self.graph = Graph("SQLAlchemy", identifier=self.ident)
        engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(self.user,self.password,self.hostame,self.port, self.database))
        if not database_exists(engine.url):
            create_database(engine.url)
        self.graph.open(self.uri, create=True)
        self.names = dict()
        self.relationships = dict()
        self.classes = dict()
        self.graph.bind(self.name, self.namespace)
        self.graph.bind("rdfs", RDF)
        return True

    def _actual_stop(self):
        self.names = None
        self.classes = None
        self.relationships = None
        return True

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()