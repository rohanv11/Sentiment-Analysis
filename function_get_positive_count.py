
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(word):
    new_word = word.strip()
    for char in punctuation_chars:
        new_word=new_word.replace(char,"")        
    return new_word


    
    
# list of positive words to use
positive_words = []
with open("data_files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(sentence):
    #convert sentence to lower case
    sentence=sentence.lower()
    words_in_sentence = sentence.split()
    count_of_posi_words=0
    
    for word in words_in_sentence:
        #get rid of punctuations
        word = strip_punctuation(word)
        if word in positive_words:
            count_of_posi_words+=1
    return count_of_posi_words

