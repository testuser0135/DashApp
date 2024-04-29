##################################################
# 経済・金融を学ぶ
##################################################

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# 2022/4/13 2系からこの書き方は非推奨になった
#from dash.dependencies import Output, Input, State
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

from app import app

layout = html.Div(
    id="study-body",
    children = [
        dbc.Row(
            id="common-subtitle-component",
            children = [
                html.P(
                    id="common-subtitle",
                    children = [
                        "経済・金融の勉強をしましょう"
                    ]
                )
            ]
        ),
        dbc.CardDeck(
            children = [
                dbc.Card(
                    [
                        # やっぱり画像いらない気がしてきたから一旦アウト
                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("経済をざっくり学ぶ", className="card-title"),
                                html.P(
                                    "Some quick example text",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary", href="/study_article1"),
                            ]
                        )
                    ]
                ),
                dbc.Card(
                    [
                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("金融をざっくり学ぶ", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        )
                    ]
                ),
                dbc.Card(
                    [
                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("株式投資をざっくり学ぶ", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        )
                    ]
                ),
                dbc.Card(
                    [
                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        ),
                    ],
                style={"width": "60rem"},
                ),
                # dbc.Card(
                #     [
                #         dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                #         dbc.CardBody(
                #             [
                #                 html.H4("Card title", className="card-title"),
                #                 html.P(
                #                     "Some quick example text to build on the card title and "
                #                     "make up the bulk of the card's content.",
                #                     className="card-text",
                #                 ),
                #                 dbc.Button("Go somewhere", color="primary"),
                #             ]
                #         )
                #     ]
                # ),
                # dbc.Card(
                #     [
                #         dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                #         dbc.CardBody(
                #             [
                #                 html.H4("Card title", className="card-title"),
                #                 html.P(
                #                     "Some quick example text to build on the card title and "
                #                     "make up the bulk of the card's content.",
                #                     className="card-text",
                #                 ),
                #                 dbc.Button("Go somewhere", color="primary"),
                #             ]
                #         )
                #     ]
                # )
            ]
        ),
        html.Br(),
        dbc.CardDeck(
            children = [
                dbc.Card(
                    [
                        # やっぱり画像いらない気がしてきたから一旦アウト
                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("経済をざっくり学ぶ", className="card-title"),
                                html.P(
                                    "Some quick example text",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        )
                    ]
                ),
                dbc.Card(
                    [
                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("金融をざっくり学ぶ", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        )
                    ]
                ),
                dbc.Card(
                    [
                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("連続複利", className="card-title"),
                                html.P(
                                    "投資したお金が将来いくらになるのかを考える",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        )
                    ]
                ),
                dbc.Card(
                    [
                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("証券市場をざっくり学ぶ", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        ),
                    ],
                style={"width": "60rem"},
                ),
                # dbc.Card(
                #     [
                #         dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                #         dbc.CardBody(
                #             [
                #                 html.H4("Card title", className="card-title"),
                #                 html.P(
                #                     "Some quick example text to build on the card title and "
                #                     "make up the bulk of the card's content.",
                #                     className="card-text",
                #                 ),
                #                 dbc.Button("Go somewhere", color="primary"),
                #             ]
                #         )
                #     ]
                # ),
                # dbc.Card(
                #     [
                #         dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                #         dbc.CardBody(
                #             [
                #                 html.H4("Card title", className="card-title"),
                #                 html.P(
                #                     "Some quick example text to build on the card title and "
                #                     "make up the bulk of the card's content.",
                #                     className="card-text",
                #                 ),
                #                 dbc.Button("Go somewhere", color="primary"),
                #             ]
                #         )
                #     ]
                # )
            ]
        ),
        html.Br()
        
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             children = [
        #                 html.Div(
        #                     children = [
        #                         "One of three columns", 
        #                     ]
        #                 )
        #             ],
        #             md=4
        #         ),
        #         dbc.Col(
        #             children = [
        #                 html.Div(
        #                     children = [
        #                         "One of three columns",
        #                     ]
        #                 )
        #             ],
        #             md=4
        #         ),
        #         dbc.Col(
        #             children = [
        #                 html.Div(
        #                     children = [
        #                         "One of three columns",
        #                     ]
        #                 )
        #             ],
        #             md=4
        #         )
        #     ]
        # ),
        # dbc.Row(
        #     [
        #         dbc.Col(html.Div("One of four columns"), width=6, lg=3),
        #         dbc.Col(html.Div("One of four columns"), width=6, lg=3),
        #         dbc.Col(html.Div("One of four columns"), width=6, lg=3),
        #         dbc.Col(html.Div("One of four columns"), width=6, lg=3),
        #     ]
        # )
    ]
)
