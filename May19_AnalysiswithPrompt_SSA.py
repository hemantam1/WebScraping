import openai
from google_play_scraper import app
import pandas as pd
import numpy as np
import openpyxl
# US Market
import requests


from google_play_scraper import Sort, reviews_all
# API_KEY = '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'
# API_KEY = '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'
API_KEY = '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'
openai.api_key = API_KEY


# , 'BEAUTY', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE', 'FOOD-AND-DRINK', 'LIFESTYLE', 'MAPS_AND_NAVIGATION', 'MEDICAL', 'MUSIC_AND_AUDIO',
# 'AUTO_AND_VEHICLES']  # ['NEWS_AND_MAGAZINES']
category_list = ['EDUCATION', 'SHOPPING']
# 'NEWS_AND_MAGAZINES', 'PARENTING', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING', 'SOCIAL', 'SPORTS', 'LIBRARIES_AND_DEMO', 'BOOKs_AND_REFERENCE', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'WEATHER', 'TRAVEL_AND_LOCAL', 'VIDEO_PLAYERS', 'TOOLS']
# print(len(category_list))


# Get each category in excel file and each app
for category in category_list:
    df = pd.read_excel('Playstore.xlsx', sheet_name=category)
    appids = df['appId'].tolist()
    appids = appids[0:1]
    # print(appids)
    # print(len(appids))  #Number of apps
    # No_of_apps = len(appids)
    for eachappid in appids:
        print(eachappid)
        urlid = eachappid.partition('&gl=')[0]  # print(urlid)
        print(urlid)
        us_reviews = reviews_all(
            urlid,
            sleep_milliseconds=0,  # defaults to 0
            lang='en',  # defaults to 'en'
            country='kw',  # defaults to 'us'
            sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
        )

# Concatenated list (list of list)
        df_autoveh = pd.DataFrame(np.array(us_reviews), columns=['review'])
        df_autoveh = df_autoveh.join(pd.DataFrame(
            df_autoveh.pop('review').tolist()))  # to dataframe
       # print(type(us_reviews))
       # print(df_autoveh.head())

        rev_list1 = df_autoveh['content'].tolist()
        if len(rev_list1) < 88:
            rev_list = rev_list1[0:len(rev_list1)]
        else:
            rev_list = rev_list1[0:88]
        # print(len(rev_list))
        print(rev_list)


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
        Your task is to Translate each review into english\
        generate a short summary of each review,\
        sentiment analysis with bad or good of each review, \
        extract relevant information from education app review\
        to give feedback about teaching quality aspect and\
        extract relevant information from shopping app review\
        to give feedback about shipping aspect\
        
        which is separated by ',' in the list\
    
        First Translate the text into english, summarize it,\
        do the sentiment analysis of the each review and\
        feedback about education and shopping app feedaback\
        from the review given below\
        delimited by triple backticks\
        in Table with column headers and title. 

        Review: ```{rev_list}```
        """
        # print(len(prompt))  # 11018
        response = get_completion(prompt)
        print(response)
        print(len(prompt)+len(response))


'''
import openai
from google_play_scraper import app
import pandas as pd
import numpy as np
import openpyxl
# US Market
import requests


from google_play_scraper import Sort, reviews_all
# API_KEY = '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'
# API_KEY = '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'
API_KEY = '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'
openai.api_key = API_KEY


# , 'BEAUTY', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE', 'FOOD-AND-DRINK', 'LIFESTYLE', 'MAPS_AND_NAVIGATION', 'MEDICAL', 'MUSIC_AND_AUDIO',
category_list = ['AUTO_AND_VEHICLES']  # ['NEWS_AND_MAGAZINES']
# 'NEWS_AND_MAGAZINES', 'PARENTING', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING', 'SOCIAL', 'SPORTS', 'LIBRARIES_AND_DEMO', 'BOOKs_AND_REFERENCE', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'WEATHER', 'TRAVEL_AND_LOCAL', 'VIDEO_PLAYERS', 'TOOLS']
# print(len(category_list))


# Get each category in excel file and each app
for category in category_list:
    df = pd.read_excel('Playstore.xlsx', sheet_name=category)
    appids = df['appId'].tolist()
    appids = appids[0:1]
    # print(appids)
    # print(len(appids))  #Number of apps
    # No_of_apps = len(appids)
    for eachappid in appids:
        print(eachappid)
        urlid = eachappid.partition('&gl=')[0]  # print(urlid)
        print(urlid)
        us_reviews = reviews_all(
            urlid,
            sleep_milliseconds=0,  # defaults to 0
            lang='en',  # defaults to 'en'
            country='kw',  # defaults to 'us'
            sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
        )

# Concatenated list (list of list)
        df_autoveh = pd.DataFrame(np.array(us_reviews), columns=['review'])
        df_autoveh = df_autoveh.join(pd.DataFrame(
            df_autoveh.pop('review').tolist()))  # to dataframe
       # print(type(us_reviews))
       # print(df_autoveh.head())

        rev_list1 = df_autoveh['content'].tolist()
        if len(rev_list1) < 88:
            rev_list = rev_list1[0:len(rev_list1)]
        else:
            rev_list = rev_list1[0:88]
        # print(len(rev_list))
        print(rev_list)


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
        Your task is to Translate each review into english\
        generate a short summary of each review and\
        sentiment analysis with bad or good of each review\
        which is separated by ',' in the list\
    
        First Translate the text into english, summarize it and\
        finally do the sentiment analysis of the review below\
        delimited by triple backticks\
        in Table with column headers and title. 

        Review: ```{rev_list}```
        """
        # print(len(prompt))  # 11018
        response = get_completion(prompt)
        print(response)
        print(len(prompt)+len(response))
        # Extract the conversation from the API response
