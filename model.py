import torch
import numpy as np

garbage_categories = ['bottle', 'glass', 'biodegradable', 'cardboard', 'garbage']

# For more info, check out this research paper: https://arxiv.org/pdf/1506.02640.pdf
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, verbose=False)

# use yolov5 to detect garbage
def detectGarbage(image):
    # predict
    results = model([image])
    results = results.pandas().xyxy[0]
    item_count = len(results)

    # only keep the garbage detections
    results = results.loc[results['name'].isin(garbage_categories)]

    garbage_count = len(results)

    # extract the detections
    out = []
    for i in range(len(results)):
        data = {
            'x1': int(results.loc[i, ['xmin']].values.astype(np.float32)[0]),
            'y1': int(results.loc[i, ['ymin']].values.astype(np.float32)[0]),
            'x2': int(results.loc[i, ['xmax']].values.astype(np.float32)[0]),
            'y2': int(results.loc[i, ['ymax']].values.astype(np.float32)[0]),
            'category': results.loc[i, ['name']].values[0]
        }
        out.append(data)
    
    return out, garbage_count, item_count