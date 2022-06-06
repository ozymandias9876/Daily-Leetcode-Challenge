from mailjet_rest import Client
from leetcode import *
import os
api_key = '049ae4f1e0a2b8d6e26ec15ef491b6b2'
api_secret = 'b2c5be0108c96ef7ddfd645a07d08bf6'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "himanshutiwarihouse@gmail.com",
        "Name": "Himanshu"
      },
      "To": [
        {
          "Email": "bhawna2907kumari@gmail.com",
          "Name": "Bhawna Kumari"
        }
      ],
      "Subject": "Greetings from Himanshu.",
      "TextPart": "Daily Leetcode Challenge",
      "HTMLPart": "<h1>Daily Leetcode Challenge</h1>""<h3>Dear User,welcome, i encourage  you to join me <a href='https://www.linkedin.com/in/himanshu3wari/'>Himanshu</a>!</h3><br />Wish you a happy day!"
                    "<p>Here's your daily leetcode challenge <a href={}>question</a>".format(today_problem),
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
