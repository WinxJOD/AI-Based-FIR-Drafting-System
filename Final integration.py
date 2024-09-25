def process_fir():
    # Step 1: Speech-to-text (or text input)
    incident_text = speech_to_text()  # Or get text input from user
    
    # Step 2: NLP Parsing
    entities, crime_keywords = extract_entities(incident_text)
    
    # Step 3: Map to legal sections
    legal_sections = map_to_legal_sections(crime_keywords)
    
    # Step 4: Draft FIR
    fir = draft_fir(incident_text, legal_sections)
    print("Generated FIR Draft:\n", fir)

# Run the system
process_fir()
