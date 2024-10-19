import plotly.graph_objects as go

################################
#-------CDC GROWTH CHARTS-------
################################

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
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de peso infantil </span>(<b><span style='color:#344F3B; font-size: 20px;'>0-3 años</span></b>)",
                      xaxis_title="Edad (Meses)",
                      yaxis_title="Peso (Kg)",
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
    fig.update_layout(title="<span style = 'font-size: 20px;'>Grafica de altura vs peso infantil</span> (<b><span style='color:#344F3B; font-size: 20px;'>0-2 años</span></b>)",
                      xaxis_title="Altura/talla (cm)",
                      yaxis_title="Peso (Kg)",
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
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de altura infantil </span>(<b><span style='color:#344F3B; font-size: 20px;'>0-3 años</span></b>)",
                      xaxis_title="Edad (Meses)",
                      yaxis_title="Altura (cm)",
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
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de perímetro cefálico infantil </span>(<b><span style='color:#344F3B; font-size: 20px;'>0-2 años</span></b>)",
                      xaxis_title="Edad (Meses)",
                      yaxis_title="Perímetro cefálico (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig


def plot_bmi_age_2_20(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_years = child_data["Age"].values
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
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_years, y=bmi, mode='lines+markers', name='Child Data'))
    
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
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica IMC </span>(<b><span style='color:#344F3B; font-size: 20px;'>2-20 años</span></b>)",
                      xaxis_title="Edad (Años)",
                      yaxis_title="IMC",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_weight_age_2_20(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_years = child_data["Age"].values
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
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_years, y=weight, mode='lines+markers', name='Child Data'))
    
    
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
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de peso </span>(<b><span style='color:#344F3B; font-size: 20px;'>3-20 años</span></b>)",
                      xaxis_title="Edad (Años)",
                      yaxis_title="Peso (Kg)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_stature_age_2_20(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_years = child_data["Age"].values
    stature = child_data["Length"].values

    # Creating the figure
    fig = go.Figure()

    # Define percentiles and associated colors
    percentiles_fill = [
        ("2nd (2.3rd)", "5th", "rgba(255,0,0,0.25)"),#rojo
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"), #verde
        ("75th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "98th (97.7th)", "rgba(255,0,0,0.25)")
    ]

    # Plotting percentiles with fills
    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))

    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_years, y=stature, mode='lines+markers', name='Child Data'))
    
    
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
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento en estatura </span>(<b><span style='color:#344F3B; font-size: 20px;'>3-20 años</span></b>)",
                      xaxis_title="Edad (Años)",
                      yaxis_title="Estatura (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

################################
#-------OMS GROWTH CHARTS-------
################################

def plot_growth_chart_oms(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    weight = child_data["Weight"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors

    
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
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
    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    
    
    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de peso infantil </span>(<b><span style='color:#344F3B; font-size: 20px;'>0-3 años</span></b>)",
                      xaxis_title="Edad (Meses)",
                      yaxis_title="Peso (Kg)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_growth_hc_oms_0_3(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    head_circumference = child_data["Head_circumference"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors

    
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
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
    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    
    
    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de perímetro cefálico </span>(<b><span style='color:#344F3B; font-size: 20px;'>0-3 años</span></b>)",
                      xaxis_title="Edad (Meses)",
                      yaxis_title="Perímetro cefálico (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig


def plot_growth_hc_oms_3_5(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    head_circumference = child_data["Head_circumference"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors

    
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
    ]


    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_months, y=head_circumference, mode='lines+markers', name='Child Data'))
    
    # Plotting the WHO reference data
    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    
    
    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de perímetro cefálico </span>(<b><span style='color:#344F3B; font-size: 20px;'>3-5 años</span></b>)",
                      xaxis_title="Edad (Años)",
                      yaxis_title="Perímetro cefálico (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_length_weight_0_2_oms(child_data, reference_data):
    # Extracting data from the child dataframe
    length = child_data["Length"].values
    weight = child_data["Weight"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
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
    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    
    
    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"

        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Length"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
        
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de altura vs peso infantil </span>(<b><span style='color:#344F3B; font-size: 20px;'>0-2 años</span></b>)",
                      xaxis_title="Altura/talla (cm)",
                      yaxis_title="Peso (Kg)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_length_weight_2_5_oms(child_data, reference_data):
    # Extracting data from the child dataframe
    length = child_data["Length"].values
    weight = child_data["Weight"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
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
    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    
    
    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"

        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Length"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
        
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de altura vs peso infantil </span>(<b><span style='color:#344F3B; font-size: 20px;'>2-5 años</span></b>)",
                      xaxis_title="Altura/talla (cm)",
                      yaxis_title="Peso (Kg)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_growth_age_length_oms(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_months = child_data["Age"].values
    length = child_data["Length"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
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

    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    
    
    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"

        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Month"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
     
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de altura infantil </span>(<b><span style='color:#344F3B; font-size: 20px;'>0-5 años</span></b>)",
                      xaxis_title="Edad (Meses)",
                      yaxis_title="Altura (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_bmi_age_5_19(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_years = child_data["Age"].values
    bmi = child_data["BMI"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
    ]

    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_years, y=bmi, mode='lines+markers', name='Child Data'))
    
    # Plotting the WHO reference data
    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    
    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica IMC </span>(<b><span style='color:#344F3B; font-size: 20px;'>5-19 años</span></b>)",
                      xaxis_title="Edad (Años)",
                      yaxis_title="IMC",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_weight_age_5_10(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_years = child_data["Age"].values
    weight = child_data["Weight"].values
    
    # Creating the figure
    fig = go.Figure()
    
    # Define percentiles and associated colors
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
    ]

    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
    
    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_years, y=weight, mode='lines+markers', name='Child Data'))
    
    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    
    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"
    
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de peso </span>(<b><span style='color:#344F3B; font-size: 20px;'>3-10 años</span></b>)",
                      xaxis_title="Edad (Años)",
                      yaxis_title="Peso (Kg)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig

