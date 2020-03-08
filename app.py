from flask import Flask, request, abort, render_template
from hist_bins import hist_bins
from hist_graph import hist_graph
from stem_leaf import stemleaf
from transformations import Point, Axis

app = Flask(__name__)

commands = [
    ("/histogram/plot","Histogram Plotter. Use POST command to send data in json."),
    ("/histogram/bins","Histogram Bins. Organizes data into bins for histogram. Use POST command to send data in json."),
    ("/stem_leaf","Steam Leaf Plot. Organizes data into stem-leaf plot. Use POST command to send data in json.")
]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def wrong_method(e):
    return render_template('405.html'), 405

@app.route("/")
def home():
    return render_template("home.html",items=commands)

@app.route("/stem_leaf", methods=['POST'])
def stemleaf_mobile():
    json = request.json
    if (json == None):
        abort(400)
    if('data' not in json):
        abort(400)
    if(json['data'] == []):
        abort(400)
    return str(stemleaf(json['data']))
        
        
@app.route("/histogram/bins", methods=['POST'])
def histogram_bins():
    json = request.json
    if (json == None):
        abort(400)
    if('data' not in json):
        abort(400)
    if(json['data'] == []):
        abort(400)
    return str(hist_bins(json['data']))

@app.route("/histogram/plot", methods=['POST'])
def histogram_plot():
    json = request.json
    if (json == None):
        abort(400)
    if('data' not in json):
        abort(400)
    if(json['data'] == []):
        abort(400)
    plot_b64 = str(hist_graph(json['data']))[2:-1]
    return render_template('histogram_graph.html', plot_url=plot_b64)

@app.route("/transformations", methods=['POST'])
def transform():
    json = request.json
    if (json == None):
        abort(400)

    # data checking time
    if (json['x'] == None or json['y'] == None or json['transformations'] == None):
        abort(400)
    
    point = Point(float(json['x']), float(json['y']))

    for transformation in json['transformations']:
        if (json['transformations'][transformation] == None):
            continue

        if (json['transformations'][transformation] == "translate"):
            if (json['transformations'][transformation]['offset_x'] == None or json['transformations'][transformation]['offset_y'] == None):
                abort(400)
            
            offset_x = float(json['transformations'][transformation]['offset_x'])
            offset_y = float(json['transformations'][transformation]['offset_y'])
            
            point.translate(offset_x, offset_y)
        
        elif (json['transformations'][transformation] == "rotate"):
            if (json['transformations'][transformation]['rotation_angle'] == None or json['transformations'][transformation]['rotation_point'] == None):
                abort(400)

            rotation_angle = float(json['transformations'][transformation]['rotation_angle'])

            if (json['transformations'][transformation]['rotation_point']['x'] == None or json['transformations'][transformation]['rotation_point']['y'] == None):
                abort(400)

            rotation_point = (
                float(json['transformations'][transformation]['rotation_point']['x']), 
                float(json['transformations'][transformation]['rotation_point']['y'])
                )

            point.rotate(rotation_angle, rotation_point)
        
        elif (json['transformations'][transformation] == "reflect"):
            if (json['transformations'][transformation]['reflection_axis'] == None or json['transformations'][transformation]['reflection_point'] == None):
                abort(400)

            reflection_axis = Axis.X_AXIS

            if (json['transformations'][transformation]['reflection_axis'] == "y"):
                reflection_axis = Axis.Y_AXIS
            elif (json['transformations'][transformation]['reflection_axis'] == "both"):
                reflection_axis = Axis.BOTH

            reflection_point = (
                float(json['transformations'][transformation]['reflection_point']['x']),
                float(json['transformations'][transformation]['reflection_point']['y'])
            )

            point.reflect(reflection_axis, reflection_point)

        elif (json['transformations'][transformation] == "dilate"):
            if (json['transformations'][transformation]['scale_factor'] or json['transformations'][transformation]['dilation_point'] == None):
                abort(400)
            
            scale_factor = float(json['transformations'][transformation]['scale_factor'])
            dilation_point = (
                float(json['transformations'][transformation]['dilation_point']['x']),
                float(json['transformations'][transformation]['dilation_point']['y'])
            )

            point.dilate(scale_factor, dilation_point)
        else:
            continue


        return str({"x": point.x, "y": point.y})

        



if __name__ == "__main__":
    app.run(threaded=True, debug=False, port=80)
