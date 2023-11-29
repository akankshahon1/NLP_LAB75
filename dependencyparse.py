""" Name: Akanksha Hon
    Roll no:75
    Batch:B-4
    Practical : Dependancy Parsing using spacy"""
import spacy
nlp = spacy.load("en_core_web_sm")
piano_text = "My school starts at 8:00.We always eat dinner together.They take the bus to work. He doesn't like vegetables."
piano_doc = nlp(piano_text)
for token in piano_doc:
    print( f"""
TOKEN: {token.text}
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )
#OUTPUT:
"""
TOKEN: My
token.tag_ = 'PRP$'
token.head.text = 'school'
token.dep_ = 'poss'

TOKEN: school
token.tag_ = 'NN'
token.head.text = 'starts'
token.dep_ = 'nsubj'

TOKEN: starts
token.tag_ = 'VBZ'
token.head.text = 'eat'
token.dep_ = 'nsubj'

TOKEN: at
token.tag_ = 'IN'
token.head.text = 'starts'
token.dep_ = 'prep'

TOKEN: 8:00.We
token.tag_ = 'NNS'
token.head.text = 'at'
token.dep_ = 'pobj'

TOKEN: always
token.tag_ = 'RB'
token.head.text = 'eat'
token.dep_ = 'advmod'

TOKEN: eat
token.tag_ = 'VBP'
token.head.text = 'eat'
token.dep_ = 'ROOT'

TOKEN: dinner
token.tag_ = 'NN'
token.head.text = 'eat'
token.dep_ = 'dobj'

TOKEN: together
token.tag_ = 'RB'
token.head.text = 'eat'
token.dep_ = 'advmod'

TOKEN: .
token.tag_ = '.'
token.head.text = 'eat'
token.dep_ = 'punct'

TOKEN: They
token.tag_ = 'PRP'
token.head.text = 'take'
token.dep_ = 'nsubj'

TOKEN: take
token.tag_ = 'VBP'
token.head.text = 'take'
token.dep_ = 'ROOT'

TOKEN: the
token.tag_ = 'DT'
token.head.text = 'bus'
token.dep_ = 'det'

TOKEN: bus
token.tag_ = 'NN'
token.head.text = 'take'
token.dep_ = 'dobj'

TOKEN: to
token.tag_ = 'TO'
token.head.text = 'work'
token.dep_ = 'aux'

TOKEN: work
token.tag_ = 'VB'
token.head.text = 'take'
token.dep_ = 'xcomp'

TOKEN: .
token.tag_ = '.'
token.head.text = 'take'
token.dep_ = 'punct'

TOKEN: He
token.tag_ = 'PRP'
token.head.text = 'like'
token.dep_ = 'nsubj'

TOKEN: does
token.tag_ = 'VBZ'
token.head.text = 'like'
token.dep_ = 'aux'

TOKEN: n't
token.tag_ = 'RB'
token.head.text = 'like'
token.dep_ = 'neg'

TOKEN: like
token.tag_ = 'VB'
token.head.text = 'like'
token.dep_ = 'ROOT'

TOKEN: vegetables
token.tag_ = 'NNS'
token.head.text = 'like'
token.dep_ = 'dobj'

TOKEN: .
token.tag_ = '.'
token.head.text = 'like'
token.dep_ = 'punct'
"""