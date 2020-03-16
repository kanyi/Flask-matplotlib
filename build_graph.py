import matplotlib.pyplot as plt
from io import BytesIO
import base64

def colorbar(mappable):
    """
    colorbar for easy usage - not fit to the graphs, anod no minortics
    https://joseph-long.com/writing/colorbars/
    """
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    #import matplotlib.pyplot as plt
    last_axes = plt.gca()
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(mappable, cax=cax)
    plt.sca(last_axes)
    return cbar

def build_xy_graph_png(x_coordinates, y_coordinates):
    img = io.BytesIO()
    plt.plot(x_coordinates, y_coordinates)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

def build_time_graph_png(x, y):
    img = BytesIO()
    plt.plot(x, y)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

def build_heatmap_df_to_png(df):
    """
    create .png matplotlib heatmap form pandas dataframe
    """
    img = BytesIO()
    plt.imshow(df, cmap="brg")
    plt.colorbar()
    plt.xticks(range(len(df.columns)), df.columns, rotation=0)
    plt.yticks(range(len(df.index)), df.index)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)
