import smtplib

def mail():

	print("\033[1;34;1m")
	print "\nHazel : Currently I support sending mail only through Gmail client. Use your gmail account."
	print("\033[1;32;1m")
	gmail_user = raw_input("\n        Enter your Google mail-id : ")
	gmail_password = raw_input("\n        Enter your Google password : ")
	sent_from = gmail_user  
	to = raw_input("\n        Enter the mail-id of the reciever : ")
	subject = raw_input("\n        Enter the subject of your mail : ")
	body = raw_input("\n        Enter the text to be sent : ")
	signature = "Hazel - Linux chatbot and system assistant"
	signature = raw_input("\n        Enter your signature (optional) : ")

	email_text = """.
	Subject: %s

	%s



	This mail was sent by %s

	get more details at : http://bit.ly/Hazel-chatbot
	
	----- powered by Hazel ------
	""" % (subject, body, signature)

	try:  
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    server.login(gmail_user, gmail_password)
	    server.sendmail(sent_from, to, email_text)
	    server.close()
	    print("\033[1;34;1m")
	    print '\nHazel : Email sent to ', to
	    print("\033[1;37;1m")
	    print '\n\n Summary : \n', email_text
	except Exception,e: 
		#print("\033[1;34;1m")
	    print "\nHazel : Something went wrong... Try enabling less secure apps here : https://myaccount.google.com/lesssecureapps"