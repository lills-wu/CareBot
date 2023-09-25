import streamlit as st
import os
import openai
import header as h

openai.api_key = h.openai_api_key

st.set_option('deprecation.showfileUploaderEncoding', False)


st.title("Chatbot App")

# Function to get chatbot response
def get_chatbot_response(conversation):
    completion = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::7zquybeq",
        messages=conversation
    )
    return completion.choices[0].message.content

# Initialize conversation
conversation = [{"role": "system", "content": "DIRECTIVE_FOR_gpt-3.5-turbo"}]

input_message = ""
while input_message != "###":
    input_message = st.text_area("You:", value=input_message, height=100)

    if st.button("Send") or (input_message and st.session_state.enter_pressed):
        conversation.append({"role": "user", "content": input_message})
        bot_response = get_chatbot_response(conversation)
        st.text_area("Assistant:", value=bot_response, height=100)
        input_message = ""

    st.session_state.enter_pressed = False 


