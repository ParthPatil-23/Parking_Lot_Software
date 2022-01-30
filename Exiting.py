# NOTE : Sender's Email and password are not provided in the code for Security reasons 
# to send OTP kindely Enter Email ID and Password on line 126 and 129
# Or the Program will not Run

from tabulate import tabulate
import time
from random import randint
import smtplib
import ssl
from email.message import EmailMessage


EXIT = input("Enter your Parking lot :- ")
EXIT = EXIT + ".txt"


LOT_FILE = open(EXIT,"r").read()

file = LOT_FILE.split(',')


sec1 = time.time()

sec = file[2]

time = sec1 - float(sec)
print(int(time))

time = int(time) / 60 / 60

price = time * 2
print(price)

print("\n1. Pay Now !!")
print("\n2. Sign In")
print("\n3. Sign Up")


a = True
b = True
c = True

import time
while(b):
	operation = int(input("\nselect the no. :- "))
	if operation == 1:
		print("\nPayment Sucessful for $",price,)
		b = False
		pass

	if operation == 2:
		b = False
		while(a):
			email = input("\nEnter your email address :- ")
			password = input("\nEnter your Password :- ")
			email1 = email+".txt"
			try:
				SIGN_IN = open(email1,"r").read()
				SIGN_IN1 = SIGN_IN.split(",")
				if SIGN_IN1[3] == password:
					print("\nPayment Sucessful")
					a = False
				else:
					print("\nThe Password you entered do not match")
			except:
				try:
					if password == "Forget":
						print("\n","we will soon contact you")
						print("\n","Paying Now")
						print("\n","processing ...")
						time.sleep(3)
						print("\nPayment Sucessful")
						break


					if password == "forget":
						print("\n","we will soon contact you")
						print("\n","Paying Now")
						print("\n","processing ...")
						time.sleep(3)
						print("\nPayment Sucessful")
						break
						
					if password == "FORGET":
						print("\n","we will soon contact you")
						print("\n","Paying Now")
						print("\n","processing ...")
						time.sleep(3)
						print("\nPayment Sucessful")
						break
				except:
					print("\nNo Account found with this credential")



	if operation == 3:
		b = False
		name = input("\nEnter you Name :- ")
		email = input("\nEnter your email address :- ")
		while(a):
			password = input("\nCreate Password :- ")
			password1 = input("\nReenter your password :- ")
			if password == password1:
				a = False
			else:
				print("\nThe Password you enter do not match the above one")
		name1 = email+".txt"
		SIGN_UP = open(name1,"a")
		SIGN_UP.write(name)
		SIGN_UP.write(",")
		SIGN_UP.write(email)
		SIGN_UP.write(",")
		SIGN_UP.write(password)

		# Sending OTP on the Email
		def random_with_N_digits(n):
			range_start = 10**(n-1)
			range_end = (10**n)-1
			return randint(range_start, range_end)

		OTP = random_with_N_digits(3)

		Subject = "Verification Email"
		body = ("Your Verification code for the Parking lot is "+ str(OTP))

		sender_email = ""  # Please enter your email here as senders Email
		reciver_email = email

		password = ""  # Please Enter your Sender's Email password here

		message = EmailMessage()
		message["From"] = sender_email
		message["To"] = reciver_email
		message["Subject"] = Subject
		message.set_content(body)

		context = ssl.create_default_context()

		print("Sending Email ...")
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
		    server.login(sender_email,password)
		    server.sendmail(sender_email, reciver_email, message.as_string())
		print("Email send Successful !!!")

		while(c):
			OTP1 = int(input("Enter the OTP :- "))
			if OTP1 == OTP:
				print("\n Your Account is successfully created")

				print("\nPlease select your plan :- ")
				plan = [["  $50   ", "  $100   ","   $150   ","   $250   "],
						["2 weeks ", " 1 month ", " 6 weeks ", " 3 Months"]]
				
				head = ["Regular","Silver","Gold","VIP"]
				
				# Printing the table of the Parking Lot
				print(tabulate(plan, headers = head, tablefmt = "grid"))	

				select_plan = input("\nEnter your plan in $")
				print("\n processing ...")
				time.sleep(3)

				print("\n","Payment Sucessful ")
				c = False
			else:
				print("\nThe OTP you entered is not correct")	
		

	else:
		print("\n","Please enter numbers between 1 to 3")

print("\nThank You Visit Again !!")