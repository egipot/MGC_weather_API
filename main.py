from flask import Flask, render_template
import pandas

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/store/')
def store():
    return render_template('store.html')

@app.route('/api/v1/<station>/<date>')
def home_api(station, date):
    df = pandas.read_csv("")
    temperature = df.station(date)
    return {"station:" : station, 
            "date:" : date, 
            "temperature:" : temperature}
    #render_template('home-api.html')


if __name__ == "__main__":
    app.run(debug=True)



