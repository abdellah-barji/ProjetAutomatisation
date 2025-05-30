# Weather SMS Notifier

A simple Python script that fetches the current weather using [wttr.in](https://wttr.in) and sends it as an SMS via the Twilio API. If it’s raining, the script will print a warning and still send the weather report.

---

## 📋 Prerequisites

- Python 3.7+
- A [Twilio](https://www.twilio.com/) account with:
  - **Account SID**
  - **Auth Token**
  - A valid Twilio phone number

---

## 🚀 Installation


____________________________________________________

Install dependencies

pip install requests twilio selenium

____________________________________________________
Add your Twilio credentials and phone numbers

Open the Python script and replace the following variables with your actual data:

account_sid = "your_account_sid"
auth_token = "your_auth_token"
from_ = "your_twilio_phone_number"
to = "recipient_phone_number"
