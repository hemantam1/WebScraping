import openai
from google_play_scraper import app
import pandas as pd
import numpy as np
# US Market

from google_play_scraper import Sort, reviews_all


us_reviews = reviews_all(
    # 'com.omega.taxi',  47
    # 'com.eterno',
    # 'com.mstech.photoeditor',11
    # 'com.logomaster.createlogo.makelogo.designer.canvafree', 241
    # 'com.canva.editor',
    'com.studio.aone.girlshairstyle.hairstylestepbystep',
    sleep_milliseconds=0,  # defaults to 0
    lang='en',  # defaults to 'en'
    country='kw',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
)

# Concatenated list (list of list)
df_autoveh = pd.DataFrame(np.array(us_reviews), columns=['review'])
df_autoveh = df_autoveh.join(pd.DataFrame(
    df_autoveh.pop('review').tolist()))  # to dataframe
print(type(us_reviews))
print(df_autoveh.head())

rev_list1 = df_autoveh['content'].tolist()
rev_list = rev_list1[0:84]
print(len(rev_list))
print(rev_list)


API_KEY = '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'
openai.api_key = API_KEY


# Andrew mentioned that the prompt/ completion paradigm is preferable for this class
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


prompt = f"""
Your task is to Tranlate and generate a short summary of each review\
which is separated by ',' in the list\

First Translate the text into english and summarize the review below\
delimited by triple backticks, in atmost 3 words. 

Review: ```{rev_list}```
"""
# print(len(prompt))  # 11018
response = get_completion(prompt)
print(response)


# List of category
category_list = ['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE', 'FOOD-AND-DRINK', 'LIFESTYLE', 'MAPS_AND_NAVIGATION', 'MEDICAL', 'MUSIC_AND_AUDIO',
                'NEWS_AND_MAGAZINES', 'PARENTING', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING', 'SOCIAL', 'SPORTS', 'LIBRARIES_AND_DEMO', 'BOOKs_AND_REFERENCE', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'WEATHER', 'TRAVEL_AND_LOCAL', 'VIDEO_PLAYERS', 'TOOLS']
# print(len(category_list))


# Get each category in excel file and each app
# for category in range(len(category_list)):
for category in category_list:
    df = pd.read_excel("Playstore.xlsx", sheet_name=category)

# From colab


'''us_reviews = reviews_all(
    # 'com.omega.taxi',
    # 'com.facebook.katana',
    'com.eterno',
    sleep_milliseconds=0,  # defaults to 0
    lang='en',  # defaults to 'en'
    country='kw',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
)



# Concatenated list (list of list)
df_autoveh = pd.DataFrame(np.array(us_reviews), columns=['review'])
df_autoveh = df_autoveh.join(pd.DataFrame(
    df_autoveh.pop('review').tolist()))  # to dataframe

# Dropping last n rows using drop
n = 50000
df_autoveh.drop(df_autoveh.tail(n).index, inplace=True)

# print(len(us_reviews))
# print(type(us_reviews))
# print(df_autoveh.head())
rev_list1 = df_autoveh['content'].tolist()
print(len(rev_list1))
rev_list = rev_list1[0:100]
print(rev_list)
'''
