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
        
            ## Insights

            #### Fun Stuff

            The thing I enjoy most about this completed project is playing around on the [predictions](/predictions) page.
            It is fun to find words that are classified incorrectly and play around with groups or variations of them to
            try to identify where the model is failing, and maybe figure out why. It is pretty cool to see the model's output
            in real time.

            #### Predictive Modeling

            As I iterated through this project, I kept adding more features in an attempt to provide the model enough data
            to catch some of the edge cases that I came across. I started with length, the number of vowels and consonants, 
            features dealing with the letter 'y', and whether or not a word started or ended with a vowel. The model's most
            significant jump in accuracy came when I added features dealing with sequences of vowels and consonants.
            As you can see in the image below, my final model made most use of the 'chunk' features; and most of my later
            feature engineering provided negligible impact on the model's decision process.

            ![Final model's feature importances](assets/feature_importances.png)

            This graph of the top of the shallow decision tree I used to establish a baseline score shows where it decided
            to split, using the 'chunk' features in it's first few levels. You can click the image to view the next row as well.

            [![Decision Tree Stump](assets/decision_tree_stump.png)](assets/decision_tree_stump_large.png 'Click for a larger view')

            For each model, I output a [confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) and 
            [classification report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html?highlight=classification%20report#sklearn.metrics.classification_report).
            While working through models and features, keeping an eye on the macro averages of precision and recall let me
            realize when I was going off track on feature engineering and parameter tuning.
            A few things stood out to me on the final models:
            - baseline model never predicted above 5 syllables
            - logistic regression never predicted above 7 syllables

            ##### Baseline Classification Report and Confusion Matrix
            ![Baseline Classification Report](assets/baseline_classification_report.png)
            ![Baseline Confusion Matrix](assets/baseline_confusion_matrix.png)

            ##### Logistic Regression Classification Report and Confusion Matrix
            ![Logistic Regression Classification Report](assets/logreg_classification_report.png)
            ![Logistic Regression Confusion Matrix](assets/logreg_confusion_matrix.png)

            ##### Random Forest Classification Report and Confusion Matrix
            ![Random Forest Classification Report](assets/rndforest_classification_report.png)|
            ![Random Forest Confusion Matrix](assets/rndforest_confusion_matrix.png)

            I think I could have made use of scikit-learn's [multi-output classification](https://scikit-learn.org/stable/modules/multiclass.html#multioutput-classification)
            to make predictions for both syllables and syllable_groups simultaneously.

            #### Things that interested my inner word-nerd

            I had difficulty quickly thinking of short words that had multiple syllables, but there are several common
            2 syllable words that are only 3 letters long, such as:
            - ago
            - emu
            - era

            The longest single syllable words in this dataset are 8 letters long. Most of those began with a
            sequence of consonants, usually starting with 's', like these:
            - schmooze
            - scrounge
            - straight
            - strength

            There were several 2 syllable words that were 12 letters long, like these:
            - crackbrained
            - breakthrough
            - bloodstained
            - hairsbreadth

            Most interesting word I learned:
            - syzygy \[ siz-i-jee \]
                - an alignment of three celestial objects
                - any two related things, either alike or opposite

            """
        ),

    ],
)

layout = dbc.Row([column1])