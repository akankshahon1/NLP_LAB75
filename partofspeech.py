import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
     "Paragraphs are medium-sized units of writing, longer than sentences, but shorter than sections, chapters, or entire works. Because they connect the “small” ideas of individual sentences to a “bigger” idea, "
     "paragraph structure is essential to any writing for organization, flow, and comprehension"
 )
about_doc = nlp(about_text)
for token in about_doc:
     print(
         f"""
 TOKEN: {str(token)}
 
 TAG: {str(token.tag_):10} POS: {token.pos_}
 EXPLANATION: {spacy.explain(token.tag_)}"""
    )