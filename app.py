from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'title': 'Portfolio Website',
        'description': 'A dynamic portfolio showcasing my skills and projects, built with React and Flask.',
        'image': 'portfolio.jpg'  # Placeholder for image file
    },
    {
        'title': 'Data Analysis Dashboard',
        'description': 'A comprehensive dashboard visualizing key metrics from a large dataset, using Python and Tableau.',
        'image': 'dashboard.jpg' # Placeholder for image file
    },
    {
        'title': 'Machine Learning Model for Image Classification',
        'description': 'A convolutional neural network (CNN) trained to classify images with high accuracy using TensorFlow.',
        'image': 'ml_image.jpg' # placeholder for image file
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)