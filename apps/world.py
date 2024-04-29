##################################################
# 世界企業
##################################################

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

from app import app

layout = html.Div(
    id="world-body",
    children = [
        "world"
    ]
)
