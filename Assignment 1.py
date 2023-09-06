#Assignment no 1
#Name:Akanksha Hon
#Roll no:75
#Batch:B4
#Assignment name:Text processing using sentence detection,stop word removal,lemmitization,pos tagging

#sentence detection
import spacy
nlp = spacy.load("en_core_web_sm") 
about_text = (
    "If men were rational in their conduct, that is to say, if they acted in the way most likely to bring about the ends that they deliberately desire, intelligence would be enough to make the world almost a paradise. "
    "In the main, what is in the long run advantageous to one man is also advantageous to another. But men are actuated by passions which distort their view; feeling an impulse to injure others, they persuade themselves that it is to their interest to do so. "
    "They will not, therefore, act in the way which is in fact to their own interest unless they are actuated by generous impulses which make them indifferent to their own interest."
)
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(f"{sentence[:5]}...")


#output:
# If men were rational in...
# In the main, what...
# But men are actuated by...
# They will not, therefore...


#tokenization
import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Like other forms of writing, paragraphs follow a standard three-part structure with a beginning middle, and end."
    "These parts are the topic sentence, development and support, and conclusion. "
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)
#output:
# Like 0
# other 5
# forms 11
# of 17
# writing 20
# , 27
# paragraphs 29
# follow 40
# a 47
# standard 49
# three 58
# - 63
# part 64
# structure 69
# with 79
# a 84
# beginning 86
# middle 96
# , 102
# and 104
# end 108
# . 111
# These 112
# parts 118
# are 124
# the 128
# topic 132
# sentence 138
# , 146
# development 148
# and 160
# support 164
# , 171
# and 173
# conclusion 177
# . 187



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
     
#Output:

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