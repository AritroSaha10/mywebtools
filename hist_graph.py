import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64
import PIL
import seaborn as sns

matplotlib.use('Agg')

# returns b64 data to use in histogram_graph.html template
def hist_graph(data):
    img = BytesIO()
    sns.distplot(data, kde=False, rug=True)
    canvas = plt.get_current_fig_manager().canvas
    canvas.draw()
    pil_image = PIL.Image.frombytes('RGB', canvas.get_width_height(), 
                 canvas.tostring_rgb())
    pil_image.save(img, 'PNG')
    plt.close()
    img.seek(0)
    val = img.getvalue()


    return base64.b64encode(img.getvalue())
    