from flask import Flask

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, World!'
def func():
    global value
    value = "Local"


value = "Global"
func()
print(value)

# def alphabetic_order(arr):
#     result = []
#     for word in arr:
#         for i in range(1, len(word)):
#             if ord(word[i]) < ord(word[0]):
#                 result.append("Yes")
#                 break
#         else:
#             result.append("No")
#     return result
#
#
# names = ["Germain", "safari", "age"]
# result = alphabetic_order(names)
# print(result)
