'''
Role this file will be:

[An NLP model]
User topic
↓
Important concepts extract
↓
List return


for example:
if we give input:
      Explain Newton's First Law
then Output should be:
     ["newton", "law", "object", "force", "motion"]

'''

# Don't use latest python version, insted install Python 3.11.0b4

# pip install spacy (Install this library) just copy paste in terminal
# python -m spacy download en_core_web_sm (intall this language model)just copy paste in terminal


import spacy

# load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_concepts(text):
    doc = nlp(text)

    concepts = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            concepts.append(token.text.lower())

    return concepts

if __name__ == "__main__":
    topic = "Explain Newton's First Law of Motion"

    result = extract_concepts(topic)

    print("Concepts:", result)