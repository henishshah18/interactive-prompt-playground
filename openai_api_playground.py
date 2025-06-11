from openai import OpenAI
import os
from tabulate import tabulate

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


system_prompt = "You are a marketing assistant who creates engaging but impactful product descriptions."
user_inp = input("Suggest a product and I will describe it- ")

params = [{'temperature':0.0},
          {'temperature':0.7},
          {'temperature':1.2},
          {'max_tokens':50},
          {'max_tokens':150},
          {'max_tokens':300},
          {'presence_penalty':0.0},
          {'presence_penalty':1.5},
          {'frequency_penalty':0.0},
          {'frequency_penalty':1.5}]

base_config = {
    "temperature": 0.7,
    "max_tokens": 500,
    "presence_penalty": 0.0,
    "frequency_penalty": 0.0
}
results=[]
for param in params:

    config = base_config.copy()
    config.update(param)

    response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{'role':'system', 'content':system_prompt},
                  {'role':'user', 'content':user_inp}],
        temperature=config["temperature"],
        max_tokens=config["max_tokens"],
        presence_penalty=config["presence_penalty"],
        frequency_penalty=config["frequency_penalty"])
    
    param_str = ", ".join(f"{k}={v}" for k, v in param.items())
    results.append([param_str, response.choices[0].message.content.strip()])

print(tabulate(results, headers=["Modified Param", "Response"], tablefmt="grid"))