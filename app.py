from flask import Flask, request
from flask_graphql import GraphQLView
from flask_cors import CORS
from schema import schema
import smtplib
from email.mime.text import MIMEText
# ---------------------------------------------------------------
def email_send(name,email,body):
    sender = "<email-of-sender>"
    recipient = "<email-of-recipient>"

    msg = MIMEText(f'Name: {name}\nEmail: {email}\n\nMesssage:\n{body}')
    msg["Subject"] = "Email from portfolio website"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("<email-of-sender>", "<email-password>")
        smtp.sendmail(sender, [recipient], msg.as_string())
# --------------------------------------------------------------

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	return 'Hello ProjectAPI'

# GrapghQL Endpoint
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Send email endpoint
@app.route('/send-email', methods=['POST'])
def send_email():
    request_data = request.get_json()
    name = request_data['name']
    email = request_data['email']
    text = request_data['text']
    
    email_send(name, email, text)
    return "Email sent successfully"


if __name__ == '__main__':
    app.run()
