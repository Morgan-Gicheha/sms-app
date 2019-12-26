from flask import Flask,render_template,redirect,url_for,request
from twilio.rest import Client 

app  = Flask(__name__)

# twillio credentials
# encrypted username/number
account_sid = "AC2337805f2c4adaf746eb84920714cd43"
# password
auth_token = "715b64a0c4c6ea0603b5556b9c75b035"
print("auths recievd from twilio")
client = Client(account_sid, auth_token)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        reciever=request.form['reciever']
        content_to_send=request.form['content_to_send']
        recieverr=reciever
        content_to_send=content_to_send
        to='+15627312373'
        # print('recieved')
        messsage = client.messages.create(recieverr, to, content_to_send)
        print('message sent')

    return render_template('home.html')

if __name__ == "__main__":
    app.run()

# from twilio.rest import Client

# # encrypted username/number
# account_sid = "AC2337805f2c4adaf746eb84920714cd43"
# # password
# auth_token = "715b64a0c4c6ea0603b5556b9c75b035"
# print("auths recievd")
# client = Client(account_sid, auth_token)

# messsage = client.messages.create(to="+254798863355", from_="+15627312373", body="ni sphy")

# print(messsage.sid)
# print('message don')


