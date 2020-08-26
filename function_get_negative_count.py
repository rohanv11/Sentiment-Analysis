
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    new_word = word.strip()
    for char in punctuation_chars:
        new_word=new_word.replace(char,"")        
    return new_word

negative_words = []
with open("data_files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(sentence):
    #convert sentence to lower case
    sentence=sentence.lower()
    words_in_sentence = sentence.split()
    count_of_neg_words=0
    
    for word in words_in_sentence:
        #get rid of punctuations
        word = strip_punctuation(word)
        if word in negative_words:
            count_of_neg_words+=1
    return count_of_neg_words