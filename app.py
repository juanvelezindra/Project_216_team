import os
from datetime import date
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objs as go
import numpy as np
from dash import html

# Create the app

workspace_user = os.getenv('JUPYTERHUB_USER')  # Get DS4A Workspace user name
request_path_prefix = '/'
if workspace_user:
    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'

app = Dash(__name__, requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])
app.title = 'Anti-corruption'                 

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
# Layout
sidebar = html.Div(
    [
        html.Img(src=app.get_asset_url('images/logo.jpg')),
        html.Hr(),
        html.P(
            "Anti-corruption", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href=request_path_prefix, active="exact"),
                dbc.NavLink("Graphics", href=request_path_prefix+"page-1", active="exact"),
                dbc.NavLink("Tables", href=request_path_prefix+"page-2", active="exact"),
                dbc.NavLink("Predictions", href=request_path_prefix+"page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

page1_tab1 = html.Div(
    [
        html.Hr(),
        html.H1("Hypothesis 1 Exploratory Data Analysis EDA"),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Select(
                            id="select",
                            placeholder="Graphic type",
                            options=[
                                {"label": "Scatter", "value": "1"},
                                {"label": "Bar", "value": "2"},
                                {"label": "His", "value": "3"},
                                {"label": "Box", "value": "4"},
                                {"label": "Violin", "value": "5"},
                                {"label": "Pie", "value": "6"},
                            ],
                        ),
                    ],
                    width=4,
                ),
                
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            end_date=date(2017, 8, 25),
                        ),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2022, 6, 10),
                            initial_visible_month=date(2022, 6, 10),
                            end_date=date(2022, 6, 10),
                        ),
                    ],
                    width=4,
                ),
            ],
            className="g-3",
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Button(
                            "Execute",
                            color="primary",
                            id="button",
                            className="mb-3",
                        ),
                    ]
                 )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        html.Img(src=app.get_asset_url('images/scatter.png')),
                    ]
                 )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        html.Img(src=app.get_asset_url('images/hist.png')),
                    ]
                 )
            ]
        ),
    ]
)


page1_tab2 = html.Div(
    [
        html.Hr(),
        html.H1("Hypothesis 2 Exploratory Data Analysis EDA"),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Select(
                            id="select",
                            placeholder="Graphic type",
                            options=[
                                {"label": "Scatter", "value": "1"},
                                {"label": "Bar", "value": "2"},
                                {"label": "His", "value": "3"},
                                {"label": "Box", "value": "4"},
                                {"label": "Violin", "value": "5"},
                                {"label": "Pie", "value": "6"},
                            ],
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dbc.Select(
                            id="select",
                            placeholder="Analysis type",
                            options=[
                                {"label": "Contracts", "value": "1"},
                                {"label": "Suppliers", "value": "2"},
                                {"label": "Entities", "value": "3"},
                            ],
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            end_date=date(2017, 8, 25),
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2022, 6, 10),
                            initial_visible_month=date(2022, 6, 10),
                            end_date=date(2022, 6, 10),
                        ),
                    ],
                    width=3,
                ),
            ],
            className="g-3",
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Button(
                            "Execute",
                            color="primary",
                            id="button",
                            className="mb-3",
                        ),
                    ]
                 )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        html.Img(src=app.get_asset_url('images/scatter.png')),
                    ]
                 )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        html.Img(src=app.get_asset_url('images/hist.png')),
                    ]
                 )
            ]
        ),
    ]
)



table_header = [
    html.Thead(html.Tr([html.Th("Entity name"), html.Th("Nit entity"), html.Th("Department"), html.Th("Town"), html.Th("Id contract"), html.Th("Supplier awarded")]))
]

row1 = html.Tr([html.Td("DIRECCION GENERAL MARITIMA-DIMAR"), html.Td("899.999.428"), html.Td("Bolívar"), html.Td("Cartagena"), html.Td("CO1.PCCNTR.1452428"), html.Td("NATALIA RAYO IBARRA")])
row2 = html.Tr([html.Td("MUNICIPIO DE TOCANCIPA"), html.Td("901.540.945"), html.Td("Cundinamarca"), html.Td("Tocancipá"), html.Td("CO1.PCCNTR.2770565"), html.Td("ANALIDA DIAZ ALDANA")])
row3 = html.Tr([html.Td("GOBERNACION NORTE DE SANTANDER"), html.Td("900.959.048"), html.Td("Norte de Santander"), html.Td("Cúcuta"), html.Td("CO1.PCCNTR.3673185"), html.Td("ANGELICA RODRIGUEZ")])
row4 = html.Tr([html.Td("ALCALDIA MUNICIPIO DE ARAUCA"), html.Td("899.999.004"), html.Td("Arauca"), html.Td("Arauca"), html.Td("CO1.PCCNTR.2804706"), html.Td("JULIANA MORALES MORALES")])

