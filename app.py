from flask import Flask, flash, request, redirect, url_for
from flask_cors import CORS, cross_origin
import main
import os

# Khởi tạo Flask Server Backend
app = Flask(__name__)

# Apply Flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = ''


@app.route('/div', methods=['POST', 'GET'])
@cross_origin(origin='*')
def predict():
    if request.method == 'POST':
        image = request.files['image']
        print(image)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'image_recognize.jpg'))
        return main.predict()

    return ''


# Start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555)
    print("done")
