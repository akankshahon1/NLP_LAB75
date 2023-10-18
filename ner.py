import spacy
raw_text="""Natural language processing (NLP) is a machine learning technology that gives computers the ability to interpret, manipulate, and comprehend human language. Organizations today have large volumes of voice and text data from various communication channels like emails, text messages, social media newsfeeds, video, audio, and more. They use NLP software to automatically process this data, analyze the intent or sentiment in the message, and respond in real time to human communication.
There are 470 illegal structures, including restaurants and cafes, within a 500m radius of the Taj Mahal in Agra. The Archaeological Survey of India (ASI) has lodged FIRs against these encroachments, but local authorities have not taken any action to remove them. ASI officials claim that despite raising the issue multiple times, the encroachments remain. The ASI has the power to issue demolition notices.. """

#Loading only the NER model of spicy.

NER = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])

#Fitting the model on the sample text.

text= NER(raw_text)

#Printing the named entity found by the model in our sample text.

for w in text.ents:
    print(w.text,w.label_)
spacy.displacy.render(text, style="ent",jupyter=True)
spacy.explain(u"NORP")