'''

'''#Code to analyse the prompt with different tasks summary, sentiment and aspect analysis

import openai
from google_play_scraper import app
import pandas as pd
import numpy as np
import openpyxl
# US Market

from google_play_scraper import Sort, reviews_all
# API_KEY = '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'
API_KEY = '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'
openai.api_key = API_KEY


# , 'BEAUTY', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE', 'FOOD-AND-DRINK', 'LIFESTYLE', 'MAPS_AND_NAVIGATION', 'MEDICAL', 'MUSIC_AND_AUDIO',
category_list = ['ART_AND_DESIGN', 'AUTO_AND_VEHICLES']
# 'NEWS_AND_MAGAZINES', 'PARENTING', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING', 'SOCIAL', 'SPORTS', 'LIBRARIES_AND_DEMO', 'BOOKs_AND_REFERENCE', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'WEATHER', 'TRAVEL_AND_LOCAL', 'VIDEO_PLAYERS', 'TOOLS']
# print(len(category_list))


# Get each category in excel file and each app
for category in category_list:
    df = pd.read_excel('Playstore.xlsx', sheet_name=category)
    appids = df['appId'].tolist()
    appids = appids[0:2]
    # print(appids)
    # print(len(appids))  #Number of apps
    # No_of_apps = len(appids)
    for eachappid in appids:
        print(eachappid)
        urlid = eachappid.partition('&gl=')[0]  # print(urlid)
        print(urlid)
        us_reviews = reviews_all(
            urlid,
            sleep_milliseconds=0,  # defaults to 0
            lang='en',  # defaults to 'en'
            country='kw',  # defaults to 'us'
            sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
        )

# Concatenated list (list of list)
        df_autoveh = pd.DataFrame(np.array(us_reviews), columns=['review'])
        df_autoveh = df_autoveh.join(pd.DataFrame(
            df_autoveh.pop('review').tolist()))  # to dataframe
       # print(type(us_reviews))
       # print(df_autoveh.head())

        rev_list1 = df_autoveh['content'].tolist()
        if len(rev_list1) < 88:
            rev_list = rev_list1[0:len(rev_list1)]
        else:
            rev_list = rev_list1[0:88]
        # print(len(rev_list))
        print(rev_list)


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
        print(response) '''
