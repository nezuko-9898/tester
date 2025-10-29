# translation model

translate=pipeline('translation_en_to_hi',model='Helsinki-NLP/opus-mt-en-hi')

text='hello my name is morning'
op=translate(text)

print(op)