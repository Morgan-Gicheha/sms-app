from flask import Flask,render_template,redirect,url_for,request,flash
from twilio.rest import Client 
from models.models import Sending
import random

app  = Flask(__name__)

# configuring secret key
app.config['SECRET_KEY']= random.random()

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        reciever=request.form['reciever']
        content_to_send=request.form['content_to_send']

        # calling the sending class
        try:
            send= Sending(body=content_to_send,to=reciever)
            send.send_sms()
            flash('Message sent .','info')
        except Exception:
           flash('An error occured! Retry','Warning')
           
            


    return render_template('home.html')

if __name__ == "__main__":
    app.run()





