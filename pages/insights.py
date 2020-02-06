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