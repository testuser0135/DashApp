#################################################
# 国内企業
#################################################

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, dash_table
import plotly.express as px
import pandas as pd

from app import app

# csv読み込み→Dataframe形式にする
df = pd.read_csv('./assets/csv/uriage.csv')
df_transform = pd.read_csv('./assets/csv/uriage.csv', index_col="quoter").T # インデックスをquoter列に指定し、行列を入れ替える(転置)

# 直後のfor文で列名を格納するために空のリスト作成
crp_list=[]
# 上で読み込んだcsvのquoter列以外の列名をcrp_listリストに格納→ドロップダウンの選択肢として使用する
for column_name in df:
    if column_name != "quoter":
        crp_list.append(column_name)

# 空のグラフオブジェクトを作成しておく。これがないとうまくいかないんだなあ。
fig_fake={}

layout = html.Div(
    id="domestic-body",
    children = [
        dbc.Row(
            id="common-subtitle-component",
            children = [
                html.P(
                    id="common-subtitle",
                    children = [
                        "企業を知れば世界がわかる"
                    ]
                )
            ]
        ),
        # 以下でグラフとテーブルを配置
        html.Div(
            id="graph-and-table-space",
            style={"padding": "3%"},
            children = [
                dcc.Dropdown(
                    id="selection",
                    options=[{"label": c, "value": c} for c in crp_list],
                    searchable=False,
                    # 初期値として選択肢のいずれかを設定しておかないとエラーになる
                    value="NTTデータ"
                ),
                # グラフ
                dcc.Graph(
                    id='amount_of_sales-graph',
                    figure=fig_fake
                ),
                # テーブル
                # 列と行が逆の方がいいかもしれない
                html.Div(
                    id="various_index_table"
                )
            ]
        ),
        # なんかおしゃれだからBootstrapのCardてのを使ってみる
        dbc.CardGroup(
            children = [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Card 1", className="card-title"),
                            html.P(
                                "This card has some text content, which is a little "
                                "bit longer than the second card.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="success", className="mt-auto"
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        children = [
                            html.H5("Card 2", className="card-title"),
                            html.P(
                                "This card has some text content.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="warning", className="mt-auto"
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        children = [
                            html.H5("Card 3", className="card-title"),
                            html.P(
                                "This card has some text content, which is longer "
                                "than both of the other two cards, in order to "
                                "demonstrate the equal height property of cards in a "
                                "card group.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto"
                            ),
                        ]
                    )
                ),
            ]
        ), 
        html.Br()
    ]
)

# コールバック関数の定義→要はユーザの操作に従ってリアクションをとるようにする
@app.callback(
    Output("amount_of_sales-graph", "figure"),
    [
        Input("selection", "value")
    ]
)
def update_graph(value_chosen):
    # 序盤でcsvを読み込んでいるため再度ここで読み込む必要はない
    # df = pd.read_csv('./asset/uriage.csv')
    return px.bar(df, x="quoter", y=value_chosen, title=value_chosen+"の売上高の推移", labels={value_chosen:"売上高","quoter":"年"}) #labelsでのラベル名変更は運良くx,yにしか作用しないらしい

# テーブルを動的に生成
@app.callback(
    Output("various_index_table", "children"),
    [
        Input("selection", "value")
    ]
)
# それぞれの項目を行名に、年を列名に設定ver
# def update_table(value_chosen):
#     # indexを「quoter」に選択した状態で、もとのcsvを転置(行列入れ替え)する
#     df_transform = pd.read_csv('.//Application/assets/csv/uriage.csv', index_col="quoter").T
#     # 行追加①「売上高総利益率」
#     df_transform.loc['売上高総利益率'] = 0
#     # 行追加②「(売上高)営業利益率」
#     df_transform.loc['営業利益率'] = df_transform.loc[value_chosen] * 100
#     # 行追加③「(売上高)経常利益率」
#     df_transform.loc['経常利益率'] = df_transform.loc[value_chosen] * 200
#     # 行追加④「(売上高)当期純利益率」
#     df_transform.loc['当期純利益率'] = df_transform.loc[value_chosen] * 300
#     # 行追加⑤「(売上高)販管費率」
#     df_transform.loc['販管費率'] = df_transform.loc[value_chosen] * 50
#     # 行名を指定し、df_transformから指定行のみ抽出する
#     # value_chosenは企業名
#     df_trans = df_transform.loc[[value_chosen, '売上高総利益率', '営業利益率', '経常利益率', '当期純利益率', '販管費率']]
#     df_trans = df_trans.rename(index={value_chosen:'売上高'})
#     # インデックスをリセット
#     df_transform_reset_index = df_trans.reset_index()
#     # インデックスをリセットしただけではいい感じのデータフレームにならなかったから一部カラム名変更
#     df_transform_rename_index = df_transform_reset_index.rename(columns={'index': 'quoter'})
#     return dash_table.DataTable(
#         columns = [{"name": str(i), "id": str(i)} for i in (df_transform_rename_index.columns)],
#         data = df_transform_rename_index.to_dict('records')
#         )

# 年を行名に、それぞれの項目を列名に設定ver
def update_table(value_chosen):
    # 値は架空
    df_uriage = pd.read_csv('./assets/csv/uriage.csv')
    # df_sourieki = pd.read_csv('./assets/csv/sourieki.csv')
    # df_eigyorieki = pd.read_csv('./assets/csv/eigyorieki.csv')
    # 列追加①「売上高総利益率」
    df_result = pd.DataFrame()
    df_result['quoter'] = df_uriage['quoter']
    df_result['売上高'] = df_uriage[value_chosen] 
    df_result['売上高総利益率'] =  180 / df_uriage[value_chosen]  # 値は架空 本当は、df_sourieki[value_chosen] / df_uriage[value_chosen]
    # 列追加②「(売上高)営業利益率」
    df_result['営業利益率'] = 120 / df_uriage[value_chosen]  # 値は架空 本当は、df_eigyorieki[value_chosen] / df_uriage[value_chosen]
    # 列追加③「(売上高)経常利益率」
    df_result['経常利益率'] = 90 / df_uriage[value_chosen]  # 値は架空
    # 列追加④「(売上高)当期純利益率」
    df_result['当期純利益率'] = 30 / df_uriage[value_chosen]  # 値は架空
    # 列追加⑤「(売上高)販管費率」
    df_result['販管費率'] = 60 / df_uriage[value_chosen]  # 値は架空
    # テーブルを返す
    return dash_table.DataTable(
        columns = [{"name": str(i), "id": str(i)} for i in (df_result.columns)],
        data = df_result.to_dict('records')
        )
