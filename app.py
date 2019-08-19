import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "GDP growth by countries"
mytitle = "GDP annual growth rate by 3 countries"
x_values = ['2009', '2010', '2011', '2012', '2013']
y1_values = [-8, 11, 9, 4,2]
y2_values = [-13, 5, 9, 0, 7]
y3_values = [-17, 11, 8, 0, 1]
color1 = '#fc9403'
color2 = '#0307fc'
color3 = '#9003fc'
name1 = 'United States'
name2 = 'United Kingdoms'
name3 = 'Candata'
tabtitle = 'GDP source'
sourceurl = 'https://wits.worldbank.org/CountryProfile'
githublink = 'https://github.com/ylcgu'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
