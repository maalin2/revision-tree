# get model setup multimodal
# from openai import OpenAI
# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)
# linux 
import requests   
API_URL = "https://api-inference.huggingface.co/models/AnReu/math_albert"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "What is two plus two?",
})
print(output)

#function to return answer string   
def gen_answer(slide):
    answer = "hi"
    return answer


print(gen_answer("whats up"))
# function to return hint string
def gen_hint(slide):
    hint = "hi"
    return hint