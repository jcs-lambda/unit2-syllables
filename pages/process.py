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

            [![small sample of the dataset](assets/words_sample_cropped.png)](assets/words_sample.png 'Click for full image')

            I chose to use accuracy score to judge my model's efficacy. As I constructed it to be a multi-class
            classification problem, I used a shallow decision tree for a baseline to compare against my model's
            performance. Baseline accuracy was about 75%, with a ROC/AUC score of almost 82%.

            As shown on the [front page](https://syllables.herokuapp.com/ 'Intro page'), linear models would have difficulty
            predicting syllables based on word length alone. The features I engineered allowed a logistic regression model
            to beat the baseline in accuracy, scoring about 79% accuracy. But, the logistic regression model had a
            significantly worse ROC/AUC score of about 63%.

            For the model in use on the [predictions page](/predictions 'Predictions'), I used a random forest classifier.
            A random forest makes use of several shallow decision trees whose outputs are averaged together to build a
            final model. The random forest model achieved an accuracy of 83.21% and a ROC/AUC score of 96.72% on the test set,
            which I had held out at the begining and only used for this final set o predictions.


            """
        ),

    ],
)

layout = dbc.Row([column1])