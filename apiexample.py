import configparser  
config = configparser.ConfigParser()
config.read(".config")  
API_KEY = config['DEFAULT']["OPENAI_API_KEY"]


import os
import openai

openai.api_key = API_KEY

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="I'm feeling down today, please give me ideas to improve my mood.",
#   temperature=0.5,
#   max_tokens=100,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
# print(response['choices'][0]['text'])

# response2 = openai.Completion.create(
#     model="davinci:ft-personal-2023-09-02-03-20-58",
#     prompt="I'm feeling frustrated today. Can you give me helpful advice on how to manage it?",
#     max_tokens=20
#     )
# print(response2['choices'][0]['text'])

message = {"role":"user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")};

conversation = [{"role": "system", "content": "You are a mental health counselor who is designed to provide supportive advice for users"}]

while(message["content"]!="###"):
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="davinci:ft-personal-2023-09-02-03-20-58", messages=conversation) 
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou:")
    print()
    conversation.append(completion.choices[0].message)