# Sending PDF Files to Amazon Kindle

This script allows you to send PDF files to your Amazon Kindle device through email. The script uses your Gmail account to send the emails with attached PDF files. The process involves setting up your email credentials, configuring directories, and running the script.

## Prerequisites

- Python 3.x installed on your computer.
- A Gmail account to send emails.
- An Amazon Kindle device with the "Send-to-Kindle" email address configured.

## Setup

1. Clone or download this repository to your computer.

2. Run the script.
    ```python sendkindle.py```
3. Edit the config.json file:
    Set "sender_email": Your Gmail email address.
    Set "sender_password": Your Gmail email password or an App Password.
    Set "receiver_email": Your Kindle's "Send-to-Kindle" email address.
    Set "toBeSent_dir": The directory where you place the PDF files you want to send.
    Set "sent_dir": The directory where sent PDF files will be moved.

## Usage

1. Place the PDF files you want to send to your Kindle in the toBeSent directory.
2. Open a terminal/command prompt and navigate to the script directory:
```cd path/to/script```
3. Run the script:
```python sendkindle.py```
4. The script will send each PDF file as an email attachment to your Kindle's email address. Successfully sent files will be moved to the Sent directory.
5. Check your Kindle device. The sent PDF files should appear in your Kindle library shortly.
