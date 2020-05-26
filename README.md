# Yaml --> Pygal ... Yamgal

The ultimate goal for this is to emulate the GitHub Shield's functionality 
but for simple charts.

# Usage

`![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/TYPE/DATA/OPTIONAL_CONFIG)`

where:
  - TYPE: `line | bar | pie | donut | stackedbar | stackedline | xy | histogram` Case insensitive
  - DATA: Key:Value pairs separated by ';'. No spaces.
  ie: `one:[1,2,3];two:[5,6,7]` or some charts, like histogram take lists of lists charts `one:[[<height>,<x_start>,<x_end>],[...]]` see [Pyagl docs](http://www.pygal.org/en/stable/documentation/types/histogram.html)
  - OPTIONAL_CONFIG: Also Key:Value pairs. All options availiable to Pygal charts are availaible. Including by not limited to:
    - `title` (str): No spaces. Case is preserved) Default=None
    - `width` (int): Default=pretty big
    - `height` (int): Default=pretty big
    - `stroke` (True | False): Wether to draw a line between points. Default=True
    - `dots` (True | False): Wether to draw points. Default=True
    - `dot_size` (int): Default=2...ish
    - `fill` (True | False): Fill below the line down to zero. Default=False
    - `zero` (float): set reference to fill down to. Default=0
    - `x_title` (str): No spaces. Case is preserved) Default=None
    - `y_title` (str): No spaces. Case is preserved) Default=None
    - `x_label_rotation` (float):  0 is horazontal, - is cw, + ccw. Default=0
    - `y_label_rotation` (float):  0 is horazontal, - is cw, + ccw. Default=0
    - `interpolate` (cubic|quadratic|lagrange|trigonometric|hermite) Default=linear
    - `style` (blue | clean | dark_colorized | dark_green_blue | dark_green | dark_solarized | dark | default | light_colorized | light_green | light_solarized | light | neon | reb_blue | turquoise)
    
    
# Examples

`![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/line/one:[1,2,3];two:[5,6,7])`

![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/line/one:[1,2,3];two:[5,6,7])

`![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/line/one:[1,2,3];two:[5,6,7]/y_title:Ooooo;x_title:Ahhhh;style:dark)`

![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/line/one:[1,2,3];two:[5,6,7]/y_title:Ooooo;x_title:Ahhhh;style:dark)

`![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/pie/one:0.1;two:0.2;three:0.3;four:0.4/style:neon;title:Pie_Chart)`

![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/pie/one:0.1;two:0.2;three:0.3;four:0.4/style:neon;title:Pie_Chart)

`![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/pie/one:1;two:2;three:3;four:4/style:neon;inner_radius:0.4;half_pie:True;title:Half_Pie_Donut_Chart?2qss)`

![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/pie/one:1;two:2;three:3;four:4/style:neon;inner_radius:0.4;half_pie:True;title:Half_Pie_Donut_Chart?2qss)

`![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/line/one:[1,2,3];two:[2,3,4];three:[3,4,5];four:[4,5,6]/style:neon;title:Line;x_labels:[labels,work,now];x_label_rotation:-30?7)`

![demo](https://yamlgal-py3-alpine-c6l3dwv2sq-de.a.run.app/line/one:[1,2,3];two:[2,3,4];three:[3,4,5];four:[4,5,6]/style:neon;title:Line;x_labels:[labels,work,now];x_label_rotation:-30?7)


## Limitations

  - The browser tends to cache the image so changes don't show up unless you
    clear your cache and sometimes that doesn't even work. If you update the
    name of the file each time a change is made that works, but THER NEEDS to
    be a better way. **Potentially a githook that adds a `?<hash-of-yaml>` to
    the end of the imageurls in the README**

