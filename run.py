#""" Shows how to use flask and matplotlib together.
#Shows SVG, and png.
#The SVG is easier to style with CSS, and hook JS events to in browser.
#python3 -m venv venv
#. ./venv/bin/activate
#pip install flask matplotlib pandas
#python3 run.py
#"""
import io
import numpy as np
import pandas as pd
import random
from flask import Flask, Response, request, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure
import build_graph


app = Flask(__name__)

@app.route("/")
def index():
    """ Returns html with the img tag for your plot.
    """
    num_x_points = int(request.args.get("num_x_points", 50))
    df = pd.DataFrame(np.random.randint(0,100,size=(16, 8)), columns=list('ABCDEFGH'))
    array = df.to_numpy(dtype=int)
    heatmap_graph = build_graph.build_heatmap_df_to_png(df)
    #return f"""
    #<h1>Flask and matplotlib</h1>
    #<h2>Random data with num_x_points={num_x_points}</h2>
    #<form method=get action="/">
    #  <input name="num_x_points" type=number value="{num_x_points}" />
    #  <input type=submit value="update graph">
    #</form>
    #<h3>Plot as a png</h3>
    #<img src="/matplot-as-image-{num_x_points}.png"
    #     alt="random points as png"
    #     height="200">
    #<h3>Plot as a SVG</h3>
    #<img src="/matplot-as-image-{num_x_points}.svg"
    #     alt="random points as svg"
    #     height="200">
    #    
    #<h3>Heatmap</h3>
    #<p>Pandas dataframe: <br> {df}</p>
    #<p>NumPy array: <br> {array}</p>    
    #<img src="/heatmap-as-image-{df}.svg"
    #     alt="missing random points picture as svg"
    #     height="400">
    #"""
    # in a real app you probably want to use a flask template:
    # from flask import render_template
    return render_template("index.html", num_x_points=num_x_points, dataframe=df, array=array, heatmap_graph=heatmap_graph)


@app.route("/heatmap-as-image-<df>.svg")
def plot_heatmap(df):
    #df = generate_df()
    fig = Figure()
    axes = fig.add_subplot(1,1,1)
    axes.imshow(df)

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


@app.route("/matplot-as-image-<int:num_x_points>.png")
def plot_png(num_x_points=50):
    """ renders the .png plot on the fly."""
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


@app.route("/matplot-as-image-<int:num_x_points>.svg")
def plot_svg(num_x_points=50):
    """ renders the .svg plot on the fly."""
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(num_x_points)
    axis.plot(x_points, [random.randint(1, 30) for x in x_points])

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)