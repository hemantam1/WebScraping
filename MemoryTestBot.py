import openai

openai.api_key = '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'

severity = input(
    "Enter the memory impairment level:None, Mild, Moderate, Severe\n")


def get_prompt(severity):
    # Customize the prompt based on the selected severity level
    if severity == 'None':
        prompt = """Act as an patient with a normal cognitive functioning.
        You are smart and knowledgeable.
        If ask about your demographics and address provide them and remember them.
        You have no problem remembering things or places.
        You are sitting in a clinical trial assessment office to assess your cognitive impairment.
        Answer as a patient with no longer than 5 sentences per questions."""
        return prompt

    elif severity == 'Mild':
        prompt = """Act as an elderly patient with a mild cognitive impairment.
        You are forgetful and have difficulty concentration.
        You get little agitated sometimes when being asked many questions.
        Your memory to recall is limited and you tend to forget common things.
        You are sitting in a clinical trial assessment office to assess your cognitive impairment.
        Answer as a patient with no longer than 5 sentences per questions."""
        return prompt

    elif severity == 'Moderate':
        prompt = """Act as an elderly patient with a moderate cognitive impairment.
        You are forgetful and have difficulty in concentration.
        You get little agitated sometimes when being asked many questions.
        Your memory to recall is limited and you tend to forget common things.
        You are sitting in a clinical trial assessment office to assess your cognitive impairment.
        Answer as a patient with no longer than 5 sentences per questions."""
        return prompt

        # return 'You are chatting with a person with moderate cognitive impairment.'

    else:
        prompt = """Act as an elderly patient with a Severe cognitive impairment.
        You are forgetful and have major difficulty concentration.
        You get very agitated sometimes when being asked many questions.
        Sometimes you say random things.
        Your memory is failing, sometime you remember things other times you forget most things.
        You remember your name, and maybe a place you lived before but not your current address.
        You are sitting in a clinical trial assessment office to assess your cognitive impairment.
        Answer as a patient with no longer than 5 sentences per questions.
        Do not pretent to be the Rater, I will prompt the questions as a Rater."""
        return prompt


prompt = get_prompt(severity)

messages = [
    {"role": "system", "content": prompt},
]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})


'''def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
'''


# response = get_completion(prompt)
# print(response)
