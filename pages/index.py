# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ### Trouble automating your haikus?

            Does your recurrent neural network haiku generator require you to label all your training data with syllable counts?

            Why not leverage the power of machine learning to automate that onerous task?

            **Bonus Feature:** Only 83% accurate predictions, so your AI can push the boundaries of haiku as an art form!

            """
        ),
        dcc.Link(dbc.Button('Try It Out', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

# import pandas as pd
# df = pd.read_csv('assets/words_min.csv')
# fig = px.scatter(df, x='length', y='syllables', trendline='ols', 
#     range_y=[0,10], range_x=[3, 20], opacity=.2, 
#     title='Word Length by Number of Syllables',
#     size_max=80,
# )

column2 = dbc.Col(
    [
        dcc.Markdown(
            """

            ##### Why word length is not a good predictor of number of syllables.

            As you can see in the plot below, it would be difficult to make accuracte predictions only using the length of the word.
            I engineered several features that enabled even a linear model to do a decent job classifying the number of a word's syllables.
            I ended up using a tree based model for use in the [predictions page](/predictions).

            [![Scatter plot of word length by number of syllables](assets/linear_scatter_small.png)](assets/linear_scatter.png 'Click for full size image')

            Check out the [Process page](/process 'Process') to see some details about the dataset and model I used.

            On the [Insights page](/insights 'Insights') I share some of the things I learned while working on this project.

            """
        ),
        # dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])