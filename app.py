from flask import Flask, request, abort, render_template
from hist_bins import hist_bins
from hist_graph import hist_graph
from stem_leaf import stemleaf
from transformations import Point

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
    
    starting_point = Point(float(json['x']), float(json['y']))
    for transformation in json['transformations']:
        if (transformation == None):
            continue

        # TODO: Fill in the conditions with the actions
        if (transformation == "translate"):
            pass
        elif (transformation == "rotate"):
            pass
        elif (transformation == "reflect"):
            pass
        elif (transformation == "dilate"):
            pass
        else:
            continue

        



if __name__ == "__main__":
    app.run(threaded=True, debug=False, port=80)
