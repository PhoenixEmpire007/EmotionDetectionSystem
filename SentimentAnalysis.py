from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
paragraph = "It was one of the worst movies I've seen, despite good reviews. \
Unbelievably bad acting!! Poor direction. VERY poor production. \
The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"


lines_list = tokenize.sent_tokenize(paragraph)
print(lines_list)

for sentence in lines_list:
    sid = SentimentIntensityAnalyzer()
    #print(sentence)

    ss = sid.polarity_scores(sentence)
    #print(ss)
    k=ss.keys()
    p=list(k)
    #print("P=",p)
    print("Negative:",ss.get(p[0]),",Neutral:",ss.get(p[1]),",Positive:",ss.get(p[2]),",Sent:",sentence)