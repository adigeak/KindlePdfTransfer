import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os, sys
import shutil
import glob
import json

# Global directories and extensions
Extension = ["*.epub","*.pdf"]

config_filename = "config.json"

def init():
	if not os.path.exists(config_filename):
		print("Config file doesn't exist. Initializing...")
		init_config = {
		"sender_email": "",
		"sender_password": "",
		"receiver_email": "",
		"toBeSent_dir": "toBeSent",
		"sent_dir": "Sent",
			}
		with open(config_filename, "w") as config_file:
			json.dump(init_config, config_file, indent=4)
		
		print("Config file created. Please edit it with your credentials and folder paths.")
		sys.exit(1)
	
	with open(config_filename) as config_file:
		config = json.load(config_file)
		globals().update(config)
		
		if not all(config.values()):
			print("Please fill in all fields in the config file.")
			sys.exit(1)
	
	# Create necessary directories if they don't exist
	for directory in [toBeSent_dir, sent_dir]:
		if not os.path.exists(directory):
			os.makedirs(directory)
			print("Add the file to be sent in the ", toBeSent_dir)

def add_files_to_list(directory, extensions):
    files_list = []
    dCurrent = os.getcwd()
    os.chdir(directory)
    
    for ext in extensions:
        files_list.extend(glob.glob(ext))
          
    os.chdir(dCurrent)
    return files_list

def filling_content():
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Email with Attachment"

    body = "Please find the attached file."
    msg.attach(MIMEText(body, 'plain'))
    return msg

def read_file(file_name, msg):
    abs_file_name = os.path.join(toBeSent_dir, file_name)
    file_extension = os.path.splitext(file_name)[-1]
    
    with open(abs_file_name, "rb") as iFile:
        attachment = MIMEApplication(iFile.read(), _subtype=file_extension)
        attachment.add_header('content-disposition', 'attachment', filename=file_name)
    msg.attach(attachment)

def send_email(msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # For Gmail
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("An error occurred:", str(e))
        return False

def move_file(file_name):
    src = os.path.join(toBeSent_dir, file_name)
    dst = os.path.join(sent_dir, file_name)
    shutil.move(src, dst)

def main():
	
    init()
    
    # Finding files to be sent
    lToBeSent = add_files_to_list(toBeSent_dir, Extension)
    
    # Sending loop
    for file_name in lToBeSent:
        message = filling_content()
        read_file(file_name, message)

        if send_email(message):
            move_file(file_name)
            print("Successfully sent and moved:", file_name)
        else:
            print("Failed to send:", file_name)

if __name__ == "__main__":
    main()
