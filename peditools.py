#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:49:18 2023

@author: felipe
"""
#----------Importar librerías-----------
import dash
import pandas as pd
import numpy as np
import datetime
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash import Dash, html, dcc, Input, Output, State, dash_table

##----------Importar modulos.-------
from modulos.modulos_gchart import *
from modulos.datasets import *
from modulos.percentil_calc import determine_specific_percentile

# Inicializar la aplicación Dash
data = []
app = Dash(__name__)
app.config.suppress_callback_exceptions = True

# Sidebar layout
sidebar = html.Div([
    html.H3("Introduce los datos", className='title'),
    html.Div([
        html.Label('Selecciona la organización:', className='bold-label'),
        dcc.Dropdown(
            id = 'org-select',
            options=[
                {'label': 'CDC', 'value':'CDC'},
                {'label':'OMS', 'value':'OMS'}
            ],
            value = 'CDC'
        )
    ], className = 'input-group'),
    html.Div([
        html.Label("Selecciona Sexo:", className='bold-label'),
        dcc.RadioItems(
            id='gender-select',
            options=[
                {'label': 'Masculino ', 'value': 'boys'},
                {'label': 'Femenino', 'value': 'girls'}
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
                {'label': '0 a 3 años', 'value': '0_3'},
                {'label': '3 a 20 años', 'value': '3_20'}
            ],
            value='0_3',
            labelStyle={'display': 'block'}
        ),
    ], className='input-group'),
    html.Div([
        html.Label(id = 'label', className='bold-label'),
        dcc.Input(id='input-age', type='number', value=1),
        html.Label("Peso (Kg):", className='bold-label'),
        dcc.Input(id='input-weight', type='number', value=4.5),
        html.Label("Longitud o Estatura (cm):", className='bold-label'),
        dcc.Input(id='input-length', type='number', value=55),
        html.Label("Circunferencia de cabeza (cm):", className='bold-label'),
        dcc.Input(id='input-headc', type='number', value=37),
    ], className='input-group'),
    html.Button(id='submit-val', n_clicks=0, children='Guardar datos', className='submit-btn')
], className='sidebar', style={'width': '20%', 'padding': '5px', 'background-color': '#f9f9f9', 'float': 'left'})

# Main content layout
main_content = html.Div([
    html.Div(id='tabs-container'),
    dcc.Graph(id='growth-chart')
], className='main-content', style={'width': '80%', 'padding': '20px', 'float': 'right'})

table = html.Div([
    dash_table.DataTable(
        id='data-table',
        data = data,
        columns=[
            {'name': 'Fecha', 'id': 'fecha'},
            {'name': 'Edad', 'id': 'edad'},
            {'name': 'Peso (Kg)', 'id': 'peso'},
            {'name': 'Estatura (cm)', 'id': 'estatura'},
            {'name': 'Circunferencia cabeza (cm)', 'id': 'circ-c'},
            {'name': 'Percentil', 'id': 'percentil'},
            {'name': 'Z score', 'id': 'z-score'},
            {'name': 'Desviación estándar', 'id': 'desv-e'}
        ],
        style_as_list_view=True,
        style_cell={'padding': '5px', 'textAlign': 'left'},
        style_header={'backgroundColor': '#D4E1DB','fontWeight': 'bold'}
    )
], style={'width': '80%', 'padding': '20px', 'float':'right'})


app.layout = html.Div([
    html.Div([sidebar, main_content], style={'display': 'flex', 'flex-flow': 'row nowrap'}),
    html.Div(table, style = {'font-size':'20px'})
])


#---------------CALLBACKS----------- 

# Callback para agregar datos a la tabla

@app.callback(
    Output('data-table', 'data'),
    Input('submit-val', 'n_clicks'),
    State('input-age', 'value'),
    State('input-weight', 'value'),
    State('input-length', 'value'),
    State('input-headc', 'value'),
    State('data-table', 'data')
)
def update_table(n_clicks, edad, peso, estatura, circunferencia, current_data):
    data = pd.read_csv('data/OMS/0-5/b_weight_age_oms_0-3.csv')
    
    if n_clicks is None:
        return dash.no_update

    if not edad or not peso or not estatura or not circunferencia:
        return dash.no_update

    # Cálculos Z score-desviación estándar-percentil-fecha
    mean_peso = np.mean(data['M'])

    std_peso = np.std(data['M'])

    z_score = (peso - mean_peso) / std_peso
    z_score = round(z_score,3)

    desviacion_estandar = std_peso
    desviacion_estandar = round(desviacion_estandar,3)
    
    fecha =  datetime.datetime.now().strftime("%d-%m-%Y")
    percentil= determine_specific_percentile(edad, peso, data)

    # Data entry for the current input
    new_entry = {
            'fecha': fecha,
            'edad': edad,
            'peso': peso,
            'estatura': estatura,
            'circ-c': circunferencia,
            'percentil':percentil,
            'z-score': z_score,
            'desv-e': desviacion_estandar
    }
    
    # Check if an entry with the same age already exists
    existing_entry = next((item for item in current_data if item["edad"] == edad), None)
    
    if existing_entry:
        # Update the existing entry if found
        index = current_data.index(existing_entry)
        current_data[index] = new_entry
    else:
        # If not found, insert the new entry at the beginning
        current_data.insert(0, new_entry)

    # Order the table based on 'edad' column, from largest to smallest
    current_data = sorted(current_data, key=lambda x: x['edad'], reverse=True)

    return current_data

@app.callback(
    Output('label', 'children'),
    Input('age-group-select', 'value')
)
def update_label(selected_value):
    if selected_value == '0_3':
        return 'Edad (Meses):'
    elif selected_value == '3_20':
        return 'Edad (Años):'


@app.callback(
    Output('tabs-container', 'children'),
    [Input('age-group-select', 'value'),
     Input('org-select', 'value')]
)
def update_tabs(age_group, organization):
    if organization == 'CDC':
        if age_group == '0_3':
            return dcc.Tabs(
                id='metric-tabs',
                value='age_weight',
                children=[
                    dcc.Tab(label='Edad vs Peso (0-3)', value='age_weight'),
                    dcc.Tab(label='Edad vs Longitud (0-3)', value='age_length'),
                    dcc.Tab(label='Edad vs Perímetro cefálico (0-2)', value='age_head'),
                    dcc.Tab(label='Longitud vs Peso (0-2)', value='length_weight')
                ]
            )
        else:
            return dcc.Tabs(
                id='metric-tabs',
                value='BMI_for_age_2_20',
                children=[
                    dcc.Tab(label='IMC vs Edad (2-20)', value='BMI_for_age_2_20'),
                    dcc.Tab(label='Peso vs Edad (3-20)', value='Weight_for_age_2_20'),
                    dcc.Tab(label='Estatura vs Edad (3-20)', value='Stature_for_age_2_20')
                ]
            )
    elif organization == 'OMS':
        if age_group == '0_3':
            return dcc.Tabs(
                id='metric-tabs',
                value='age_weight',
                children=[
                    dcc.Tab(label='Edad vs Peso (0-3)', value='age_weight'),
                    dcc.Tab(label='Edad vs Longitud (0-3)', value='age_length_0-3'),
                    dcc.Tab(label='Edad vs Perímetro cefálico (0-3)', value='age_head_0-3'),
                    dcc.Tab(label='Longitud vs Peso (0-2)', value='length_weight_0-2')
                ]
            )
        else:
            return dcc.Tabs(
                id='metric-tabs',
                value='BMI_for_age_5_19',
                children=[
                    dcc.Tab(label='IMC vs Edad (5-19)', value='BMI_for_age_5_19'),
                    dcc.Tab(label='Edad vs Peso (3-10)', value='Weight_for_age_3_10'),
                    dcc.Tab(label='Edad vs Perímetro cefálico (3-5)', value='age_head_3-5'),
                    dcc.Tab(label='Longitud vs Peso (2-5)', value='length_weight_2-5'),
                    dcc.Tab(label='Estatura vs Edad (3-19)', value='Stature_for_age_3_19')
                ]
            )
    
@app.callback(
    Output('growth-chart', 'figure'),
    [Input('gender-select', 'value'),
     Input('age-group-select', 'value'),
     Input('metric-tabs', 'value'),
     Input('input-age', 'value'),
     Input('input-weight', 'value'),
     Input('input-length', 'value'),
     Input('input-headc', 'value'),
     Input('org-select', 'value')]
)

def update_graph(gender, age_group, metric, age, weight, length, headc, organization):
    if organization == 'CDC':    
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
        
    
    elif organization == 'OMS':
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
            data = datasets_oms["boys"][data_key]
        else:
            data = datasets_oms["girls"][data_key]

        # Decide qué tipo de gráfico mostrar basado en la métrica
        if metric == 'age_weight':
            return plot_growth_chart_oms(child_data, data)
        elif metric == 'age_head_0-3':
            return plot_growth_hc_oms_0_3(child_data, data)
        elif metric == 'age_length_0-3':
            return plot_growth_age_length_oms(child_data, data)
        elif metric == 'length_weight_0-2':
            return plot_length_weight_0_2_oms(child_data, data)
        elif metric == 'BMI_for_age_5_19':
            return plot_bmi_age_5_19(child_data, data)
        elif metric == 'age_head_3-5':
            return plot_growth_hc_oms_3_5(child_data, data)
        elif metric == 'length_weight_2-5':
            return plot_length_weight_2_5_oms(child_data, data)
        elif metric == 'Weight_for_age_3_10':
            return plot_weight_age_5_10(child_data, data)
        elif metric == 'Stature_for_age_3_19':
            return plot_stature_age_5_19(child_data, data)


if __name__ == '__main__':
    app.run_server(debug=True)



