import requests


def greet(who_to_greet):
    # Greet the Person
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)

name = input("Your Name: ")

print(greet(name))
