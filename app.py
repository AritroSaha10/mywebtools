from flask import Flask, request, abort, render_template
from hist_bins import hist_bins
from hist_graph import hist_graph

app = Flask(__name__)

commands = [
    ("/histogram/plot","Histogram Plotter. Use POST command to send data in json."),
    ("/histogram/bins","Histogram Bins. Organizes data into bins for histogram. Use POST command to send data in json.")
]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def home():
    return render_template("home.html",items=commands)

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

if __name__ == "__main__":
    app.run(threaded=True, debug=False, port=80)
