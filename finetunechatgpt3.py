import os
import openai
import header as h

def open_file(filepath):
    with open(filepath, "r", encoding='utf-8') as infile:
        return infile.read()

def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)

api_key = open_file('/home/lillian/git/.config')
openai.api_key = h.openai_api_key

# with open('/home/lillian/git/chatgpt35turbodata.jsonl', 'rb') as file: 
#     response = openai.File.create(
#         file=open("chatgpt35turbodata.jsonl", "rb"),
#         purpose='fine-tune'
#     )

# file_id = response
# print(f"File uploaded successfully with ID: {file_id}")

# response = openai.FineTuningJob.create(
#     training_file="file-P4ZHAjfYLHnrEjWoJyZBOea3", 
#     model="gpt-3.5-turbo"
#     )

print(openai.FineTuningJob.list(limit=2))
#print(response[id])

message = {"role":"user", "content": input("This is the beginning of your chat with AI. [To exit, send \"###\".]\n\nYou:")};

conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]

while(message["content"]!="###"):
    conversation.append(message)
    completion = openai.ChatCompletion.create(model="ft:gpt-3.5-turbo-0613:personal::7zquybeq", messages=conversation) 
    message["content"] = input(f"Assistant: {completion.choices[0].message.content} \nYou: ")
    print()
    conversation.append(completion.choices[0].message)