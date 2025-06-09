# Import the FastAPI class from the fastapi module
from fastapi import FastAPI

# Declare an instance of the FastAPI class
app = FastAPI()

# use the app instance as a decorator to handle  an
# HTTP route and HTTP method
@app.get("/")
def read_index():
    """
    Return a python dictionary that supports JSON serialization.
    """
    return {"messsage": "Hello, World!"}
@app.get("/hello/{name}")
def read_hello(name: str):
    """
    Return a python dictionary that supports JSON serialization.
    """
    return {"message": f"Hello, {name}!"}
@app.get("/hello/{name}/age/{age}")
def read_hello_age(name: str, age: int):
    """
    Return a python dictionary that supports JSON serialization.
    """
    return {"message": f"Hello, {name}! You are {age} years old."}
@app.get("/hello/{name}/age/{age}/city/{city}")
def read_hello_age_city(name: str, age: int, city: str):
    """
    Return a python dictionary that supports JSON serialization.
    """
    return {"message": f"Hello, {name}! You are {age} years old and live in {city}."}
@app.get("/hello/{name}/age/{age}/city/{city}/country/{country}")
def read_hello_age_city_country(name: str, age: int, city: str, country: str):
    """
    Return a python dictionary that supports JSON serialization.
    """
    return {"message": f"Hello, {name}! You are {age} years old, live in {city}, and are from {country}."}
@app.get("/hello/{name}/age/{age}/city/{city}/country/{country}/zipcode/{zipcode}")
def read_hello_age_city_country_zipcode(name: str, age: int, city: str, country: str, zipcode: str):
    """
    Return a python dictionary that supports JSON serialization.
    """
    return {"message": f"Hello, {name}! You are {age} years old, live in {city}, are from {country}, and your zipcode is {zipcode}."}
@app.get("/hello/{name}/age/{age}/city/{city}/country/{country}/zipcode/{zipcode}/street/{street}")
def read_hello_age_city_country_zipcode_street(name: str, age: int, city: str, country: str, zipcode: str, street: str):
    """
    Return a python dictionary that supports JSON serialization.
    """
    return {"message": f"Hello, {name}! You are {age} years old, live in {city}, are from {country}, your zipcode is {zipcode}, and your street is {street}."}
@app.get("/hello/{name}/age/{age}/city/{city}/country/{country}/zipcode/{zipcode}/street/{street}/house/{house}")
def read_hello_age_city_country_zipcode_street_house(name: str, age: int, city: str, country: str, zipcode: str, street: str, house: str):
    """
    Return a python dictionary that supports JSON serialization.
    """
    return {"message": f"Hello, {name}! You are {age} years old, live in {city}, are from {country}, your zipcode is {zipcode}, your street is {street}, and your house number is {house}."}