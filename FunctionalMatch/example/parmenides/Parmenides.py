import dataclasses
import os.path
import urllib
import rdflib
from rdflib.graph import Graph, ConjunctiveGraph
from rdflib import Graph, URIRef, BNode, Literal, XSD
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS, FOAF

from FunctionalMatch.example.parmenides import SentenceStructure, Prepositions
from FunctionalMatch.rdf.RDFGraph import RDFGraph


class Parmenides(RDFGraph):
    parmenides_ns = Namespace("https://logds.github.io/parmenides#")

    def __init__(self, user, password, hostame, port):
        super().__init__("parmenides", "https://logds.github.io/parmenides#", user, password, hostame, port, "parmenides")


def load_from_txt_file(p:Parmenides, path:str, classes:list, to_reject:set):
    with open(path, "r") as dep:
        for line in dep:
            line = line.strip()
            if line in to_reject:
                classes.append("Rejectable")
            p.create_entity(line, classes)

def generate_parmenides_graph(p:Parmenides, data_path:str):
    p.create_property("hasAdjective")
    p.create_property("subject")
    p.create_property("d_object")
    p.create_property("composite_form_with")
    p.create_property("attachTo")
    p.create_property("argument")
    p.create_property("logicalConstructProperty")
    p.create_property("logicalConstructName")
    p.create_relationship("hasProperty")
    p.create_relationship("formOf")
    p.create_relationship("entryPoint")
    p.create_relationship("partOf")
    p.create_relationship("isA")
    p.create_relationship("relatedTo")
    p.create_relationship("capableOf")
    p.create_relationship("adjectivalForm")
    p.create_relationship("adverbialForm")
    p.create_relationship("eqTo")
    p.create_relationship("neqTo")
    _T = p.create_class("Dimensions")
    LOC_T = p.create_class("LOC", "Dimensions")
    GPE_T = p.create_class("GPE", ["Dimensions", "LOC"])
    gp_T = p.create_class("GraphParse")
    reject_T = p.create_class("Rejectable", "GraphParse",
                              comment="Whether the edge shall be rejected in the internal rewriting pipeline")
    meta_T = p.create_class("MetaGrammaticalFunction")
    dep_T = p.create_class("dependency", "MetaGrammaticalFunction")
    log_f_T = p.create_class("LogicalFunction", "MetaGrammaticalFunction",
                             comment="The sentence constructs at the logical level, similarly to English' Adverbial Phrases and Indirect Objects (https://it.wikipedia.org/wiki/Analisi_logica_della_proposizione vs. https://en.wikipedia.org/wiki/Adverbial_phrase)")
    log_f_T = p.create_class("LogicalRewritingRule", "MetaGrammaticalFunction",
                             comment="Defines how to capture the elements within the sentence structure and rewriting them in the most appropriate way as properties of the kernel/singleton they refer to")
    gr_obj_T = p.create_class("GrammaticalFunction", "MetaGrammaticalFunction")
    verb_T = p.create_class("Measure", "GrammaticalFunction")  # TODO: Is this a grammatical function
    verb_T = p.create_class("Concept", "GrammaticalFunction")  # TODO: Is this a grammatical function
    verb_T = p.create_class("Verb", "GrammaticalFunction")
    verb_T = p.create_class("Preposition", "GrammaticalFunction")
    noun_T = p.create_class("Noun", "GrammaticalFunction")
    adj_T = p.create_class("Adjective", "GrammaticalFunction")
    adj_T = p.create_class("Adverb", "GrammaticalFunction")
    adj_T = p.create_class("CompoundForm", "GrammaticalFunction")
    tverb_T = p.create_class("TransitiveVerb", "Verb")
    iverb_T = p.create_class("IntransitiveVerb", "Verb")
    causverb_T = p.create_class("CausativeVerb", "Verb")
    moveverb_T = p.create_class("MovementVerb", "Verb")
    meansverb_T = p.create_class("MeansVerb", "Verb")
    stateverb_T = p.create_class("StateVerb", "Verb")
    matverb_T = p.create_class("MaterialisationVerb", "Verb")
    semimodalverb_T = p.create_class("SemiModalVerb", "Verb")
    proto_Prop = p.create_class("PrototypicalPreposition", "Preposition")
    dep_Prop = p.create_class("DependantPreposition", "Preposition")
    idio_Prop = p.create_class("IdiomaticPreposition", "Preposition")
    complex_Prop = p.create_class("ComplexPreposition", "Preposition")
    pronoun = p.create_class("Pronoun")
    pronoun_per = p.create_class("PersonalPronoun", "Pronoun")
    pronoun_dem = p.create_class("DemonstrativePronoun", "Pronoun")
    pronoun_rel = p.create_class("RelativePronoun", "Pronoun")
    pronoun_indef = p.create_class("IndefinitePronoun", "Pronoun")
    pronoun_interro = p.create_class("InterrogativePronoun", "Pronoun")
    unit_of_measure = p.create_class("UnitOfMeasure", "Measure")
    abstract_concept = p.create_class("AbstractEntity", "Concept")
    to_reject = None
    with open(os.path.join(data_path, "rejected_edge_types.txt"), "r") as dep:
        to_reject = {line.strip().lower() for line in dep}

    load_from_txt_file(p, os.path.join(data_path, "non_verb_types.txt"), ["dependency"], to_reject)
    load_from_txt_file(p, os.path.join(data_path, "verbs", "causative_verbs.txt"), ["CausativeVerb"], to_reject)
    load_from_txt_file(p, os.path.join(data_path, "verbs", "transitive_verbs.txt"), ["TransitiveVerb"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "units_of_measure.txt"), ["UnitOfMeasure"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "abstract_entity_concepts.txt"), ["AbstractEntity"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "verbs", "stative_verbs.txt"), ["Verb", "CausativeVerb"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "verbs", "means_verbs.txt"), ["Verb", "MeansVerb"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "verbs", "state_verbs.txt"), ["Verb", "StateVerb"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "verbs", "movement_verbs.txt"), ["Verb", "MovementVerb"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "verbs", "materialisation_verbs.txt"), ["Verb", "MaterialisationVerb"], to_reject)


    for preposition in Prepositions.load_prepositions(os.path.join(data_path, "prepositions.json")):
        classes = preposition.generate_classes(preposition.name.lower() in to_reject)
        p.create_entity(preposition.name, classes, **preposition.as_properties())

    log_defs, log_rewr_rules = SentenceStructure.load_logical_analysis(os.path.join(data_path, "logical_analysis.json"))
    for name, v in log_defs.items():
        for x in v.specs:
            d = dataclasses.asdict(x)
            if "property" in d and d["property"] is None:
                d.pop("property")
            else:
                d["logicalConstructProperty"] = d.pop("property")
            d["logicalConstructName"] = name
            entity_name = f"log/{name}/{d['logicalConstructProperty']}" if "logicalConstructProperty" in d else f"log/{name}"
            p.create_entity(entity_name, "LogicalFunction", entity_name, **d)
    ruleid = 1
    for rule in log_rewr_rules:
        for result in rule.classification:
            dres = dataclasses.asdict(result)
            if "property" in dres and dres["property"] is None:
                dres.pop("property")
            else:
                dres["logicalConstructProperty"] = dres.pop("property")
            dres["logicalConstructName"] = dres.pop("type")
            dres["rule_order"] = ruleid
            dres.update(rule.premise)
            p.create_entity(f"logrule/{ruleid}", "LogicalRewritingRule", **dres)
            ruleid += 1

    load_from_txt_file(p, os.path.join(data_path,  "pronouns","personal_pronouns.txt"), ["Pronoun", "PersonalPronoun"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "pronouns","demonstrative_pronouns.txt"), ["Pronoun", "DemonstrativePronoun"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "pronouns","relative_pronouns.txt"), ["Pronoun", "RelativePronoun"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "pronouns","indefinite_pronouns.txt"), ["Pronoun", "IndefinitePronoun"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "pronouns", "interrogative_pronouns.txt"), ["Pronoun", "InterrogativePronoun"], to_reject)
    load_from_txt_file(p, os.path.join(data_path,  "verbs", "semi_modal_verbs.txt"), ["Verb", "SemiModalVerb"], to_reject)


    p.create_concept("world", ["Noun"])
    p.create_concept("picture", ["Noun"])
    p.create_concept("hectic", "Adjective")
    p.create_concept("beautiful", "Adjective")
    p.create_concept("fabulous", "Adjective")
    p.create_concept("center", "Adjective")
    p.create_concept("centre", "Adjective")
    p.create_relationship_instance("center", "eqTo", "centre", True)
    p.create_concept("busy", "Adjective")
    p.create_concept("crowded", "Adjective")
    p.create_concept("fast", "Adjective")
    p.create_concept("busy", "Adjective")
    p.create_concept("slow#adj", "Adjective", entity_name="slow")
    p.create_concept("slow#v", "Verb", entity_name="slow")
    p.create_relationship_instance("slow#v", "adjectivalForm", "slow#adj")
    p.create_relationship_instance("slow#adj", "neqTo", "fast", True)
    p.create_concept("crowd#n", "Noun", entity_name="crowd")
    p.create_concept("crowd#v", "Verb", entity_name="crowd")
    p.create_relationship_instance("busy", "relatedTo", "crowd#n", True)
    p.create_relationship_instance("crowd#n", "relatedTo", "crowded", True)
    p.create_relationship_instance("crowd#v", "relatedTo", "crowded", True)
    p.create_concept("city", "LOC")
    p.create_concept("Newcastle", "GPE")
    p.create_relationship_instance("Newcastle", "isA", "city")
    p.create_concept("come back#v", "Verb", entity_name="come back")
    p.create_concept("traffic#v", "Verb", entity_name="traffic")
    p.create_concept("traffic#n", "Noun", entity_name="traffic")
    p.create_concept("flow in", "Verb")
    p.create_concept("flow#v", "Verb", entity_name="flow")
    p.create_relationship_instance("flow#v", "adjectivalForm", "fast")
    p.create_concept("flow#n", "Noun", entity_name="flow")
    p.create_concept("congestion", ["Noun"])
    p.create_concept("jam", ["Noun"])
    p.create_concept("busy city", ["Noun"], hasAdjective="busy", entryPoint="city")
    p.create_concept("traffic jam", ["Noun"], composite_with=["traffic#n", "jam"], entryPoint="traffic#n")
    p.create_concept("traffic congestion", ["Noun"], composite_with=["traffic#n", "congestion"], entryPoint="traffic#n")
    p.create_relationship_instance("traffic jam", "eqTo", "traffic congestion", True)
    p.create_relationship_instance("traffic jam", "eqTo", "traffic congestion", True)
    p.create_concept("flow fast", "CompoundForm", hasAdjective="fast", entryPoint="flow#v")
    p.create_relationship_instance("flow in", "eqTo", "flow#v", True)
    p.create_concept("traffic jam can slow traffic", "CompoundForm", entryPoint="slow", subject="traffic jam", d_object="traffic#n")
    p.create_concept("city centers", "LOC", hasAdjective="center", entryPoint="city")
    p.create_concept("city centres", "LOC", hasAdjective="centre", entryPoint="city")
    p.create_concept("city center", "LOC", hasAdjective="center", entryPoint="city")
    p.create_concept("city centre", "LOC", hasAdjective="centre", entryPoint="city")
    p.create_relationship_instance("city", "hasProperty", "busy", True)
    p.create_relationship_instance("city center", "partOf", "city")
    p.create_relationship_instance("city center", "eqTo", "city centre", True)
    p.create_relationship_instance("city centre", "partOf", "city")
    p.create_relationship_instance("city centers", "partOf", "city")
    p.create_relationship_instance("city centres", "partOf", "city")
    p.create_relationship_instance("city center", "eqTo", "city centers", True)
    p.create_relationship_instance("city center", "eqTo", "city centres", True)
    p.create_relationship_instance("city centre", "eqTo", "city centers", True)
    p.create_relationship_instance("city centre", "eqTo", "city centres", True)
    p.create_relationship_instance("city centers", "eqTo", "city centres", True)
    p.create_relationship_instance("busy", "relatedTo", "crowd#n", True)
    p.create_relationship_instance("congestion", "relatedTo", "traffic congestion", True)
    p.create_relationship_instance("crowd#n", "relatedTo", "congestion", True)
    p.create_relationship_instance("busy city", "relatedTo", "crowd#n", True)
    p.create_relationship_instance("traffic jam", "capableOf", "traffic jam can slow traffic")
    p.create_relationship_instance("hectic", "hasProperty", "traffic#n", True)
    p.create_relationship_instance("hectic", "eqTo", "busy", True)

    ## This is a tumor: single entity match in post-processing
    p.create_concept("embryoma_of_the_kidney#n", "Noun", entity_name="embryoma of the kidney")

    ## These are the examples leading to swapped specification properties via nmod, so, not specification(front,letter) as per nmod, but swapped specification(letter,front)
    p.create_concept("letter#n", "Noun", entity_name="letter")
    p.create_concept("front#n", "Noun", entity_name="front")
    p.create_relationship_instance("letter#n", "hasProperty", "front#n") ## Example of inverse occurrence of the relationship if compared to the nmod (isSymmetricalIfComparedToNMod,hasNModPartOf)
    p.create_concept("street#n", "Noun", entity_name="street")
    p.create_concept("corner#n", "Noun", entity_name="corner")
    p.create_relationship_instance("street#n", "hasProperty", "corner#n")
    p.create_concept("cell_division#n", "Noun", entity_name="cell division")
    p.create_concept("phase#n", "Noun", entity_name="phase")
    p.create_relationship_instance("cell_division#n", "hasProperty", "phase#n")
    p.create_concept("object#n", "Noun", entity_name="object")
    p.create_concept("surface#n", "Noun", entity_name="surface")
    p.create_relationship_instance("object#n", "hasProperty", "surface#n")
    p.create_concept("game#n", "Noun", entity_name="game")
    p.create_concept("chess#n", "Noun", entity_name="chess")
    p.create_relationship_instance("chess#n", "isA", "game#n") #(isSymmetricalIfComparedToNMod,hasNModIsA)

    p.serialize("parmenides.ttl")