from flask import Flask
app = Flask(__name__)
print(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

#
# if __name__=="main":
#     app.run()
#
#
# nested function
# import time
#
#
# def delay_decorator(function):
#     def wrap():
#         time.sleep(2)
#         function()
#         function()
#
#     return wrap()


@delay_decorator
def write():
    print("hello world")


