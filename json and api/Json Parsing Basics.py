import json

question = '{"questionno":1,"question":"What is the capital of Japan","option1":"Hukulganj","option2":"Peelikothi","option3":"Jaunpur","option4":"Tokyo","correct":"4"}'

print(question, type(question))
question = json.loads(question)
print(question, type(question))
question = json.dumps(question)
print(question, type(question))
