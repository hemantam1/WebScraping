import openai
API_KEY = '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'
openai.api_key = API_KEY

model = 'text-davinci-003'
prompt = '''cyber security in India
--- 
Cyber security in Singapore
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
