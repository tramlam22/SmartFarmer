import smtplib

def sendAlert (curr_user, msg):

    #email properties
    sent_from = "153berkeley@gmail.com"
    to = 'tramphuonglam@gmail.com'
    subject = "Farm Alert"

    #email send request
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()

        #login to sender acc
        server.login("153berkeley@gmail.com", "A406Roomies")

        #send email
        msg = 'Subject:{}\n\n{}'.format(subject,msg)
        server.sendmail(sent_from, to, msg)
        server.close()

        print ('Email sent!')
    except Exception as e:
        print(e)
        print ('Something went wrong...')