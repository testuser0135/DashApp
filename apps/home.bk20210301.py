#################################################
# ホーム(ホームリンクがクリックされた時の中身)
#################################################

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

# ↓これ別にlayoutという名前の変数でなくてもよい。index.pyのCallbackで使う時に「クラス名.変数名」と記述するのが味噌
layout = html.Div(
    id="home-body",
    children = [
        html.Div(
            id="img-wrap",
            children = [
                html.Img(
                    id="neo-future-img",
                    src=app.get_asset_url('neo_future.jpg')
                ),
                html.P(
                    style={
                        "position": "absolute",
                        "top": "30%",
                        "left": "50%",
                        "transform": "translate(-50%,-50%)",
                        "margin": 0,
                        "padding": 0,
                        "font-family": "Quicksand, sans-serif"
                        },
                    children = [
                        "aaaaaaaaaaaaaaaa"
                    ]
                )
            ]
        ),
        "home"
    ]
)