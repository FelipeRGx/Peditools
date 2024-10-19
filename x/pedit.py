import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State


# Load data

def plot_growth_chart(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    weight = child_data["Weight"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors

    
    percentiles_fill = [
        ("2nd (2.3rd)", "5th", "rgba(255,0,0,0.25)"),
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),
        ("10th", "25th", "rgba(255, 234, 0,0.225)"),
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),
        ("75th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "98th (97.7th)", "rgba(255,0,0,0.25)")
    ]


    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_months, y=weight, mode='lines+markers', name='Child Data'))
    
    # Plotting the WHO reference data
    percentiles = [2.3, 5, 10, 25, 50, 75, 90, 95, 97.7]
    colors = ["#FF4500", "#FF7F50", "#FFA500", "#FFD700", "#32CD32", "#FFD700", "#FFA500", "#FF7F50", "#FF4500"]
    
    for perc, color in zip(percentiles, colors):
        if perc == 2.3:
            label = "2nd (2.3rd)"
        elif perc == 97.7:
            label = "98th (97.7th)"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="Child's Weight Growth Chart",
                      xaxis_title="Age (Months)",
                      yaxis_title="Weight (Kg)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig



def plot_length_weight(child_data, reference_data):
    # Extracting data from the child dataframe
    length = child_data["Length"].values
    weight = child_data["Weight"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("2nd (2.3rd)", "5th", "rgba(255,0,0,0.25)"),
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),
        ("10th", "25th", "rgba(255, 234, 0,0.225)"),
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),
        ("75th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "98th (97.7th)", "rgba(255,0,0,0.25)")
    ]

    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Length"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Length"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=length, y=weight, mode='lines+markers', name='Child Data'))
    
    # Plotting the WHO reference data
    percentiles = [2.3, 5, 10, 25, 50, 75, 90, 95, 97.7]
    colors = ["#FF4500", "#FF7F50", "#FFA500", "#FFD700", "#32CD32", "#FFD700", "#FFA500", "#FF7F50", "#FF4500"]
    
    for perc, color in zip(percentiles, colors):
        if perc == 2.3:
            label = "2nd (2.3rd)"
        elif perc == 97.7:
            label = "98th (97.7th)"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Length"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="Child's Length/Height vs Weight Chart",
                      xaxis_title="Length/Height (cm)",
                      yaxis_title="Weight (Kg)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig



def plot_growth_chart_age_length(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    length = child_data["Length"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("2nd (2.3rd)", "5th", "rgba(255,0,0,0.25)"),
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),
        ("10th", "25th", "rgba(255, 234, 0,0.225)"),
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),
        ("75th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "98th (97.7th)", "rgba(255,0,0,0.25)")
    ]

    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_months, y=length, mode='lines+markers', name='Child Data'))
    
    # Plotting the WHO reference data
    percentiles = [2.3, 5, 10, 25, 50, 75, 90, 95, 97.7]
    colors = ["#FF4500", "#FF7F50", "#FFA500", "#FFD700", "#32CD32", "#FFD700", "#FFA500", "#FF7F50", "#FF4500"]
    
    for perc, color in zip(percentiles, colors):
        if perc == 2.3:
            label = "2nd (2.3rd)"
        elif perc == 97.7:
            label = "98th (97.7th)"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="Child's Length Growth Chart",
                      xaxis_title="Age (Months)",
                      yaxis_title="Length (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig




def plot_growth_chart_age_head(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    head_circumference = child_data["Head_circumference"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("2nd (2.3rd)", "5th", "rgba(255,0,0,0.25)"),
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),
        ("10th", "25th", "rgba(255, 234, 0,0.225)"),
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),
        ("75th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "98th (97.7th)", "rgba(255,0,0,0.25)")
    ]

    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_months, y=head_circumference, mode='lines+markers', name='Child Data'))
    
    # Plotting the WHO reference data
    percentiles = [2.3, 5, 10, 25, 50, 75, 90, 95, 97.7]
    colors = ["#FF4500", "#FF7F50", "#FFA500", "#FFD700", "#32CD32", "#FFD700", "#FFA500", "#FF7F50", "#FF4500"]
    
    for perc, color in zip(percentiles, colors):
        if perc == 2.3:
            label = "2nd (2.3rd)"
        elif perc == 97.7:
            label = "98th (97.7th)"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="Child's Head Circumference Growth Chart",
                      xaxis_title="Age (Months)",
                      yaxis_title="Head Circumference (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig





