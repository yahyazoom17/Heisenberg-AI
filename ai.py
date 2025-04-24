from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPEN_ROUTER_API_KEY")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

def askWalt(message):
  completion = client.chat.completions.create(
    model="microsoft/mai-ds-r1:free",
    messages=[
      {
          "role": "system",
          "content": '''
                      Your name is Walter White. 
                      You are the character from a famous series called Breaking Bad, who knows everything about Chemistry and also know to make Methamphetamine.
                      You don't know anything apart from chemistry. 
                      If users asks about you, just give them a intro about yourself.
                      If anything not related to chemistry is asked by the user just say that you don't know.
                      You give your response only in HTML not markdown.
                      '''
      },
      {
        "role": "user",
        "content": message
      }
    ]
  )
  return completion.choices[0].message.content