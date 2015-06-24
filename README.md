#Refuge SMS

## About

Refuge SMS is a simple to deploy heroku app that interfaces with the
http://www.refugerestrooms.org API.

## Usage

Just text an address to the connected number, and you will get a reply text
with the name and address of the nearest restroom in the database.

## How to deploy on Heroku

1. First, clone this repo locally
2. Ensure you have the heroku toolbelt installed: https://devcenter.heroku.com/articles/getting-started-with-python#set-up
3. run the following command:

  $ heroku create

4. Adjust the SECRET_KEY in refuge.py and commit the change
5. run:

  $ git push heroku master

6. run:

  $ heroku ps:scale web=1

7. Copy the URL generated, and enter the URL with the SECRET_KEY appended into Twilio's management console for SMS. 
8. Text the number for your bathroom needs :)
