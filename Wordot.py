from gensim.models import KeyedVectors
import random

model = KeyedVectors.load_word2vec_format("frWac_postag_no_phrase_700_skip_cut50.bin",
                                          binary=True, unicode_errors="ignore")

# Choosing a random word
word = random.choice(model.index_to_key)

# Getting the most similar word of the random one
mostSimilar, similarityOfMostSimilar = model.most_similar(word, topn=1)[0]
print(word)
print(mostSimilar)
print(similarityOfMostSimilar)

# Start of the game
print("Choose a word :")
attempt = input()
if attempt == word:
    print("vous avez gagné")

