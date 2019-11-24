from flask import Flask, request, abort, render_template
from hist_bins import hist_bins
from hist_graph import hist_graph

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"

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