def map_to_legal_sections(crime_keywords):
    # Simple keyword to section mapping
    legal_mapping = {
        'steal': 'IPC 379: Punishment for Theft',
        'rob': 'IPC 392: Robbery',
        'assault': 'IPC 351: Assault',
    }
    
    suggested_sections = []
    for keyword in crime_keywords:
        if keyword in legal_mapping:
            suggested_sections.append(legal_mapping[keyword])

    if suggested_sections:
        print("Suggested legal sections:", suggested_sections)
    else:
        print("No matching legal sections found.")
    
    return suggested_sections

# Example usage
# crime_keywords = ['steal']
# map_to_legal_sections(crime_keywords)
