from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from model import detectGarbage
from PIL import Image
import os
from glob import glob

app = Flask(__name__)
CORS(app)

@app.route('/detect', methods=['POST'])
def detect():
    # save image
    if 'imagefile' not in request.files.keys():
        return jsonify({})
    image = request.files['imagefile']
    path = os.path.join("storage", image.filename)
    image.save(path)

    # read image using Pillow
    image = Image.open(path)

    # detect any garbage
    detections, garbage_count, item_count = detectGarbage(image)

    # remove saved image to free up memory
    for file in glob("storage/*"):
        os.remove(file)
    
    print(detections)

    if item_count == 0:
        return jsonify({'detections' : detections})
    else:
        return jsonify({'detections' : detections, 'garbagePercentage' : (garbage_count / item_count * 100)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)