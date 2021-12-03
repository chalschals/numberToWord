# commands

## TO Create Virtual Environment

pip install virtualenv

python3 -m venv env

.\env\Scripts\activate

## FOR PROJECT SETUP

cd <project_root>

pip install -r requirements.txt

## TO START DJANGO APPLICAION

python manage.py runserver

## FOR DJANGO TESTING

coverage run manage.py test

## ENDPOINTS

GET http://localhost:8000/num_to_english?number=123

POST http://localhost:8000/num_to_english
{
"number":125
}
