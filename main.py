from bottle import route, request,run, template, TEMPLATE_PATH
from advisor import Advisor;
#import requests

TEMPLATE_PATH.append('./ui_templates/') # Set the path to the directory containing my html templates

investor_types = ['Conservative', 'Moderate', 'Aggressive'] # Create an array called investor_types
result = '' # initiate a variable called result
my_name = 'Susan' # initiate a variable called myName
stock_advisor = Advisor() # Create an instance of the Advisor class

@route('/')
def index():
    return template('top_level_component.tpl', title='Welcome', name=my_name, investor_types=investor_types, result=result) 

@route('/',method='POST')
def submit_form():
    investor_type=request.forms.get('investor_type')
    data = stock_advisor.recommend_stocks(investor_type)
    return template('top_level_component.tpl', title='Welcome', name=my_name, investor_types=investor_types, result=f"Here are some stocks we want to recomment to you {my_name} since you are a {investor_type} investor:")

if __name__ =='__main__':
    run(host='localhost',port=8080,debug=True)