datasets = {
    "boys": {
        "age_weight": pd.read_csv("data/b_age_weight.csv"),
        "age_length": pd.read_csv("data/b_age_length.csv"),
        "age_head": pd.read_csv("data/b_age_headc.csv"),
        "length_weight": pd.read_csv("data/b_length_weight.csv")
        
        

        # ... [Añade otros conjuntos de datos para niños aquí]
    },
    "girls": {
        "age_weight": pd.read_csv("data/g_age_weight.csv"),
        "age_length": pd.read_csv("data/g_age_length.csv"),
        "age_head": pd.read_csv("data/g_age_headc.csv"),
        "length_weight": pd.read_csv("data/g_length_weight.csv")
        # ... [Añade otros conjuntos de datos para niñas aquí]
    }
}

child_data = pd.read_csv("data/child_data.csv")


# Inicializar la aplicación Dash


app = dash.Dash(__name__)

# Sidebar layout
sidebar = html.Div([
    html.H3("Introduce los datos", className='title'),
    html.Div([
        html.Label("Selecciona género:", className='bold-label'),
        dcc.RadioItems(
            id='gender-select',
            options=[
                {'label': 'Niño', 'value': 'boys'},
                {'label': 'Niña', 'value': 'girls'}
            ],
            value='boys',
            labelStyle={'display': 'block'}
        ),
    ], className='input-group'),
    html.Div([
        html.Label("Edad (Meses):", className='bold-label'),
        dcc.Input(id='input-age', type='number', value=0),
        html.Label("Peso (Kg):", className='bold-label'),
        dcc.Input(id='input-weight', type='number', value=0),
        html.Label("Longitud (cm):", className='bold-label'),
        dcc.Input(id='input-length', type='number', value=0),
        html.Label("Circunferencia de cabeza (cm):", className='bold-label'),
        dcc.Input(id='input-headc', type='number', value=0),
    ], className='input-group'),
    html.Button(id='submit-val', n_clicks=0, children='Actualizar gráfico', className='submit-btn')
], className='sidebar', style={'width': '20%', 'padding': '5px', 'background-color': '#f9f9f9', 'float': 'left'})

# Main content layout
main_content = html.Div([
    dcc.Tabs(
        id='metric-tabs',
        value='age_weight',
        children=[
            dcc.Tab(label='Edad vs Peso', value='age_weight'),
            dcc.Tab(label='Edad vs Longitud', value='age_length'),
            dcc.Tab(label='Edad vs Circunferencia de cabeza', value='age_head'),
            dcc.Tab(label='Longitud vs Peso', value='length_weight')
        ] # Esto es para intentar reducir la altura de las pestañas
    ),
    dcc.Graph(id='growth-chart')
], className='main-content', style={'width': '80%', 'padding': '20px', 'float': 'right'})
# Overall layout
app.layout = html.Div([sidebar, main_content], style={'display': 'flex', 'flex-flow': 'row nowrap'})

@app.callback(
    Output('growth-chart', 'figure'),
    [Input('gender-select', 'value'),
     Input('metric-tabs', 'value'),  # Ajusta esto
     Input('input-age', 'value'),
     Input('input-weight', 'value'),
     Input('input-length', 'value'),
     Input('input-headc', 'value')]
)

def update_graph(gender, metric, age, weight, length, headc):
    child_data = pd.DataFrame({
        'Age': [age],
        'Weight': [weight],
        'Length': [length],
        'Head_circumference': [headc]
    })
    
    if gender == "boys":
        data = datasets["boys"][metric]
    else:
        data = datasets["girls"][metric]
    
    if metric == 'age_weight':
        return plot_growth_chart(child_data, data)
    elif metric == 'age_length':
        return plot_growth_chart_age_length(child_data, data)
    elif metric == 'age_head':
        return plot_growth_chart_age_head(child_data, data)
    elif metric == 'length_weight':
        return plot_length_weight(child_data, data)

if __name__ == '__main__':
    app.run_server(debug=True)



