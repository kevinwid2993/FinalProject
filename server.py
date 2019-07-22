from flask import Flask, request, render_template , jsonify
import requests
import joblib as jb

app = Flask(__name__, static_url_path='') 

#home route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods = ['GET','POST'])
def result():
    if request.method == 'POST':
        Name = str(request.form['Name'])
        Age = int(request.form['Age'])
        Points = int(request.form['Points'])
        Blocks = int(request.form['Blocks'])
        Steals = int(request.form['Steals'])
        Assists = int(request.form['Assists'])
        Rebounds = int(request.form['Rebounds'])
    
    prediksi = model.predict([[Age,Points,Blocks,Steals,Assists,Rebounds]])[0]

    if prediksi <= 0:
        prediksi = '47371 (Min salary)'
    elif prediksi >= 37457154:
        prediksi = '37457154 (Max salary)'
    else:
        prediksi
    
    dataHasil = {
        'Name' : Name,
        'Age' : Age, 
        'Points' : Points, 
        'Blocks' : Blocks, 
        'Steals' : Steals, 
        'Assists' : Assists, 
        'Rebounds' : Rebounds, 
        'Prediction' : prediksi
    } 

    return render_template('result.html', Hasil=dataHasil)

@app.route('/displot')
def displot():
    return render_template('displot.html')

@app.route('/heatmap')
def heatmap ():
    return render_template('heatmap.html')

if __name__=='__main__':
    model = jb.load('modeljoblib')
    app.run(debug=True)