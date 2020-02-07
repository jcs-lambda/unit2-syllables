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

            I started with [dictionary.com's](https://dictionary.com) offline mobile app database. 
            I used all entries that were at least three characters in length and
            contained no spaces or punctuation. One other field that I used consisted of words divided into syllables.
            I removed words with more than 10 syllables from my dataset because there were only 6 of them. 
            I had to manually fix a few incorrect entries that I came across while exploring 
            the data. My final dataset contains about 89,000 words.

            I created the target feature 'syllables' by splitting on the separator character and using the length of the
            resulting list.
            I also created a potential target called 'syllables_group', but I decided not to use it because
            specific predictions would be more interesting and potentially useful. I didn't learn until close to the end of this
            project that I could have used scikit-learns [multi-output classification](https://scikit-learn.org/stable/modules/multiclass.html#multioutput-classification)
            to make predictions for both tagets at once.
            I also created the feature 'length' for the number of characters in the word.

            To avoid leakage in the predictive model (and make feature engineering simpler), I decided to only use
            numeric features that I derived from the words themselves.
            I created a number of features dealing with vowel and consonant counts, vowel and consonant sequences,
            doubled consonants ('tt', 'gg', 'ss', etc.), and features specific to certain letters ('e', 'y', and 'h').
            The image below shows a sample of the dataset, which is available as a CSV in
            [this project's github repo](https://github.com/jcs-lambda/unit2-syllables/blob/master/assets/words.csv).

            [![small sample of the dataset](assets/words_sample_cropped.png)](assets/words_sample.png 'Click for full image')

            I chose to use accuracy score to judge my model's efficacy. I used a shallow [decision tree](https://scikit-learn.org/stable/modules/tree.html 'sklearn Trees documentation')
             for a baseline to compare against my model's performance. Baseline accuracy was about 75%, with a 
            [ROC/AUC](https://www.dataschool.io/roc-curves-and-auc-explained/ 'ROC/AUC measures how well a classifier ranks predicted probabilities')
            score of almost 82%.

            As shown on the [front page](https://syllables.herokuapp.com/ 'Intro page'), linear models would have difficulty
            predicting syllables based on word length alone. The features I engineered allowed a 
            [logistic regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression 'sklearn Logistic Regression documentation')
            model to beat the baseline in accuracy. It scored about 79% accuracy, though the logistic regression model had a
            significantly worse ROC/AUC score of about 63%.

            For the model on the [predictions page](/predictions 'Predictions'), I used a 
            [random forest](https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees 'sklearn forest documentation') classifier.
            A random forest makes use of multiple randomized shallow decision trees by averaging their predictions to form a
            final 'ensemble' prediction. The random forest model achieved an accuracy of 83.21% and a ROC/AUC score of 96.72% on the test set.

            After all is said and done, this particular model is not very useful for any real world application.
            There are [many resources available](https://duckduckgo.com/?q=programatically+counting+syllables 'web search')
            that probably outperform this model. Most of them are rule based and can handle edge cases much better than a
            machine learning model - or at least one I can currently build.

            You can view my work notebook on [github](https://github.com/jcs-lambda/unit2-syllables/blob/master/notebooks/syllables.ipynb).

            """
        ),

    ],
)

layout = dbc.Row([column1])