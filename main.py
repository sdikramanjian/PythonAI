from bottle import route, run, template, TEMPLATE_PATH
#import requests

TEMPLATE_PATH.append('./ui_templates/') # Set the path to the directory containing my html templates

investor_types = ['Conservative', 'Moderate', 'Aggressive'] # Create an array called investor_types
result = '' # Create a variable called result

@route('/')
def index():
    return template('top_level_component.tpl', title='Welcome', name='Susan', investor_types=investor_types, result=result) 

@route('/',method='POST')
def submit_form():
   # investor_type=request.forms.get('investor_type')
    return template('top_level_component.tpl', title='Welcome', name='Susan', investor_types=investor_types, result=f"Here are some stocks we want to recomment to you:")

if __name__ =='__main__':
    run(host='localhost',port=8080,debug=True)
