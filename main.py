from flask import Flask, render_template
import pandas


app = Flask(__name__)

stations = pandas.read_csv('data_small/stations.txt', skiprows=17, index_col=0)
#print specific columns (station ID and station name), removing the rest of columns
#stations = stations[['STAID', 'STANAME                                 ']]

@app.route('/')
def home():
    return render_template('home-api.html', data=stations.to_html())

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
def weather_api_query(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE']=="1860-01-05"]['   TG'].squeeze() / 10
    # print(station)
    # print(temperature)
    #here, get the temperature value based on filtered date 
    #df.loc[df['    DATE']=="1860-01-05"]['   TG'].squeeze() / 10
    
    return {"station:" : station, 
            "date:" : date, 
            "temperature:" : temperature}


@app.route('/api/v1/<station>')
def weather_api_all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient='records')
    return result



@app.route('/api/v1/yearly/<station>/<year>')
def weather_api_all_year(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pandas.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient='records')
    return result



if __name__ == "__main__":
    app.run(debug=True)



