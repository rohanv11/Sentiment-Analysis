
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


# lists of words to use
positive_words = []
with open("data_files/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("data_files/negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word):
    new_word = word.strip()
    for char in punctuation_chars:
        new_word=new_word.replace(char,"")        
    return new_word

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



#get tweets from project_twitter_data.csv
twitter_data = open('data_files/project_twitter_data(synthetic_data).csv',"r")
#header : the text of a tweet, the number of retweets of that tweet, 
#         and the number of replies to that tweet


#file to write the new dat
file_ref = open("resulting_data.csv","w")
columns = ["Number of Retweets","Number of Replies","Positive Score",
           "Negative Score","Net Score"]
file_ref.write(", ".join(columns)+"\n")

#first line of twitter csv
header_twitter_data = twitter_data.readline()
#print(header_twitter_data+"hitherer")


#logic to classify data into positive and negative sentiments and add to resulting_data.csv
for line in twitter_data.readlines():
    ## line is a string containing the \n character at the end
    line = line.strip().lower()
    columns = line.split(",")
    ##columns[0] = tweet text
    ##columns[1] = retweet count
    ##columns[2] = reply count
    
    number_of_retweets = columns[1] 
    
    number_of_replies = columns[2] 
    
    positive_score=get_pos(columns[0])
    
    negative_score=get_neg(columns[0])
    
    net_score = positive_score - negative_score
    
    file_ref.write(number_of_retweets+", ")
    file_ref.write(number_of_replies+", ")
    file_ref.write(str(positive_score)+", ")
    file_ref.write(str(negative_score)+", ")
    file_ref.write(str(net_score))
    file_ref.write("\n")
    


file_ref.close()
twitter_data.close()
