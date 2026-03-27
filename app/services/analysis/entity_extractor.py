import spacy
from app.models.analysis import ExtractedEntities
import logging

logger = logging.getLogger("ainews.analysis.extractor")

class EntityExtractor:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            logger.warning("Spacy model 'en_core_web_sm' not found. Downloading it is required.")
            self.nlp = None

    def extract_entities(self, text: str) -> ExtractedEntities:
        """Uses local SpaCy NLP to extract deterministic entities from text."""
        result = ExtractedEntities(persons=[], organizations=[], locations=[], events=[])
        if not self.nlp or not text:
            return result

        doc = self.nlp(text)
        
        persons = set()
        orgs = set()
        locs = set()
        events = set()

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                persons.add(ent.text)
            elif ent.label_ in ["ORG", "COMPANY"]:
                orgs.add(ent.text)
            elif ent.label_ in ["GPE", "LOC", "FAC"]:
                locs.add(ent.text)
            elif ent.label_ == "EVENT":
                events.add(ent.text)

        result.persons = list(persons)
        result.organizations = list(orgs)
        result.locations = list(locs)
        result.events = list(events)
        
        return result

entity_extractor = EntityExtractor()
