import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Like other forms of writing, paragraphs follow a standard three-part structure with a beginning middle, and end."
    "These parts are the topic sentence, development and support, and conclusion. "
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)
