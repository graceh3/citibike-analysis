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
                                    text=[f'{n:,}' for n in y[i]],
                                    textposition='outside' # displays numeric value in bar
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


def plot_hbar(values,x,y,colors,title,subtitle,figsize=(800,450),showlegendvalue=True,subtitle_fontsize='10pt',y_axis_range=None,stack_labels=None):
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
                                x=x[i],
                                y=y,
                                name=v,
                                marker_color=colors[i],
                                text=stack_labels[i],
                                textposition='outside', # displays numeric value in bar
                                orientation='h'
                            ))    
    else:
        for i,v in enumerate(values):
            fig.add_trace(go.Bar(
                                    x=x[i],
                                    y=y,
                                    name=v,
                                    marker_color=colors[i],
                                    text= [f'{n:,}' for n in x[i]], # OLD: x[i], 
                                    textposition='auto', # displays numeric value in bar
                                    orientation='h'
                                ))

    fig.update_layout(barmode='group',
                    title_text=f'<b>{title}</b><br><span style="font-size: {subtitle_fontsize}">{subtitle}</span>',
                    showlegend=showlegendvalue,
                    autosize=False,
                    width=figsize[0],
                    height=figsize[1],
                    xaxis=dict(ticks='',showticklabels=False))

    if y_axis_range:
        fig.update_yaxes(range=y_axis_range)
    else:
        pass
        
    fig.update_yaxes(autorange="reversed")

    fig.show()


def plot_doublegrouped_hbar(groups,labels,x,x2,y,x_colors,x2_colors,title,subtitle,figsize=(800,450),showlegendvalue=True,subtitle_fontsize='10pt',y_axis_range=None,stack_labels=None):

    # initialize the figure
    data=[]
    
    for i, l in enumerate(labels):
        if i==0:
            for j,g in enumerate(groups):
                data.append(go.Bar(
                                y=y,
                                x=x[j],
                                name=g+'-'+labels[i],
                                marker_color=x_colors[j],
                                # text=[f'{n:,}' for n in x[i]],
                                # textposition='auto', # displays numeric value in bar
                                orientation='h',
                                offsetgroup=j
                            )
                )
        else:
            for j,g in enumerate(groups):
                    data.append(go.Bar(
                                        y=y,
                                        x=x2[j],
                                        name=g+'-'+labels[i],
                                        marker_color=x2_colors[j],
                                        # text=[f'{n:,}' for n in x2[i]],
                                        # textposition='auto', # displays numeric value in bar
                                        orientation='h',
                                        offsetgroup=j,
                                        base=x[j]
                                        ))

    fig=go.Figure(data=data)

    fig.update_layout(barmode='group',
                    title_text=f'<b>{title}</b><br><span style="font-size: {subtitle_fontsize}">{subtitle}</span>',
                    showlegend=True,
                    autosize=False,
                    width=figsize[0],
                    height=figsize[1]
                    # xaxis=dict(ticks='',showticklabels=False)
                    )
    fig.update_yaxes(autorange="reversed")

    fig.show()

