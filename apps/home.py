#################################################
# ホーム(ホームリンクがクリックされた時の中身)
#################################################

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd


from app import app

nikkei_stock_average = pd.read_csv('./assets/csv/nikkei_stock_average.csv')


# ↓これ別にlayoutという名前の変数でなくてもよい。index.pyのCallbackで使う時に「クラス名.変数名」と記述するのが味噌
layout = html.Div(
    id="home-body",
    children = [
        html.Div(
            id="first-block",
            children = [
                html.Div(
                    id="img-wrap",
                    children = [
                        html.Div(
                            id="img-wrap-inner-content",
                            children = [
                                html.P(
                                    id="text1",
                                    children = [
                                        "バナナは世界を救う"
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        html.Div(
            id="second-block",
            children = [
                html.Div(
                    id="topnews-block",
                    children = [
                        "一押しの知らせ",
                        html.Br(),
                        "ここにHPのタイトルにあったメッセージを入れる。動きがあればなおよし"
                    ]
                ),
                html.Div(
                    id="news-block",
                    children = [
                        html.Div(
                            id="news-block-title",
                            children = [
                                "ここはニュースブロックのタイトルです"
                            ]
                        ),
                        dbc.CardDeck(
                            id="news",
                            children = [
                                dbc.Card(
                                    [
                                        # やっぱり画像いらない気がしてきたから一旦アウト
                                        # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                                        dbc.CardBody(
                                            [
                                                html.H4("Card title", className="card-title"),
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
                                                html.H4("Card title", className="card-title"),
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
                                        )
                                    ]
                                )
                            ]
                        ) 
                    ]
                ),
                dcc.Graph(
                    figure=px.line(
                        data_frame=nikkei_stock_average,
                        x="year",
                        y="stock_price", 
                        title="日経平均株価"
                    )
                )
            ]
        ),
        "home"
    ]
)
