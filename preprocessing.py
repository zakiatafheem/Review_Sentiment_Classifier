import re

def clean(doc):
    # Remove special characters and numbers
    doc = re.sub(r'[^a-zA-Z\s]', '', doc)
    
    # Convert to lowercase
    doc = doc.lower()
    
    # Remove extra spaces
    doc = re.sub(r'\s+', ' ', doc).strip()
    
    return doc