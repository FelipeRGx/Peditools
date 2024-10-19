#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:49:18 2023

@author: felipe
"""


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


def plot_bmi_age_2_20(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    bmi = child_data["BMI"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("2nd (2.3rd)", "5th", "rgba(255,0,0,0.25)"),
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),
        ("10th", "25th", "rgba(255, 234, 0,0.225)"),
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),
        ("75th", "85th", "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 117, 24,0.25)"),
        ("90th", "95th", "rgba(255,0,0,0.25)"),
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
    fig.add_trace(go.Scatter(x=age_in_months, y=bmi, mode='lines+markers', name='Child Data'))
    
    # Plotting the WHO reference data
    percentiles = [2.3, 5, 10, 25, 50, 75, 85, 90, 95, 97.7]
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
    fig.update_layout(title="Child's BMI for Age 2 to 20",
                      xaxis_title="Age (Months)",
                      yaxis_title="BMI",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_weight_age_2_20(child_data, reference_data):
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
    fig.update_layout(title="Child's Weight Growth Chart (2-20 years)",
                      xaxis_title="Age (Months)",
                      yaxis_title="Weight (Kg)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_stature_age_2_20(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    stature = child_data["Length"].values

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

    # Plotting percentiles with fills
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
    fig.add_trace(go.Scatter(x=age_in_months, y=stature, mode='lines+markers', name='Child Data'))
    
    
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
    fig.update_layout(title="Child's Stature Growth Chart (2-20 years)",
                      xaxis_title="Age (Years)",
                      yaxis_title="Stature (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig



datasets = {
    "boys": {
        "age_weight": pd.read_csv("data/b_age_weight.csv"),
        "age_length": pd.read_csv("data/b_age_length.csv"),
        "age_head": pd.read_csv("data/b_age_headc.csv"),
        "length_weight": pd.read_csv("data/b_length_weight.csv"),
        "BMI_for_age_2_20": pd.read_csv("data/2-20/BMI-for-age_b.tsv"),
        "Weight_for_age_2_20": pd.read_csv("data/2-20/Weight-for-age_b.tsv"),
        "Stature_for_age_2_20": pd.read_csv("data/2-20/Stature-for-age_b.tsv")
    },
    "girls": {
        "age_weight": pd.read_csv("data/g_age_weight.csv"),
        "age_length": pd.read_csv("data/g_age_length.csv"),
        "age_head": pd.read_csv("data/g_age_headc.csv"),
        "length_weight": pd.read_csv("data/g_length_weight.csv"),
        "BMI_for_age_2_20": pd.read_csv("data/2-20/BMI-for-age_W.tsv"),
        "Weight_for_age_2_20": pd.read_csv("data/2-20/Weight-for-age_W.tsv"),
        "Stature_for_age_2_20": pd.read_csv("data/2-20/Stature-for-age_W.tsv")
    }
}




child_data = pd.read_csv("data/child_data.csv")


# Inicializar la aplicación Dash


app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

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
        html.Label("Selecciona grupo de edad:", className='bold-label'),
        dcc.RadioItems(
            id='age-group-select',
            options=[
                {'label': '0 a 2 años', 'value': '0_2'},
                {'label': '2 a 20 años', 'value': '2_20'}
            ],
            value='0_2',
            labelStyle={'display': 'block'}
        ),
    ], className='input-group'),
    
    html.Div([
        html.Label("Edad (Meses o Años):", className='bold-label'),
        dcc.Input(id='input-age', type='number', value=0),
        
        html.Label("Peso (Kg):", className='bold-label'),
        dcc.Input(id='input-weight', type='number', value=0),
        
        html.Label("Longitud o Estatura (cm):", className='bold-label'),
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
            dcc.Tab(label='Edad vs Peso (0-2)', value='age_weight'),
            dcc.Tab(label='Edad vs Longitud (0-2)', value='age_length'),
            dcc.Tab(label='Edad vs Circunferencia de cabeza (0-2)', value='age_head'),
            dcc.Tab(label='Longitud vs Peso (0-2)', value='length_weight'),
            dcc.Tab(label='BMI vs Edad (2-20)', value='BMI_for_age_2_20'),
            dcc.Tab(label='Peso vs Edad (2-20)', value='Weight_for_age_2_20'),
            dcc.Tab(label='Estatura vs Edad (2-20)', value='Stature_for_age_2_20')
        ]
    ),
    dcc.Graph(id='growth-chart')
], className='main-content', style={'width': '80%', 'padding': '20px', 'float': 'right'})


app.layout = html.Div([sidebar, main_content], style={'display': 'flex', 'flex-flow': 'row nowrap'})
@app.callback(
    Output('growth-chart', 'figure'),
    [Input('gender-select', 'value'),
     Input('age-group-select', 'value'),  # Nuevo input
     Input('metric-tabs', 'value'),
     Input('input-age', 'value'),
     Input('input-weight', 'value'),
     Input('input-length', 'value'),
     Input('input-headc', 'value')]
)

def update_graph(gender, age_group, metric, age, weight, length, headc):
    child_data = pd.DataFrame({
        'Age': [age],
        'Weight': [weight],
        'Length': [length],
        'Head_circumference': [headc]
    })
    
    
    if length is not None and weight is not None and length != 0 and weight != 0:
        length_in_meters = length / 100  # Convertir la longitud de cm a m
        bmi = weight / (length_in_meters ** 2)  # Calcular el BMI
        child_data['BMI'] = [bmi]  # Añadir el BMI al DataFrame
    else:
        child_data['BMI'] = [None]  

    # Decide qué conjunto de datos usar basado en el género y el grupo de edad
    data_key = metric
      # Añade sufijo para métricas de 2 a 20 años

    if gender == "boys":
        data = datasets["boys"][data_key]
    else:
        data = datasets["girls"][data_key]

    # Decide qué tipo de gráfico mostrar basado en la métrica
    if metric == 'age_weight':
        return plot_growth_chart(child_data, data)
    elif metric == 'age_length':
        return plot_growth_chart_age_length(child_data, data)
    elif metric == 'age_head':
        return plot_growth_chart_age_head(child_data, data)
    elif metric == 'length_weight':
        return plot_length_weight(child_data, data)
    elif metric == 'BMI_for_age_2_20':
        return plot_bmi_age_2_20(child_data, data)
    elif metric == 'Weight_for_age_2_20':
        return plot_weight_age_2_20(child_data, data)
    elif metric == 'Stature_for_age_2_20':
        return plot_stature_age_2_20(child_data, data)

if __name__ == '__main__':
    app.run_server(debug=True)



