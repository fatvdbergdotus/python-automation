from flask import Flask, render_template, request

def calculate_volume(length, width, height):
    """
    Calculate the volume of a rectangular prism.

    Parameters:
    length (float): The length of the prism.
    width (float): The width of the prism.
    height (float): The height of the prism.

    Returns:
    float: The calculated volume.
    """
    return length * width * height

app = Flask(__name__)

# Route for the home page (get request)
@app.route('/')
def about():
    print("get request")
    return render_template('index.html', dim_1=0, dim_2=0, dim_3=0)

# Route for the home page (post request)
@app.route('/', methods=['POST'])
def home():
    dim1 = request.form.get('first_dim')
    dim2 = request.form.get('second_dim')
    dim3 = request.form.get('third_dim')
    volume = calculate_volume(float(dim1), float(dim2), float(dim3))
    print("post request")
    return render_template('index.html', output=volume, dim_1=dim1, dim_2=dim2, dim_3=dim3)

app.run(debug=True)