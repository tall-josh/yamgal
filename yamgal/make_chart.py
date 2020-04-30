import pygal
import yaml

CHART_FROM_NAME_STR = {
    "Line" : pygal.Line,
    "StackedLine": pygal.StackedLine
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


def line_chart(data):

    validate_data(data)


    init_chart = CHART_FROM_NAME_STR[data['chart_type']]
    line_chart = init_chart(title   = data.get('title', ''),
                            x_title = data.get('x_title',''),
                            y_title = data.get('y_title',''),
                            interpolate = data.get('interpolate', None),
                            x_label_rotation=data.get('x_label_rotation', 0),
                            y_label_rotation=data.get('y_label_rotation', 0),
                            stroke = data.get('stroke', True),
                            dots = data.get('dots', True),
                            dot_size = data.get('dot_size', 1),
                            fill = data.get('fill', False),
                            zero = data.get('zero', 0),
                            human_readable = True,
                           )

    def default_x_labels(data):
        x_count = 0
        for run, values in data['data'].items():
            line_chart.add(run, values)
            if len(values) > x_count:
                x_count = len(values)
        return range(x_count)

    line_chart.x_labels = data.get('x_labels',\
                                   default_x_labels(data))
    line_chart.y_labels = data.get('y_labels', [])

    return line_chart
