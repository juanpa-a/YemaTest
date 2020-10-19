# Yema Test

## Installation

Navigate to `yematestfront/` inside directory and clone the front-end [repo](https://github.com/juanpa-a/YemaTest).

**To clone with HTTP:**
```
cd yematestfront && git clone https://github.com/juanpa-a/YemaTest
```
**To clone SSH:**
```
cd yematestfront && git clone git@github.com:juanpa-a/YemaFront.git
```
### Dependencies
#### Frontend 
**To install dependencies run the following:**
```
npm i
```

### Backend 
Go back to the root of the project `YemaTest/` and if you don't already have virtualenv installed install it.

**Opcional:**
```
pip3 install virtualenv
```
If you get permission problems installing virtualenv run it with super user privileges.
```
sudo pip3 install virtualenv
```


Once you have virtual env installed create an enviorment for the project and activate it.
```
virtualenv env
source env/bin/activate
```

To install navigate to the `yematest/` directory and run the following command
```
pip install -r requirements.txt
```

Once all the dependencies are installed you need to apply the database migrations.
```
python manage.py migrate
```
or depending on your python version
```
python3 manage.py migrate
```

When the database is ready you will be able to start the server.
```
python manage.py runserver
```

When the server is up you can either interact with it using curl, postman, insomnia or your [browser](http://localhost:8000/)

To be able to send email from the admin dashboard you will need to configure some variables in the code.

Open the `yematest/settings.py` file and scroll to the bottom
```
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
```
and the `main/admin.py` file and enter your email
in the `YOUR_EMAIL` variable.


You will need to provide your gmail account and password to send emails, if you don't want to use a gmail account it's ok but you will need to change other settings aswell.

Also you will to allow your gmail account to connect to the demo app, to allow it click [here](http://myaccount.google.com/lesssecureapps)

Now you will be albe to go back to the `yematestfront/` repository and start the front end with the following command

```
npm start
```
This will start the server in `http://localhost:9000`.

I recommend you first create some patients and doctors directly in the admin dashboard since i didn't implement any persistence in the front end.


## Testing

In order to test the api you only need to run:
```
python manage.py test
```
