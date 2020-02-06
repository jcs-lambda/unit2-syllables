# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            I started with [dictinary.com's](https://dictionary.com) offline mobile app database. It contains a lot information
            that I ended up not using for this project. I used all the entries at least three charachters in length that
            did not contain any spaces or puncuation. One other field that I used contained the words divided into syllables.
            I removed words with more than 10 syllables from my dataset, because words that large were only 6 of them. 
            I had to manually fix a few incorrect entries that I came across while exploring 
            the data. Eventually, the dataset contained about 89,000 words.

            I created the target feature 'syllables' by splitting on the separator character and using the length of the
            resulting list.
            I also created a potential target called 'syllables_group', but I decided not to use it because
            specific predictions would be more interesting and potentially useful.
            I also created the feature 'length' for the number of characters in the word.

            To avoid leakage in the predictive model (and make feature engineering simpler), I decided to only use
            numeric features that I derived from the words themselves.
            I created number of features dealing with vowel and consonant counts, vowel and consonant sequences,
            doubled consonants ('tt', 'gg', 'ss', etc.), and features specific to certain letters ('e', 'y', and 'h').
            The final dataset I used for this model looked like the image below and is available as a CSV in
            [this project's github repo](https://github.com/jcs-lambda/unit2-syllables/assets/words.csv).

            ![small sample of the dataset](assets/words_sample.png 'small sample of the dataset')

            

            """
        ),

    ],
)

layout = dbc.Row([column1])