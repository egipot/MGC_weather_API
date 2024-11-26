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
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']=="1860-01-05"]['   TG'].squeeze() / 10
    print(station)
    print(temperature)
    
    #here, get the temperature value based on filtered date 
    #df.loc[df['    DATE']=="1860-01-05"]['   TG'].squeeze() / 10
    
    #temperature = df.station(date)
    return {"station:" : station, 
            "date:" : date, 
            "temperature:" : temperature}
    #render_template('home-api.html')


if __name__ == "__main__":
    app.run(debug=True)



