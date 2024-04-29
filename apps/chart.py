import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import pandas as pd
from skimage import data

from app import app

basic_chart_list = ["scatter", 
                    "line", 
                    "bar", 
                    "area", 
                    "pie", 
                    "treemap", 
                    "sunburst", 
                    "icicle"]
statistical_chart_list = ["density_heatmap", 
                          "histogram", 
                          "parallel_categories", 
                          "box", 
                          "scatter_matrix", 
                          "violin", 
                          "strip"]
scientific_chart_list = ["imshow", 
                         "imshow_jpeg", 
                         "scatter_ternary", 
                         "scatter_polar", 
                         "line_polar", 
                         "parallel_coordinates"]
map_list = ["choropleth_mapbox", 
            "scatter_geo", 
            "scatter_mapbox", 
            "line_geo", 
            "density_mapbox"]


radio_b1 = dcc.RadioItems(id="radio_b1", options=basic_chart_list, value="scatter", labelStyle={'display': 'inline-block', 'margin-right': '2%'})
my_graph1 = dcc.Graph(id="basic_chart")
radio_b2 = dcc.RadioItems(id="radio_b2", options=statistical_chart_list, value="density_heatmap", labelStyle={'display': 'inline-block', 'margin-right': '2%'})
my_graph2 = dcc.Graph(id="statistical_chart")
radio_b3 = dcc.RadioItems(id="radio_b3", options=scientific_chart_list, value="imshow", labelStyle={'display': 'inline-block', 'margin-right': '2%'})
my_graph3 = dcc.Graph(id="scientific_chart")
radio_b4 = dcc.RadioItems(id="radio_b4", options=map_list, value="choropleth_mapbox", labelStyle={'display': 'inline-block', 'margin-right': '2%'})
my_graph4 = dcc.Graph(id="maps")

layout = html.Div(
    id = "chart-body",
    children = [
        dbc.Row(
            id="common-subtitle-component",
            children = [
                html.P(
                    id="common-subtitle",
                    children = [
                        "チャート一覧"
                    ]
                )
            ]
        ),
        html.Div(
            id = "first", 
            children = [
                html.H3(
                    id="title1",
                    children = [
                        "基本のチャート"
                    ]
                ),
                radio_b1, 
                my_graph1, 
            ]
        ), 
        html.Div(
            id = "second", 
            children = [
                html.H3(
                    id="title2",
                    children = [
                        "統計のチャート"
                    ]
                ),
                radio_b2, 
                my_graph2
            ]
        ),
        html.Div(
            id = "third", 
            children = [
                html.H3(
                    id="title3",
                    children = [
                        "科学のチャート"
                    ]
                ),
                radio_b3, 
                my_graph3
            ]
        ), 
        html.Div(
            id = "forth", 
            children = [
                html.H3(
                    id="title4",
                    children = [
                        "地図"
                    ]
                ),
                radio_b4, 
                my_graph4
            ]
        )
    ]
)


@app.callback(Output("basic_chart", "figure"),
              Input("radio_b1", "value"))
def update_graph(value):
    if value == "scatter":
        df = px.data.iris()
        fig = px.scatter(df, x='sepal_width', y='sepal_length')
    elif value == "line":
        df = px.data.stocks()
        fig = px.line(df, x='date', y='GOOG')
    elif value == "bar":
        df = px.data.medals_long()
        fig = px.bar(df, x='nation', y='count', color='medal')
    elif value == "area":
        df = px.data.medals_long()
        fig = px.area(df, x='medal', y='count', color='nation')
    elif value == "pie":
        df = px.data.tips()
        fig = px.pie(df, values='tip', names='day')
    elif value == "treemap":
        df = px.data.tips()
        fig = px.treemap(df, path=[px.Constant("all"), 'sex', 'day', 'time'], values='total_bill')
    elif value == "sunburst":
        df = px.data.tips()
        fig = px.sunburst(df, path=['day', 'time', 'sex'],values='total_bill')
    elif value == "icicle":
        df = px.data.tips()
        fig = px.icicle(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
        fig.update_traces(root_color='lightgrey')
    else:
        fig = None
    return fig

@app.callback(Output("statistical_chart", "figure"),
              Input("radio_b2", "value"))
def update_graph(value):
    if value == "density_heatmap":
        df = px.data.tips()
        fig = px.density_heatmap(df, x='total_bill', y='tip')
    elif value == "histogram":
        df = px.data.tips()
        fig = px.histogram(df, x='total_bill')
    elif value == "parallel_categories":
        df = px.data.tips()
        fig=px.parallel_categories(df)
    elif value == "box":
        df = px.data.tips()
        fig = px.box(df, x='time', y='total_bill')
    elif value == "scatter_matrix":
        df = px.data.iris()
        fig = px.scatter_matrix(df)
    elif value == "violin":
        df = px.data.tips()
        fig = px.violin(df, y='total_bill', box=True)
    elif value == "strip":
        df = px.data.tips()
        fig = px.strip(df, x='total_bill', y='day')
    else:
        fig = None
    return fig

@app.callback(Output("scientific_chart", "figure"),
              Input("radio_b3", "value"))
def update_graph(value):
    if value == "imshow":
        df = px.data.medals_wide(indexed=True)
        fig = px.imshow(df)
    elif value == "imshow_jpeg":
        img = data.astronaut()
        fig = px.imshow(img, binary_format='jpeg', binary_compression_level=0)
    elif value == "scatter_ternary":
        df = px.data.election()
        fig = px.scatter_ternary(df, a='Joly', b='Coderre', c='Bergeron')
    elif value == "scatter_polar":
        df = px.data.wind()
        fig = px.scatter_polar(df, r='frequency', theta='direction')
    elif value == "line_polar":
        df = pd.DataFrame(dict(r=[1, 5, 2, 2, 3], theta=['processing cost', 'mechanical properties', 'chemical stability', 'thermal stability', 'device integration']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    elif value == "parallel_coordinates":
        df = px.data.iris()
        fig = px.parallel_coordinates(df, color='species_id')
    else:
        fig = None
    return fig

@app.callback(Output("maps", "figure"),
              Input("radio_b4", "value"))
def update_graph(value):
    if value == "choropleth_mapbox":
        df = px.data.election()
        geojson = px.data.election_geojson()
        fig = px.choropleth_mapbox(df, geojson=geojson, color='Bergeron', locations='district', featureidkey='properties.district',center={'lat': 45.5517, 'lon': -73.7073},  mapbox_style='carto-positron', zoom=9)
    elif value == "scatter_geo":
        df = px.data.gapminder().query('year==2007')
        fig = px.scatter_geo(df, locations='iso_alpha', color='continent', hover_name='country', size='pop', projection='natural earth')
    elif value == "scatter_mapbox":
        df = pd.read_csv( 'https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv')
        fig = px.scatter_mapbox(df, lat='lat', lon='lon', hover_name='City', hover_data=['State', 'Population'], zoom=3, height=600)
        fig.update_layout(mapbox_style='open-street-map')
    elif value == "line_geo":
        df = px.data.gapminder().query('year==2007')
        fig = px.line_geo(df, locations='iso_alpha', color='continent', projection='orthographic')
    elif value == "density_mapbox":
        df = pd.read_csv( 'https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
        fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10, center=dict(lat=0, lon=180), zoom=0, mapbox_style='stamen-terrain')
    else:
        fig = None
    return fig
