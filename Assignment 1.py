#Assignment no 1
#Name:Akanksha Hon
#Roll no:75
#Batch:B4
#Assignment name:Text processing using sentence detection,stop word removal,lemmitization,pos tagging


#Lemmatization
#import spacy
import spacy
#load nlp
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "Paragraphs are medium-sized units of writing"
    "longer than sentences, but shorter than sections, chapters, or entire works."
      "Because they connect the small ideas of individual sentences to a bigger idea,"
      "paragraph structure is essential to any writing for organization, flow, and comprehension."
)
#lemmatization
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")

#Output:
# Paragraphs : paragraph
#            units : unit
#         sentences : sentence
#           shorter : short
#           sections : section
#           chapters : chapter
#              works : work
#           Because : because
#              ideas : idea
#          sentences : sentence
#             bigger : big
#                 is : be

#PartOfspeech pos tagging
import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
     "Paragraphs are medium-sized units of writing. "
     "Because they connect the “small” ideas of individual sentences to a “bigger” idea, "
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
     
Output:

#       TOKEN: Paragraphs
 
#  TAG: NNS        POS: NOUN
#  EXPLANATION: noun, plural

#  TOKEN: are
 
#  TAG: VBP        POS: AUX
#  EXPLANATION: verb, non-3rd person singular present

#  TOKEN: medium
 
#  TAG: JJ         POS: ADJ
#  EXPLANATION: adjective (English), other noun-modifier (Chinese)

#  TOKEN: -
 
#  TAG: HYPH       POS: PUNCT
#  EXPLANATION: punctuation mark, hyphen

#  TOKEN: sized
 
#  TAG: JJ         POS: ADJ
#  EXPLANATION: adjective (English), other noun-modifier (Chinese)

#  TOKEN: units
 
#  TAG: NNS        POS: NOUN
#  EXPLANATION: noun, plural

#  TOKEN: of
 
#  TAG: IN         POS: ADP
#  EXPLANATION: conjunction, subordinating or preposition

#  TOKEN: writing
 
#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: .
 
#  TAG: .          POS: PUNCT
#  EXPLANATION: punctuation mark, sentence closer

#  TOKEN: Because
 
#  TAG: IN         POS: SCONJ
#  EXPLANATION: conjunction, subordinating or preposition

#  TOKEN: they
 
#  TAG: PRP        POS: PRON
#  EXPLANATION: pronoun, personal

#  TOKEN: connect
 
#  TAG: VBP        POS: VERB
#  EXPLANATION: verb, non-3rd person singular present

#  TOKEN: the
 
#  TAG: DT         POS: DET
#  EXPLANATION: determiner

#  TOKEN: “
 
#  TAG: ``         POS: PUNCT
#  EXPLANATION: opening quotation mark

#  TOKEN: small
 
#  TAG: JJ         POS: ADJ
#  EXPLANATION: adjective (English), other noun-modifier (Chinese)

#  TOKEN: ”
 
#  TAG: ''         POS: PUNCT
#  EXPLANATION: closing quotation mark

#  TOKEN: ideas
 
#  TAG: NNS        POS: NOUN
#  EXPLANATION: noun, plural

#  TOKEN: of
 
#  TAG: IN         POS: ADP
#  EXPLANATION: conjunction, subordinating or preposition

#  TOKEN: individual
 
#  TAG: JJ         POS: ADJ
#  EXPLANATION: adjective (English), other noun-modifier (Chinese)

#  TOKEN: sentences
 
#  TAG: NNS        POS: NOUN
#  EXPLANATION: noun, plural

#  TOKEN: to
 
#  TAG: IN         POS: ADP
#  EXPLANATION: conjunction, subordinating or preposition

#  TOKEN: a
 
#  TAG: DT         POS: DET
#  EXPLANATION: determiner

#  TOKEN: “
 
#  TAG: ``         POS: PUNCT
#  EXPLANATION: opening quotation mark

#  TOKEN: bigger
 
#  TAG: JJR        POS: ADJ
#  EXPLANATION: adjective, comparative

#  TOKEN: ”
 
#  TAG: ''         POS: PUNCT
#  EXPLANATION: closing quotation mark

#  TOKEN: idea
 
#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: ,
 
#  TAG: ,          POS: PUNCT
#  EXPLANATION: punctuation mark, comma

#  TOKEN: paragraph
 
#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: structure
 
#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: is
 
#  TAG: VBZ        POS: AUX
#  EXPLANATION: verb, 3rd person singular present

#  TOKEN: essential
 
#  TAG: JJ         POS: ADJ
#  EXPLANATION: adjective (English), other noun-modifier (Chinese)

#  TOKEN: to
 
#  TAG: IN         POS: ADP
#  EXPLANATION: conjunction, subordinating or preposition

#  TOKEN: any
 
#  TAG: DT         POS: DET
#  EXPLANATION: determiner

#  TOKEN: writing
 
#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: for
 
#  TAG: IN         POS: ADP
#  EXPLANATION: conjunction, subordinating or preposition

#  TOKEN: organization
 
#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: ,
 
#  TAG: ,          POS: PUNCT
#  EXPLANATION: punctuation mark, comma

#  TOKEN: flow
 
#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass

#  TOKEN: ,
 
#  TAG: ,          POS: PUNCT
#  EXPLANATION: punctuation mark, comma

#  TOKEN: and
 
#  TAG: CC         POS: CCONJ
#  EXPLANATION: conjunction, coordinating

#  TOKEN: comprehension
 
#  TAG: NN         POS: NOUN
#  EXPLANATION: noun, singular or mass