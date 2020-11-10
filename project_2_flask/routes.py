from project_2_flask import app, forms
from flask import request, render_template #render_templete will launch html
#this request is used to request data from the user
#the "requests" is used to get data from api's
@app.route('/', methods=['GET', 'POST'])
def search():
    my_form = forms.CriticsReviewForm(request.form) #this 'forms' is the file with the class form

    # if the user select the Search button
    if request.method == 'POST':
        #first_name = request.form['first_name']
        options = request.form['reviews'] #this variable is assigned to the option selected by the user
        choice = request.form['choice']
        # call de api
        my_response = forms.get_critics_reviews(options, choice)
        #print(my_response)
        return render_template('results.html',result = options, response=my_response)

    return render_template('search.html', form=my_form)