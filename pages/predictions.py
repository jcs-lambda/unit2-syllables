# Imports from 3rd party libraries
import dash
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Enter some text and press enter to have the model predict how many syllables each word contains.

            This ignores any character that is not "a" - "z".

            """
        ),
        dcc.Textarea(
        # dcc.Input(
            id = 'prediction_input',
            placeholder = 'Enter some text...',
            # type = 'textarea',
            value = '',
            # debounce = True,
            autoFocus = 'autoFocus',
            persistence = True,
            persistence_type = 'session',
            cols = 25,
            rows = 7
        )
    ],
    md=4,
)

column2 = dbc.Col(
    [
        # html.H2('Predicted syllables', className='mb-5'),
        # html.Div(id='prediction-content', className='lead')
        html.Div(dash_table.DataTable(id='prediction-content'))
    ]
)

layout = dbc.Row([column1, column2])

from joblib import load
import pandas as pd

pipeline = load('assets/pipeline.joblib')

@app.callback(
    [Output('prediction-content', 'data'), Output('prediction-content', 'columns')],
    [Input('prediction_input', 'value')],
)

def predict(text:str):
    if text is None or text == '':
        return [{'word':'', 'syllables':0}], [{'name':'word', 'id':'word'}, {'name':'syllables', 'id':'syllables'}]
    text = pd.Series(text)
    # replace anything that is not an english alphabetic character or white space with nothing
    # replace any white space sequences with the first white space character
    # split on whitespace into individual words
    words = pd.Series(text.str.replace('[^a-zA-Z\s]', '').str.replace('(\s)+', '\\1').str.split('\s')[0])
    words = words[words.str.len() > 0]
    if len(words) == 0 or words.str.len().sum() == 0:
        return [{'word':'', 'syllables':0}], [{'name':'word', 'id':'word'}, {'name':'syllables', 'id':'syllables'}]
    data = {
        'length' : words.str.len(),
        'num_vowels' : words.str.count('[aeiou]'),
        'vowel_chunks' : words.str.count('[aeiou]+'),
        'max_vowel_chunk_length' : words.str.split('[^aeiou]+').apply(lambda a_list : max([len(item) for item in a_list])),
        'ends_with_e' : words.str.endswith('e'),
        'h_as_vowel' : words.str.contains('[aeiou]h[^aeiouy]'),
        'num_ys' : words.str.count('y'), 
        'ends_with_y' : words.str.endswith('y'),
        'y_as_consonant' : words.str.contains('[aeiou]y[aeiou]'),
        'num_consonants' : words.str.count('[^aeiou]'), 
        'consonant_chunks' : words.str.count('[^aeiou]+'),
        'max_consonant_chunk_length' : words.str.split('[aeiou]+').apply(lambda a_list : max([len(item) for item in a_list])),
        'num_doubled_consonants' : words.str.count('([^aeiou])\\1{1}[^$]')
    }
    df = pd.DataFrame(data)
    y_pred = pipeline.predict(df)
    df_predictions = pd.DataFrame({
        'word' : words,
        'syllables' : y_pred
    })
    columns = [{'name':i, 'id':i} for i in df_predictions.columns]
    data = df_predictions.to_dict('records')
    return data, columns
