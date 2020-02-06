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