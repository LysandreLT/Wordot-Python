from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format("frWac_postag_no_phrase_700_skip_cut50.bin",
                                          binary=True, unicode_errors="ignore")

print(model.most_similar("voiture_n"))
