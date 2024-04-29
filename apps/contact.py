##################################################
# お問い合わせ
##################################################

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output

from app import app

# layout = html.Div(
#     id="contact-body",
#     children = [
#         "contact"
#     ]
# )

email_input = dbc.Row([
        dbc.Label("Email"
                , html_for="example-email-row"
                , width=2),
        dbc.Col(dbc.Input(
                type="email"
                , id="example-email-row"
                , placeholder="Enter email"
            ),width=10,
        )],className="mb-3"
)
user_input = dbc.Row([
        dbc.Label("Password", html_for="example-name-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text"
                , id="example-name-row"
                , placeholder="Enter name"
                , maxLength = 80
            ),width=10
        )], className="mb-3"
)
message = dbc.Row([
        dbc.Label(
            "Message",
            align = 'start',
            html_for="example-message-row", width=2)
        ,dbc.Col(
            dbc.Textarea(
                id = "example-message-row",
                className="mb-3",
                placeholder="Enter message",
                required = True,
                style={'height': 120}
                ),
            width=10
            )
        ], className="mb-3")

markdown = ''' バナナの花言葉を知っていますか？  
            \nバナナは別名で「実芭蕉(みばしょう)」とも呼ばれますが、芭蕉という名の通り特徴のある大きな葉を持っています。  
            大きな葉を風に揺らしながら、堂々と立つその姿から「風格」の花言葉が付きました。  
            \n弊社はそんなバナナのようにどっしりと構えて、皆様からの温かいお言葉もちょっと厳しいお言葉も真摯に受け止めます。'''

layout = html.Div(
    id = "domestic-body",           
    children = [ 
        dbc.Row(
            id="common-subtitle-component",
            children = [
                html.P(
                    id="common-subtitle",
                    children = [
                        "お問い合わせフォーム"
                    ]
                )
            ]
        ), 
        dbc.Container(
            children = [
                dcc.Markdown(markdown),
                html.Br(),
                dbc.Card(
                    dbc.CardBody(
                        children = [
                            dbc.Form(
                                children = [
                                    email_input,
                                    user_input,
                                    message
                                ]
                            ),
                            html.Div(
                                id = 'div-button',
                                children = [
                                    dbc.Button(
                                        'Submit',
                                        color = 'primary',
                                        id='button-submit',
                                        n_clicks = 0
                                    )
                                ]
                            )
                        ]
                    )
                ),
                html.Br(),
                html.Br()
            ]
        )
    ]
)
