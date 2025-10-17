import os
import pymysql
from urllib.request import urlopen
from email_validator import validate_email, EmailNotValidError

db_config = os.environ.get('DB_CONFIG')
# My goal was to save the sensitive information in a environment variable
# and then use that environment variable to connect to the database
# information is stored in .env variable with gitignore so ensure it does not push

def get_user_input():
    users = os.environ.get('USERS')
    user_input = input('Enter your name: ')
    if user_input in users:
        return users[user_input]
    else:
        return None
# My goal here was to save the users in a environment variable
# and return the user input if it is found. If not return as None.

def send_email(to, subject, body):
    try:
        send_to = to
        email = validate_email(email, check_deliverability=True)
        return True, "Valid Email"
    
    except EmailNotValidError as e:
        return False, str(e)
    
# One way I think to validate email, is to use a library like validate_email
# We used this library back in term 2 of ISD course. 

def get_data():
    url = 'https://insecure-api.com/get-data'
    try:
        response = response.get(url)
        
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
# Goal here was to use HTTPS and use a try catch block to get a response from
# the API. If it returns a valid response, return the data.
# If not, catch the exception error and return None.
# users saved in env variable

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)