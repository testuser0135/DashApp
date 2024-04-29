##################################################
# 経済・金融を学ぶ　の記事１
##################################################

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
#from dash.dependencies import Output, Input, State
from dash import Dash, dcc, html, Input, Output

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
                        "金融を学ぶ"
                    ]
                )
            ]
        ),
        html.Div(
            id="content",
            children = [
                html.Div(
                    id="table-of-contents",
                    children = [
                        html.H4(
                            "目次"
                        ),
                        html.Ol(
                            children = [
                                html.Li(
                                    html.A(
                                        href="#section1",
                                        children = [
                                            "金融を学ぶことの意味"
                                        ]
                                    )
                                ),
                                html.Li(
                                    html.A(
                                        href="#section2",
                                        children = [
                                            "「金融」とは？"
                                        ]
                                    )
                                ),
                                html.Li(
                                    html.A(
                                        href="#section3",
                                        children = [
                                            "金融市場の大きさ"
                                        ]
                                    )
                                ),
                                html.Li(
                                    html.A(
                                        href="#section4",
                                        children = [
                                            "金融業界の動向"
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    id="aaa",
                    children = [
                        dbc.Col(
                            children = [
                                html.Div(
                                    className="section",
                                    id="section1",
                                    children = [
                                        "金融を学ぶことの意味"
                                    ]
                                ),
                                html.Div(
                                    children = [
                                        "aaa"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    id="aaa",
                    children = [
                        dbc.Col(
                            children = [
                                html.Div(
                                    className="section",
                                    id="section2",
                                    children = [
                                        "「金融」とは？"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    id="aaa",
                    children = [
                        dbc.Col(
                            children = [
                                html.Div(
                                    className="section",
                                    id="section3",
                                    children = [
                                        "金融市場の大きさ"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    id="aaa",
                    children = [
                        dbc.Col(
                            children = [
                                html.Div(
                                    className="section",
                                    id="section4",
                                    children = [
                                        "金融業界の動向"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    id="aaa",
                    children = [
                        dbc.Col(
                            children = [
                                html.Div(
                                    className="section",
                                    id="section5",
                                    children = [
                                        "6aaaaaaaaaaaaa"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    id="aaa",
                    children = [
                        dbc.Col(
                            children = [
                                html.Div(
                                    className="section",
                                    id="section6",
                                    children = [
                                        "6aaaaaaaaaaaaa"
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dbc.Row(
                    id="aaa",
                    children = [
                        dbc.Col(
                            children = [
                                html.Div(
                                    className="section",
                                    id="section7",
                                    children = [
                                        "6aaaaaaaaaaaaa"
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)



