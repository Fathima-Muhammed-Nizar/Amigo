import os
import openai
import gradio as gr

#Open ai api key as environment variable,use
#openai.api_key=os.getenv("OPENAI_API_KEY")

#Open ai Api key as string:
openai.api_key="xxxxx"




start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman:Do you simplify concepts in an understandable way?\nAI:Yeah,you can ask and I will clarify your doubts in a way even a five year old can understand.(NOTE:IF YOU WANT TO GET VERY SIMPLE EXPLANATIONS,GO LIKE THIS:EXPLAIN THEORY OF EVOLUTION TO A FIVE YEAR OLD )\nHuman: ",

def openai_create(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
)

    return response.choices[0].text

def chatgpt_clone(input,history):
    history=history or []
    s=list(sum(history,()))
    s.append(input)
    inp=''.join(s)
    output=openai_create(inp)
    history.append((input,output))
    return history,history


block=gr.Blocks()
with block:
    gr.Markdown("""<h1><center>Amigo:Simplifying the Complex,Your Trusted Guide to Clarity & Understanding</center></h1>""")

    chatbot=gr.Chatbot()
    message=gr.Textbox(placeholder=prompt)
    state=gr.State()
    submit=gr.Button("SEND")
    submit.click(chatgpt_clone,inputs=[message,state],outputs=[chatbot,state])

block.launch(debug=True)
