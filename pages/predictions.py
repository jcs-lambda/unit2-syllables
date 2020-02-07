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

            Enter text to have the model predict how many syllables each word contains.

            This ignores any character that is not in the English alphabet.

            If the actual number of syllables is unknown, it will be blacked out.

            """
        ),
        dcc.Textarea(
            id = 'prediction_input',
            placeholder = 'Enter some text...',
            value = '',
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
        html.Div(dash_table.DataTable(
            id='prediction-content',
            style_data_conditional = [
                {
                    'if' : {
                        'column_id' : 'predicted syllables',
                        'filter_query' : '{predicted syllables} ne {actual syllables} && {actual syllables} ne 0'
                    },
                    'backgroundColor' : '#ffcccc'
                },
                {
                    'if' :{
                        'column_id' : 'actual syllables',
                        'filter_query' : '{actual syllables} eq 0 && {predicted syllables} ne 0'
                    },
                    'backgroundColor' : '#000000'
                }
            ]
        ))
    ]
)

layout = dbc.Row([column1, column2])

from joblib import load
import pandas as pd

pipeline = load('assets/pipeline.joblib')
df_words_min = pd.read_csv('assets/words_min.csv')
df_words_min['entry'] = df_words_min['entry'].str.lower()
df_words_min.drop_duplicates(subset='entry', keep='first', inplace=False)

def get_actual(word):
    if len(word) == 0:
        return 0
    elif len(word) < 3:
        return 1
    else:
        syllables = df_words_min[df_words_min['entry'] == word]['syllables'].values
        if len(syllables) == 0:
            return 0
        else:
            return syllables[0]

@app.callback(
    [Output('prediction-content', 'data'), Output('prediction-content', 'columns')],
    [Input('prediction_input', 'value')],
)

def predict(text:str):
    if text is None or text == '':
        return [{'word':'', 'predicted syllables':0, 'actual syllables':0}], [{'name':'word', 'id':'word'}, {'name':'predicted syllables', 'id':'predicted syllables'}, {'name':'actual syllables', 'id':'actual syllables'}]
    text = pd.Series(text)
    # replace anything that is not an english alphabetic character or white space with nothing
    # replace any white space sequences with the first white space character
    # split on whitespace into individual words
    words = pd.Series(text.str.replace('[^a-zA-Z\s]', '').str.replace('(\s)+', '\\1').str.split('\s')[0])
    words = words[words.str.len() > 0]
    if len(words) == 0 or words.str.len().sum() == 0:
        return [{'word':'', 'predicted syllables':0, 'actual syllables':0}], [{'name':'word', 'id':'word'}, {'name':'predicted syllables', 'id':'predicted syllables'}, {'name':'actual syllables', 'id':'actual syllables'}]
    data = {
        'length' : words.str.len(),
        'num_vowels' : words.str.lower().str.count('[aeiou]'),
        'vowel_chunks' : words.str.lower().str.count('[aeiou]+'),
        'max_vowel_chunk_length' : words.str.lower().str.split('[^aeiou]+').apply(lambda a_list : max([len(item) for item in a_list])),
        'ends_with_e' : words.str.lower().str.endswith('[e]'),
        'h_as_vowel' : words.str.lower().str.contains('[aeiou]h[^aeiouy]'),
        'num_ys' : words.str.lower().str.count('y'), 
        'ends_with_y' : words.str.lower().str.endswith('y'),
        'y_as_consonant' : words.str.lower().str.contains('[aeiou]y[aeiou]'),
        'num_consonants' : words.str.lower().str.count('[^aeiou]'), 
        'consonant_chunks' : words.str.lower().str.count('[^aeiou]+'),
        'max_consonant_chunk_length' : words.str.lower().str.split('[aeiou]+').apply(lambda a_list : max([len(item) for item in a_list])),
        'num_doubled_consonants' : words.str.lower().str.count('([^aeiou])\\1{1}[^$]')
    }
    df = pd.DataFrame(data)
    y_pred = pipeline.predict(df)
    df_predictions = pd.DataFrame({
        'word' : words,
        'predicted syllables' : y_pred,
        'actual syllables' : [get_actual(word) for word in words.str.lower()]
    })
    columns = [{'name':i, 'id':i} for i in df_predictions.columns]
    data = df_predictions.to_dict('records')
    return data, columns
