import pandas as pd
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px

data = pd.read_csv('complete_sales_data.csv')

app = Dash(__name__)


colors = {
    'main' : '#1f2630',
    'secondary' : '#252e3f',
    'secondText': "#2cfec1"
}


#Graph
def gen_fig(data):
    fig = px.line(data, x="date", y="sales")
    fig.update_layout(
        plot_bgcolor=colors['main'],
        paper_bgcolor=colors['secondary'],
        font_color=colors['secondText']
    )
    fig.update_traces(line=dict(color=colors['secondText']))  # dict = dictionary
    return fig;


visulization = dcc.Graph(
    id="visualization",
    figure=gen_fig(data),
    
)

#Header
header = html.H1(
    "Pink Morsel Sales",
    id="header",
    style={
        'textAlign' : 'center',
        'color': colors['secondText'],
        'margin': '40px 0',
        
    }
)

region_picker = dcc.RadioItems(
    ["all","north","east","south","west"],"all",
    id="region_picker",
    inline=True,
    style={
        'color' : colors['secondText'],
        'backgroundColor': colors['secondary'],
        'padding': '0 0 40px 0'
    }
)

@app.callback (
    Output('visualization', "figure"),
    Input('region_picker', "value")
)
def update_graph(region):
    if region == 'all':
        trimmed_data = data;
    else:
        trimmed_data = data[data["region"] == region]
    
    fig=gen_fig(trimmed_data)
    return fig

app.layout = html.Div(
    [
        header,
        visulization,
        region_picker
    ],
    style={
        "textAlign": "center",
        "background-color": colors["main"],
        'height': '100vh',
    }
)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run_server()


