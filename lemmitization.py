import spacy
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "Paragraphs are medium-sized units of writing"
    "longer than sentences, but shorter than sections, chapters, or entire works."
      "Because they connect the small ideas of individual sentences to a bigger idea,"
      "paragraph structure is essential to any writing for organization, flow, and comprehension."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")