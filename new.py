import nltk
from nltk.sentiment
import SentimentIntensityAnalyzer

def get_emotion(text):
    sia=SentimentIntensityAnalyzer()
    sentiment=sia.polarity_scores(text)
    if sentiment['compound']>=0.05:
        return 'Positive'
    elif sentiment['compound']<=-0.05:
        return 'Negative'
    else:
        return 'Neutral'


emotion=get_emotion(user_input)
if emotion=='Positive':
    #recommend happy songs
elif emotion=='Negative':
    #recommend sad songs
else:
    print('process failed')

