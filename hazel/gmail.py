import smtplib
import getpass

def mail():

	print("\033[1;34;1m")
	print("\nHazel : Currently I support sending mail only through Gmail client. Use your gmail account.")
	print("\033[1;32;1m")
	gmail_user = input("\n        Enter your Google mail-id : ")
	if not gmail_user:
		print("\033[1;34;1m")
		print("\n        Let's try that again. I don't think it's possible to send a mail without the sender id!")
		print("\033[1;32;1m")
		gmail_user = input("\n        Enter your Google mail-id (again) : ")
		if not gmail_user:
			print("\033[1;34;1m")
			print("\nHazel : You did'nt enter a value")
			return
	gmail_password = getpass.getpass("\n        Enter your Google password : ")
	if not gmail_password:
		print("\033[1;34;1m")
		print("\n        Let's try that again. You kind of skipped that one. In a real world, passwords do exist!!! LOL...")
		print("\033[1;32;1m")
		gmail_password = getpass.getpass("\n        Enter your Google password (once more pls) : ")
		if not gmail_password:
			print("\033[1;34;1m")
			print("\nHazel : You did'nt enter a value")
			return
	sent_from = gmail_user  
	to = input("\n        Enter the mail-id of the reciever : ")
	if not to:
		print("\033[1;34;1m")
		print("\n        I have a strong feeling that you cannot send a mail to a nobody. Enter a valid recipient mail id")
		print("\033[1;32;1m")
		to = input("\n        Enter the mail-id of the reciever : ")
		if not to:
			print("\033[1;34;1m")
			print("\nHazel : You did'nt enter a value")
			return
	subject = input("\n        Enter the subject of your mail : ")
	if not subject:
		print("\033[1;34;1m")
		print("\n        I'm not forcing anyone to do anything,  but giving a subject to the mail is a good pracitce")
		print("\033[1;32;1m")
		subject = input("\n        Enter the subject of your mail : ")
	body = input("\n        Enter the text to be sent : ")
	if not body:
		print("\033[1;34;1m")
		print("\n        Guess what. An email with no content is no email at all. Add some text so that the recipient can read something")
		print("\033[1;32;1m")
		body = input("\n        Enter the text to be sent : ")
	signature = "Hazel - Linux chatbot and system assistant"
	signature = input("\n        Enter your signature (optional) : ")
	if not signature:
			signature = "Hazel - Linux chatbot and system assistant"
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
	    print ('\nHazel : Email sent to ', to)
	    print("\033[1;37;1m")
	    print('\n\n Summary : \n', email_text)
	except Exception as e: 
		#print("\033[1;34;1m")
	    print("\nHazel : Something went wrong... Check if you entered the right password or Try enabling less secure apps here : https://myaccount.google.com/lesssecureapps")