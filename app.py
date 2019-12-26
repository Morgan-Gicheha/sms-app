from flask import Flask,render_template,redirect,url_for,request
from twilio.rest import Client 

app  = Flask(__name__)

# twillio credentials
# encrypted username/number
account_sid = "AC*******************"
# password
auth_token = "71********************"
print("auths recievd from twilio")
client = Client(account_sid, auth_token)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        reciever=request.form['reciever']
        content_to_send=request.form['content_to_send']
        recieverr=reciever


    return render_template('home.html')

if __name__ == "__main__":
    app.run()





