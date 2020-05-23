import pygal
import yaml

CHART_FROM_NAME_STR = {
    "Line" : pygal.Line,
    "StackedLine": pygal.StackedLine,
    "Bar": pygal.Bar,
    "StackedBar": pygal.StackedBar,
    "HorizontalBar": pygal.HorizontalBar,
    "Pie": pygal.Pie,
    "Histogram": pygal.Histogram,
    "XY": pygal.XY
}

STYLE_FROM_NAME_STR = {
    "Default": pygal.style.DefaultStyle,
    "Dark": pygal.style.DarkStyle,
    "Neon": pygal.style.NeonStyle,
    "DarkSolarized": pygal.style.DarkSolarizedStyle,
    "LightSolarized": pygal.style.LightSolarizedStyle,
    "Light": pygal.style.LightStyle,
    "Clean": pygal.style.CleanStyle,
    "RedBlue": pygal.style.RedBlueStyle,
    "DarkColorized": pygal.style.DarkColorizedStyle,
    "LightColorized": pygal.style.LightColorizedStyle,
    "Turquoise": pygal.style.TurquoiseStyle,
    "LightGreen": pygal.style.LightGreenStyle,
    "DarkGreen": pygal.style.DarkGreenStyle,
    "DarkGreenBlue": pygal.style.DarkGreenBlueStyle,
    "Blue": pygal.style.BlueStyle,
}

CHART_TYPE = 'chart_type'
DATA = 'data'

def validate_data(data):
    if not(CHART_TYPE in data):
        raise KeyError(f'"{CHART_TYPE}" must be specified')
    if not(data[CHART_TYPE] in CHART_FROM_NAME_STR):
        raise ValueError(f'Invalid chart_type: "{data[CHART_TYPE]}"')
    if not(DATA in data):
        raise KeyError('"data" MUST be specified')


def make_chart(data):

    validate_data(data)

    style = data['chart_config'].get('style', 'Default')
    data['chart_config']['style'] = STYLE_FROM_NAME_STR[style]

    init_chart = CHART_FROM_NAME_STR[data['chart_type']]
    chart = init_chart(**data['chart_config'],
                       human_readable = True,
                      )

    for run, values in data['data'].items():
        chart.add(run, values)

    chart.x_labels = data.get('x_labels', None)
    chart.y_labels = data.get('y_labels', None)

    return chart