table_body = [html.Tbody([row1, row2, row3, row4])]

table = dbc.Table(table_header + table_body, bordered=True)

page2_tab1 = html.Div(
    [
        html.Hr(),
        html.H1("Hypothesis 1 Data Sources"),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Select(
                            id="select",
                            placeholder="Data Source",
                            options=[
                                {"label": "Electronic Contracts", "value": "1"},
                                {"label": "Registered Suppliers", "value": "2"},
                                {"label": "Contract Process", "value": "3"},
                                {"label": "Additions", "value": "4"},
                                {"label": "PAA", "value": "5"},
                            ],
                        ),
                    ],
                    width=4,
                ),
                
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            end_date=date(2017, 8, 25),
                        ),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2022, 6, 10),
                            initial_visible_month=date(2022, 6, 10),
                            end_date=date(2022, 6, 10),
                        ),
                    ],
                    width=4,
                ),
            ],
            className="g-3",
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Button(
                            "Execute",
                            color="primary",
                            id="button",
                            className="mb-3",
                        ),
                    ]
                 )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        table,
                    ]
                 )
            ]
        ),
    ]
)

page2_tab2 = html.Div(
    [
        html.Hr(),
        html.H1("Hypothesis 2 Data Sources"),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Select(
                            id="select",
                            placeholder="Data Source",
                            options=[
                                {"label": "Electronic Contracts", "value": "1"},
                                {"label": "Registered Suppliers", "value": "2"},
                                {"label": "Contract Process", "value": "3"},
                                {"label": "Additions", "value": "4"},
                                {"label": "PAA", "value": "5"},
                            ],
                        ),
                    ],
                    width=4,
                ),
                
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            end_date=date(2017, 8, 25),
                        ),
                    ],
                    width=4,
                ),
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2022, 6, 10),
                            initial_visible_month=date(2022, 6, 10),
                            end_date=date(2022, 6, 10),
                        ),
                    ],
                    width=4,
                ),
            ],
            className="g-3",
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Button(
                            "Execute",
                            color="primary",
                            id="button",
                            className="mb-3",
                        ),
                    ]
                 )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        table,
                    ]
                 )
            ]
        ),
    ]
)

page3_tab1 = html.Div(
    [
        html.Hr(),
        html.H1("Prediction Models"),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Label("Choose hypothesis"),
                        dbc.Select(
                            id="select",
                            placeholder="Hypothesis",
                            options=[
                                {"label": "Hypothesis 1", "value": "1"},
                                {"label": "Hypothesis 2", "value": "2"},
                                {"label": "Hypothesis 3", "value": "3"},
                                {"label": "Hypothesis 4", "value": "4"},
                            ],
                        ),
                    ],
                    width=3,
                 ),
                dbc.Col(
                    [
                        dbc.Label("Choose model"),
                        dbc.Select(
                            id="select",
                            placeholder="Models",
                            options=[
                                {"label": "Linear regression", "value": "1"},
                                {"label": "Multiple linear regression", "value": "2"},
                                {"label": "Logistic regression", "value": "3"},
                                {"label": "Deep learning", "value": "4"},
                            ],
                        ),
                    ],
                    width=3,
                 ),
                dbc.Col(
                    [
                        dbc.Label("Choose source"),
                        dbc.Select(
                            id="select",
                            placeholder="Sources",
                            options=[
                                {"label": "Electronic Contracts", "value": "1"},
                                {"label": "Registered Suppliers", "value": "2"},
                                {"label": "Contract Process", "value": "3"},
                                {"label": "Additions", "value": "4"},
                                {"label": "PAA", "value": "5"},
                            ],
                        ),
                    ],
                    width=3,
                 ),
                dbc.Col(
                    [
                        dbc.Label("Choose schema"),
                        dbc.Select(
                            id="select",
                            placeholder="Schemas",
                            options=[
                                {"label": "Contracts", "value": "1"},
                                {"label": "Suppliers", "value": "2"},
                                {"label": "Entities", "value": "3"},
                            ],
                        ),
                    ],
                    width=3,
                 )
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            initial_visible_month=date(2017, 8, 5),
                            end_date=date(2017, 8, 25),
                        ),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2022, 6, 10),
                            initial_visible_month=date(2022, 6, 10),
                            end_date=date(2022, 6, 10),
                        ),
                    ],
                    width=6,
                ),
             ]
        ),
        html.Br(),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        dbc.Button(
                            "Run",
                            color="primary",
                            id="button",
                            className="mb-3",
                        ),
                    ]
                 )
            ]
        ),
        html.Br(),
        dbc.Card("Chi Square", body=True),
        dbc.Card(
            dbc.CardBody("The proportion of subjects who reported being depressed did not differ by marriage, X2 (1, N = 104) = 1.7, p > .05. There is a significant relationship between the two variables. Hipsters are more likely than non-hipsters to own an IPhone, X2 (1, N = 54) = 6.7, p < .01. A chi-square test of independence showed that there was no significant association between gender and chocolate preference, X2 (2, N = 88) = 2.1, p = .35."),
            className="mb-3",
        ),
        dbc.Row(
            [
                 dbc.Col(
                    [
                        html.Img(src=app.get_asset_url('images/maps.png')),
                    ],
                    width=12,
                 )
            ]
        ),
    ]
)

