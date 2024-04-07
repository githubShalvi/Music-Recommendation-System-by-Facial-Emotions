from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
import joblib

app = Flask(__name__)

def get_similar_music(music_name,user_rating):
    # subtract user_rating (used for scaling) by mean of rating to accomodate disliked movies
    similar_score = item_similarity_df[music_name]*(float(user_rating)-2.5)
    similar_music= similar_score.sort_values(ascending=False)
    return similar_music
  
def getRecommendations(music,rating):
    try:
        similar_music= pd.DataFrame()
        similar_music= similar_music.append(get_similar_music(music,rating),ignore_index=True)
        all_recommend = similar_music.sum().sort_values(ascending=False)
        m = all_recommend[0:15].to_string()
        m = m.split("\n")
        l=[]
        for i in m:
            i = i.split("  ")
            l.append(i[0])
        return l
        s = ""
        for i in l:
            s+=i+"  "
        return(s)
    except:
        return("Sorry No suggestions available !")
		
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	df= pd.read_excel("Dataset.xlsx")
	X = df['mood']
	y = df['Label']
	
	cv = CountVectorizer()
	X = cv.fit_transform(X) # Fit the Data
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

	clf = MultinomialNB()
	clf.fit(X_train,y_train)
	clf.score(X_test,y_test)

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect)
	return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
	app.run(debug=True)