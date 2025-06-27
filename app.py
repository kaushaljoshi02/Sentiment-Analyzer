import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        sentiment=request.form.get('Sentiment')
        sid =  SentimentIntensityAnalyzer()
        score =sid.polarity_scores(sentiment)

        print(sentiment)
        print(score)

        if score['neg'] >score['pos'] and score['neu']:
            return render_template("home.html",message='Negative😞 ')
        elif score['pos'] >score['neg'] and score['neu']:
            return render_template("home.html",message='Positive😊')
        else:
            return render_template("home.html",message='Neutral😐')
        
    return render_template("home.html")    

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0')