page0_tab1 = html.Div(
    [
        dbc.Carousel(
            items=[
                 {
                    "key": "1",
                    "src": app.get_asset_url('images/anticorruption1.png'),
                    "header": "Corruption as a Political Phenomenon",
                    "caption": "Corruption—the appropriate of public resources for private purposes",
                },
                {
                    "key": "2",
                    "src": app.get_asset_url('images/anticorruption2.png'),
                    "header": "WHAT IS CORRUPTION?",
                    "caption": "Corruption erodes trust and weakens democracy.",
                },
                {
                    "key": "3",
                    "src": app.get_asset_url('images/anticorruption3.png'),
                    "header": "Political and Institutional corruption",
                    "caption": "The ‘corruption’ can be interpreted as any act of dishonest behaviour",
                },
                
                
            ],
            controls=True,
            indicators=True,
        ),
        html.Hr(),
        dbc.Tabs(
            [
                dbc.Tab(
                    html.Div(
                        [
                            html.Br(),
                            html.P("In order to answer the main issue of the project, whether there is abnormal concentration of contracts in the public sector, an initial exploratory data analysis was made through the large databases of SECOP II (Electronic System of public contracting), where are recorded the processes, public entities, suppliers and the representative caracteristicas of contracts in the public sector of colombia."),
                            html.Br(),
                            html.P("To begin with, a brief description of the characteristics of variables from the tables (Contracts, Suppliers, Additions) documented in the sourced data document is presented. Then to prepare the data appropriately and to reach consistency and relevance in the data a data cleaning procedure  was made."),
                            html.Br(),
                            html.P("Finally, trying to focus on the most relevant variables and tables that are going to help to  answer the next questions, a summary of data with statistics and graphics of the variables  is shown."),
                            html.Br(),
                        ]
                    ), 
                    label="Presentation"
                ),
                dbc.Tab(
                    html.Div(
                        [
                            html.Br(),
                            html.P("As the first step all the tables were analyzed in order to explore the data that contains each one. With this activity is expected to determine the Data Quality, Specific data types, pertinence of information and a brief data description for each one."),
                            html.Br(),
                            html.P("The analysis for each table was done using directly in notebooks and using pandas profiling which can show the main information summary. Following is the validation for each table."),
                            html.Br(),
                        ]
                    ), 
                    label="Problematic"),
                dbc.Tab(
                    html.Div(
                        [
                            html.Br(),
                            html.P("Hypothesis 1"),
                            html.P("Are there natural persons awarded with a group of contracts that cannot fulfill the purpose of the contract due to its inability to execute it.Either because it does not have the man-hours available or the resources required for such a purpose?"),
                            html.Br(),
                            html.P("Hypothesis 2"),
                            html.P("How behave the concentration of contracts in different geographical areas where both, the contracting entity and the contractor, are located?"),
                            html.Br(),
                            html.P("Hypothesis 3"),
                            html.P("Is there some correlation between the different time periods with the increase or decrease in contracting?"),
                            html.Br(),
                            html.P("Hypothesis 4"),
                            html.P("How inefficiency in the contracting entities affects natural persons due to vacant time (mandatory vacations) between contracts?"),
                            html.Br(),
                        ]
                    ), 
                    label="Hypothesis"),
            ]
        ),
    ]
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Callbacks

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return page0_tab1
    elif pathname == "/page-1":
        htmlretorno = dbc.Tabs(
            [
                dbc.Tab(page1_tab1, label="Hypothesis 1"),
                dbc.Tab(page1_tab2, label="Hypothesis 2"),
                dbc.Tab(page1_tab1, label="Hypothesis 3"),
                dbc.Tab(page1_tab2, label="Hypothesis 4"),
            ]
        )
        return htmlretorno
    elif pathname == "/page-2":
        htmlretorno = dbc.Tabs(
            [
                dbc.Tab(page2_tab1, label="Hypothesis 1"),
                dbc.Tab(page2_tab2, label="Hypothesis 2"),
                dbc.Tab(page2_tab1, label="Hypothesis 3"),
                dbc.Tab(page2_tab1, label="Hypothesis 4"),
            ]
        )
        return htmlretorno
    elif pathname == "/page-3":
        return page3_tab1
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# Start the server
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)