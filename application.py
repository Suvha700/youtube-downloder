from flask import Flask, render_template, request,jsonify,send_file
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from pytube import YouTube
#import pymongo


application= Flask(__name__) # initializing a flask app
app=application
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            youtube_link = request.form['content']
            link=YouTube(youtube_link)
            video=link.streams.get_highest_resolution()
            file=video.download()
            return send_file(file,as_attachment=True)
        
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
 

    else:
        return render_template('index.html')
    
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
	#app.run(debug=True)