import spacy

# Load English NLP model
nlp = spacy.load('en_core_web_sm')

def extract_entities(incident_text):
    doc = nlp(incident_text)
    
    # Extract entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("Entities found:", entities)

    # Extract keywords or crime-related terms based on rule-based matching
    crime_keywords = [token.text for token in doc if token.pos_ == 'VERB']
    print("Crime-related terms:", crime_keywords)

    return entities, crime_keywords

# Example usage
# incident_text = "John Doe stole a car on 5th Street in New York City."
# extract_entities(incident_text)
