import openai
openai.api_key = open("apikey.txt", "r").read()
content = "Hello, I am feeling very tired today" 
prompt = f"Can you give me only one emoji that is new, trendy and widely used by other users for the following text: {content}"


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)


#print(completion)
emoji = completion.choices[0].message["content"]

print(content, " -> Suggested emoji:", emoji)

#2 
content = "Are you planning to go to the open gym today?" 
prompt = f"Can you give me only one emoji that is new, trendy and widely used by other users for the following text: {content}"


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)


#print(completion)
emoji = completion.choices[0].message["content"]

print(content, " -> Suggested emoji:", emoji)

#3 
content = "I went to a Sushi place in Palo Alto for dinner. Their nigiri is nice!" 
prompt = f"Can you give me only one emoji that is new, trendy and widely used by other users for the following text: {content}"


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

#print(completion)
emoji = completion.choices[0].message["content"]
print(content, " -> Suggested emoji:", emoji)



#4

content = "Have you looked at the Geometry homework? I have a few questions that I like to discuss" 
prompt = f"Can you give me one and only one emoji that is new, trendy and widely used by other users for the following text: {content}"


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)

#print(completion)
emoji = completion.choices[0].message["content"]
print(content, " -> Suggested emoji:", emoji)