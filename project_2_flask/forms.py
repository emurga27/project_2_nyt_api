from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, RadioField
import requests
import json
from project_2_flask import main_functions
import pprint

class CriticsReviewForm(FlaskForm): #to create a form, we create a class
    reviews = SelectField('Review',
                         choices=[('all', 'All'), #the 1st column is what I see, the second input is what users sees
                                  ('picks', 'Picks')])
    choice = SelectField('Choice',
                         choices=[('display_title', 'Title'), #the 1st column is what I see, the second input is what users sees
                                  ('headline', 'Headline'),
                                  ('summary_short', 'Summary')])

#movie reviews that are critics' picks
def get_critics_reviews(type, choice):
    api_key_dict = main_functions.read_from_file('project_2_flask/JSON_documents/api_key.json')
    api_key = api_key_dict['my_nyt_key']
    url = f'https://api.nytimes.com/svc/movies/v2/reviews/{type}.json?api-key=' + api_key
    response = requests.get(url).json()
    main_functions.save_to_file(response, 'project_2_flask/JSON_documents/response.json')
    my_movie_reviews = main_functions.read_from_file('project_2_flask/JSON_documents/response.json')

    '''from the response dictionary, you need to filter the data requested by the user'''
    #create alist with the info I want from the json file
    my_response = []

    for i in my_movie_reviews['results']:
        my_response.append(i[choice])
    #print(my_response[0])

    return my_response

#print(get_critics_reviews("all")) #to test the functions