import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Example claim and text
claim = "The earth is flat."
text = "The earth is round, as shown by pictures from space."

# Process the claim and text with spaCy
claim_doc = nlp(claim)
text_doc = nlp(text)

# Compare the similarity of the claim and text using spaCy's similarity function
similarity = claim_doc.similarity(text_doc)

# Print the similarity score
print("Similarity score:", similarity)