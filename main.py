from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()  # Enable encryption

    # Login credentials
    username = 'mark.myfiles@outlook.com'
    password = 'M@estro2'

    # Login to the server
    server.login(username, password)

    # Email content
    msg = MIMEMultipart()
    msg['From'] = 'Mark'
    msg['To'] = 'mark.myfiles@outlook.com'
    msg['Subject'] = 'File Sent'

    # Retrieve custom text from the form
    custom_text = request.form['custom_text']
    msg.attach(MIMEText(custom_text, 'plain'))

    # Get the uploaded file
    uploaded_file = request.files['file']
    filename = uploaded_file.filename

    # Attach file
    file_content = uploaded_file.read()
    attachment = MIMEApplication(file_content)
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(attachment)

    # Send the email
    server.sendmail(username, 'mark.myfiles@outlook.com', msg.as_string())

    # Quit the server
    server.quit()

    return 'Email sent successfully!'
