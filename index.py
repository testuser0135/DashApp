import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

from app import app
from apps import home, domestic, world, study, contact, study_article1

app.layout = html.Div(
    id="all-body",
    children = [
        # BootstrapのNavbarSimpleっていうヘッダー的なものを使ってみる # 画面遷移してもヘッダーは固定
        dbc.NavbarSimple(
            id="navbar-edit",
            className="bg-light-override",
            fixed="top",
            children = [
                dcc.Location(id='url'), # リンクに飛べるようにする呪文
                dbc.NavItem(dbc.NavLink("ホーム", href="/")),
                dbc.DropdownMenu(
                    children = [
                        dbc.DropdownMenuItem("More pages", header=True),
                        dbc.DropdownMenuItem("ホーム", href="/"),
                        dbc.DropdownMenuItem("国内企業", href="/domestic"),
                        dbc.DropdownMenuItem("海外企業", href="/world"),
                        dbc.DropdownMenuItem("経済・金融を学ぶ", href="/study"),
                        dbc.DropdownMenuItem("お問い合わせ", href="/contact")
                    ],
                    nav=True,
                    in_navbar=True,
                    label="More"
                )
            ],
            brand="Bnana Co., Ltd",
            brand_href="/",
        ),
        # ここに色々と中身が入る。画面遷移によって可変する。
        # 中のコンポーネントが画面いっぱいに広がらないようにpadding:1%するためにdivで囲う。画面いっぱいだと見づらいから。
        html.Div(
            id="page-content",
        ),
        # 画面遷移してもフッターは固定
        html.Footer(

            children = [
                html.P(
                    "©️2021　banana"
                )
            ]
        )
    ]
)


# 画面遷移
@app.callback(
    Output("page-content", "children"),
    [
        Input("url", "pathname")
    ]
)
def display_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/domestic":
        return domestic.layout
    elif pathname == "/world":
        return world.layout
    elif pathname == "/study":
        return study.layout
    elif pathname == "/contact":
        return contact.layout
    elif pathname == "/study_article1":
        return study_article1.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port = 10000, debug = True)
    # app.run_server(debug=True)
