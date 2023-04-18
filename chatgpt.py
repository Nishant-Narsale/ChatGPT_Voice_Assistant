import openai

commands = [
    "Write an introduction to neem oil, writing what it is.",
    "thing to do in Miami.",
    "best 10 beers in the world."
]

openai.api_key = ''

model_engine = "text-curie-001"


def get_ans_from_response(response:openai.openai_object.OpenAIObject) -> str:
    first = dict(response)['choices']
    sec = dict(first[0])
    return sec['text']

def command(model_engine:str = model_engine,prompt:str = "") -> str:
    # Send the request to the Chat GPT API
    response = openai.Completion.create(
                          engine=model_engine,
                          prompt=prompt,
                          max_tokens=1024
                          )
    return get_ans_from_response(response)


if __name__=="__main__":
    for c in commands:
        res = command(prompt=c)
        print(res)
        break