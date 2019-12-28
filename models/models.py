from twilio.rest import Client


class Sending:
    ''' this model is for sending sms with twilio'''
    from_='+1562*******'
    
    account_sid = 'AC2337805f2c4adaf746eb*********'
    auth_token = '40c*****************************'
      
    def __init__(self,body,to):
            self.body=body
            self.to=to

    '''verification function. it verifies twilio credentials'''
    def verify(self):
        pass

    def send_sms(self):
        
        client=Client(self.account_sid,self.auth_token)
        print('auths recieved')
        message= client.messages.create(self.to ,from_=self.from_,body=self.body)
        print('message sent')








        
    