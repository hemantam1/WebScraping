import openai
import PyPDF2  # for PDF file
import google_play_scraper
from google_play_scraper import app
import pandas as pd
import numpy as np

API_KEY = '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'
openai.api_key = API_KEY


# function to convert PDF to text
def PDF2text(filename):

    # Open the PDF file
    with open(filename, mode='rb') as file:

        # Read the PDF file
        reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF file
        num_pages = len(reader.pages)

        # Extract text from each page of the PDF file
        text = ""
        for i in range(num_pages):
            page = reader.pages[i]
            text += page.extract_text()
    return (text)  # print(text)


input_text = PDF2text('Australia_cybersecuritystrategy.pdf')

# Sentiment Analysis
for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a product \ 
    review from an ecommerce site. 

    Summarize the review below, delimited by triple \
    backticks in at most 20 words. 

    Review: ```{reviews[i]}```
    """

    response = get_completion(prompt)
    print(i, response, "\n")


# print(input_text)
'''
#Creation /Generate the content format
model = 'text-davinci-003'
prompt = 'Districts in Tamilnadu'
response = openai.Completion.create(
    prompt=prompt,
    model=model,
    max_tokens=1000,
    temperature=0,   # variation in output 
    n=3
)
for result in response.choices:
    print(result.text)



def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"] '''
