import openai
API_KEY = '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'
openai.api_key = API_KEY

model = 'text-davinci-003'
prompt = '''Generate the report for cyber security policy in Canada for 10 pages
'''
response = openai.Completion.create(
    
    prompt = prompt,
    model = model,
    max_tokens = 1000,
    temperature=0.9,
    n=3,
    stop=['---']

)
for result in response.choices:
  print(result.text)