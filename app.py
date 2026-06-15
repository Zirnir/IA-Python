#import
from sklearn.feature_extraction.text import CountVectorizer

#Phrase de référance et correspondance morale

sentence = [
    "J'aime le projet",
    "C'est très facile",
    "Parfait",
    "Je déteste ce bug",
    "C'est nul",
    "Je n'aime pas ce projet"
]

moral = [1, 1, 1, 0, 0, 0]

#Vectoriseur

    #Découpeur et référenciel de mots

translator = CountVectorizer()

    #Lecture des phraseset assignation de score aux mots

word_to_nb = translator.fit_transform(sentence)



#Test
print(translator.vocabulary_)