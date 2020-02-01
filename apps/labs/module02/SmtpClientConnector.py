'''
Created on Jan 22, 2020

@author: pallaksingh
'''
#import required libraries
from labs.common            import ConfigUtil
from email.mime.multipart   import MIMEMultipart
from email.mime.text        import MIMEText
import smtplib

class SmtpClientConnector(object):
    '''
    classdocs
    '''
    #instantiate ConfigUtil for reading SMTP configuration from config file
    config = ConfigUtil.ConfigUtil()

    #empty constructor as no extra params needed
    def __init__(self):
        '''
        Constructor
        '''
            
        pass
    
    #method for sending email 
    def publishMessage(self, topic, data):
        
        '''
            Setting up attributes for sending e-mail notification
        '''
        
        #getting host and port number for opening socket connection
        host = self.config.getValue('smtp.cloud', 'host')
        port = self.config.getIntegerValue('smtp.cloud', 'port')
        
             
        #getting sender and receiver credentials from configuration file
        fromAddr = self.config.getValue('smtp.cloud', 'fromAddr')
        toAddr = self.config.getValue('smtp.cloud', 'toAddr')
            
        #getting sender's password from configuration file
        authToken = self.config.getValue('smtp.cloud', 'authToken')
            
        #initialize the email body
        msg = MIMEMultipart()
            
        #defining the message attributes
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
            
        #define the message body
        msgBody = data
    
        #attach the message body to the message
        msg.attach(MIMEText(msgBody))
            
        #convert the message from MIME format type to string type to sent via email
        msgText = msg.as_string()
            
        '''
            Sending e-mail Notification
        '''
        try: 
            #instantiating SMTP connection
            smtpServer = smtplib.SMTP_SSL(host,port)
                
            #identifying self to SMTP server using ehlo
            smtpServer.ehlo()
                
            #login to the SMTP server using credentials defined above
            smtpServer.login(fromAddr, authToken)
                
            #send the mail 
            smtpServer.sendmail(fromAddr, toAddr, msgText)
                
            #close the SMTP connection
            smtpServer.close()
            
        #if encountered an error
        except:
                
            #return false indicating failure to publishing Message
            return False
            
        #return true indicating success in publishing Message
        return True
        

        
        
            
             
            
            
            
        
        
        
        
        
        