import requests

# testing modes
QUESTION_ADD_TEST = 1
QUESTION_GET_TEST = 2
DEFINITION_ADD_TEST = 3
DEFINITION_GET_TEST = 4
QUESTION_CORRECT_ADD_TEST = 5

# current mode (change this)
mode = DEFINITION_GET_TEST

# sample data
sample_question_data = {
    "explanation": "nothing here",
    "category": "test cat",
    "level": 2,
    "question": "helloworld",
    "option1": "blah", "option2": "another test", "option3": "this is correct", "option4": "wrong",
    "answer": 3,
}

sample_definition_data = {
    "item": "test",
    "definition": "testing",
    "aliases": """["testing", "tests"]""",
}

# add qn api test
if mode == QUESTION_ADD_TEST:
    r = requests.post("http://localhost:5000/api/v1/questions",
                      sample_question_data)
    print(r.text)

# get qn api test
elif mode == QUESTION_GET_TEST:
    r = requests.get("http://localhost:5000/api/v1/questions?mode=all&num=10")
    print(r.text)

# add definition api test
elif mode == DEFINITION_ADD_TEST:
    r = requests.post(
        "http://localhost:5000/api/v1/definitions", sample_definition_data)
    print(r.text)

elif mode == DEFINITION_GET_TEST:
    r = requests.get("http://localhost:5000/api/v1/definitions?input=tests")
    print(r.text)