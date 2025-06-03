from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)