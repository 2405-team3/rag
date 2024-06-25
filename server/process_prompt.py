"""

note: you will need to create a .env file in the root project folder (e.g., same folder with main.py)
it will contain: OPENAI_API_KEY=yourKeyHere

"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

async def process_prompt(query, context):
    messages = create_messages(query, context)
    if len(context) == 0:
      return "There are no parts of the document that match your query. Have you uploaded a pdf yet?"
    else:
      return send_prompt(messages)

def create_messages(query, context):
    return [
        {"role": "system", "content": "You are tasked with utilizing provided context to answer a user's question with a scholarly response."},
        {"role": "system", "content": "Please never use one-word introductory clauses."},
        # {"role": "system", "content": f'Do not use any sources of information outside of this context: {context}'},
        {"role": "system", "content": f'The content you will be using to answer questions is {context}'},
        {"role": "user", "content": f'Extrapolate on but only use the given information to answer this question: {query}'}
    ]

    # preamble = 'Extrapolate on but only use the given information to respond to this question:'
    # messages = []

    # add system role entries
    # for chunk in context['matches']:
    #     messages.append({
    #         'role': 'system',
    #         'content': chunk
    #     })

    # add user role
    # messages.append({
    #     'role': 'user',
    #     'content': f"{preamble} {context['query']}"
    # })

    # return messages



def send_prompt(returned_messages):
    print('connecting to openai client...')
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    print('connected. sending prompt...')
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=returned_messages
    )

    return completion.choices[0].message.content


