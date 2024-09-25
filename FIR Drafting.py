def draft_fir(incident_text, legal_sections):
    fir_draft = f"Incident Description:\n{incident_text}\n\nRelevant Legal Sections:\n"
    fir_draft += "\n".join(legal_sections)
    return fir_draft

# Example usage
# incident_text = "John Doe stole a car on 5th Street."
# legal_sections = ['IPC 379: Punishment for Theft']
# fir = draft_fir(incident_text, legal_sections)
# print(fir)