def plot_stature_age_5_19(child_data, reference_data):
    # Extracting data from the child dataframe
    age_in_years = child_data["Age"].values
    stature = child_data["Length"].values

    # Creating the figure
    fig = go.Figure()

    # Define percentiles and associated colors
    percentiles_fill = [
        ("0.1st", "1st", "rgba(255,0,0,0.25)"),#rojo
        ("1st", "3rd", "rgba(255,0,0,0.25)"),#rojo
        ("3rd", "5th", "rgba(255, 117, 24,0.25)"),#naranja
        ("5th", "10th", "rgba(255, 117, 24,0.25)"),#naranja
        ("10th", "15th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("15th", "25th", "rgba(255, 234, 0,0.225)"),#amarillo
        ("25th", "50th", "rgba(171, 224, 152,0.27)"),#verde
        ("50th", "75th", "rgba(171, 224, 152,0.27)"),#verde
        ('75th', '85th', "rgba(255, 234, 0,0.225)"),
        ("85th", "90th", "rgba(255, 234, 0,0.225)"),
        ("90th", "95th", "rgba(255, 117, 24,0.25)"),
        ("95th", "97th", "rgba(255, 117, 24,0.25)"),
        ("97th", "99th", "rgba(255,0,0,0.25)"),
        ("99th", "99.9th", "rgba(255,0,0,0.25)")
    ]

    # Plotting percentiles with fills
    for lower, upper, fillcolor in percentiles_fill:
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[upper],
                                 fill=None,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))
        
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[lower],
                                 fill='tonexty',
                                 fillcolor=fillcolor,
                                 mode='lines',
                                 line=dict(width=0),
                                 showlegend=False))

    # Plotting the child's data
    fig.add_trace(go.Scatter(x=age_in_years, y=stature, mode='lines+markers', name='Child Data'))
    
    
    percentiles = [0.1, 1, 3, 5, 10, 15, 25, 50, 75, 85, 90, 95, 97, 99, 99.9]
    colors = ["#FF4500","#FF4500", "#FF7F50", "#FF7F50", '#FFA500','#FFA500',"#32CD32","#32CD32","#32CD32",'#FFA500', '#FFA500', "#FF7F50", "#FF7F50","#FF4500", "#FF4500"]
    

    for perc, color in zip(percentiles, colors):
        if perc == 0.1:
            label = "0.1st"
        elif perc == 1:
            label = "1st"
        elif perc == 3:
            label = "3rd"    
        elif perc == 99.9:
            label = "99.9th"
        else:
            label = f"{int(perc)}th"
        
        # Main percentile line
        fig.add_trace(go.Scatter(x=reference_data["Years"], 
                                 y=reference_data[label].values, 
                                 mode='lines', 
                                 name=label,
                                 line=dict(color=color, width=1.5)))
    
    
    # Adding titles, labels, and adjusting dimensions
    fig.update_layout(title="<span style = 'font-size: 20px;'> Grafica crecimiento de estatura </span>(<b><span style='color:#344F3B; font-size: 20px;'>5-19 años</span></b>)",
                      xaxis_title="Edad (Años)",
                      yaxis_title="Estatura (cm)",
                      template="plotly_white",
                      width=1600,
                      height=800)
    
    return fig