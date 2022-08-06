import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('wordIndex.json') as json_file:
  word_index = json.load(json_file)
  tokenizer.word_index = word_index

def SentenceToToken(sentence):
    tokenized_sentence = okt.morphs(sentence, stem=True) # 토큰화
    stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
    token=[]
    token.append(tokenizer.texts_to_sequences(stopwords_removed_sentence))
    token=pad_sequences(token, maxlen=55)
    token=token.reshape(1,55)
    return token