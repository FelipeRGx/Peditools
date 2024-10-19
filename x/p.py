import dash
import pandas as pd
from dash import dcc, html
import plotly.graph_objects as go


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

# Leer los datos
b_age_weight = pd.read_csv("data/b_age_weight.csv")
g_age_weight = pd.read_csv("data/g_age_weight.csv")
b_length_weight = pd.read_csv("data/b_length_weight.csv")
g_length_weight = pd.read_csv("data/g_length_weight.csv")
child_data = pd.read_csv("data/child_data.csv", skiprows=1)

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Definir el diseño de la aplicación
app.layout = html.Div([
    # Encabezado
    html.Div([
        html.H1("Child's Growth Chart"),
    ], style={'textAlign': 'center', 'padding': '20px'}),
    
    # Pestañas para géneros
    dcc.Tabs([
        # Pestaña para niños
        dcc.Tab(label="Boys", children=[
            # Gráfico de Peso vs. Edad
            html.Div([
                dcc.Graph(figure=plot_growth_chart(child_data, b_age_weight))
            ]),
            # Gráfico de Longitud vs. Peso
            html.Div([
                dcc.Graph(figure=plot_growth_chart(child_data, b_length_weight))
            ])
        ]),
        
        # Pestaña para niñas
        dcc.Tab(label="Girls", children=[
            # Gráfico de Peso vs. Edad
            html.Div([
                dcc.Graph(figure=plot_growth_chart(child_data, g_age_weight))
            ]),
            # Gráfico de Longitud vs. Peso
            html.Div([
                dcc.Graph(figure=plot_growth_chart(child_data, g_length_weight))
            ])
        ]),
    ]),
    
    # Información adicional o controles (si es necesario)
    html.Div([], style={'padding': '20px'})
])

if __name__ == '__main__':
    app.run_server(debug=True)