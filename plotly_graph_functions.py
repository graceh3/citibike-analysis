import plotly.graph_objects as go


def plot_stackedbar(values=[],x=[],y=[],colors=[],title='',subtitle='',figsize=(800,450),showlegendvalue=True,subtitle_fontsize='10pt',y_axis_range=None,stack_labels=None):
    '''
    values (list) : string list of names for each stacked group,
    x (list) : string list of all categorical values to display on x-axis,
    y (list) : list of lists containing numerical value for each stacked group,
    colors (list) : string list of colors,
    title (str) : main title,
    subtitle (str) : subtitle,
    figsize (list) : list of numeric values representing [width, height],
    showlegendvalue (bool) : True/False,
    subtitle_fontsize (str) : font-size of subtitle,
    y_axis_range (list) : customer numeric range of y-axis [min, max],
    stack_labels (list) : list of lists
    '''
    # initialize the figure
    fig = go.Figure()

    # if you want to add custom stack labels
    if stack_labels:
        for i,v in enumerate(values):
            fig.add_trace(go.Bar(
                                x=x,
                                y=y[i],
                                name=v,
                                marker_color=colors[i],
                                text=stack_labels[i],
                                textposition='auto' # displays numeric value in bar
                            ))
    else:
    
        for i,v in enumerate(values):
            fig.add_trace(go.Bar(
                                    x=x,
                                    y=y[i],
                                    name=v,
                                    marker_color=colors[i],
                                    text=y[i],
                                    textposition='auto' # displays numeric value in bar
                                ))

    fig.update_layout(barmode='stack',
                    title_text=f'<b>{title}</b><br><span style="font-size: {subtitle_fontsize}">{subtitle}</span>',
                    xaxis_type='category',
                    showlegend=showlegendvalue,
                    autosize=False,
                    width=figsize[0],
                    height=figsize[1])

    if y_axis_range:
        fig.update_yaxes(range=y_axis_range)
    else:
        pass
        
    fig.show()



def plot_hbar(values=[],x=[],y=[],colors=[],title='',subtitle='',figsize=(800,450),showlegendvalue=True,subtitle_fontsize='10pt',y_axis_range=None,stack_labels=None):
    '''
    values (list) : string list of names for each stacked group,
    x (list) : string list of all categorical values to display on x-axis,
    y (list) : list of lists containing numerical value for each stacked group,
    colors (list) : string list of colors,
    title (str) : main title,
    subtitle (str) : subtitle,
    figsize (list) : list of numeric values representing [width, height],
    showlegendvalue (bool) : True/False,
    subtitle_fontsize (str) : font-size of subtitle,
    y_axis_range (list) : customer numeric range of y-axis [min, max],
    stack_labels (list) : list of lists
    '''
    # initialize the figure
    fig = go.Figure()

    # if you want to add custom stack labels
    if stack_labels:
        for i,v in enumerate(values):
            fig.add_trace(go.Bar(
                                x=x,
                                y=y[i],
                                name=v,
                                marker_color=colors[i],
                                text=stack_labels[i],
                                textposition='auto', # displays numeric value in bar
                                orientation='h'
                            ))    
    else:
        for i,v in enumerate(values):
            fig.add_trace(go.Bar(
                                    x=x,
                                    y=y[i],
                                    name=v,
                                    marker_color=colors[i],
                                    text=y[i],
                                    textposition='auto' # displays numeric value in bar
                                ))

    fig.update_layout(
                    title_text=f'<b>{title}</b><br><span style="font-size: {subtitle_fontsize}">{subtitle}</span>',
                    xaxis_type='category',
                    showlegend=showlegendvalue,
                    autosize=False,
                    width=figsize[0],
                    height=figsize[1])

    if y_axis_range:
        fig.update_yaxes(range=y_axis_range)
    else:
        pass
        
    fig.show()