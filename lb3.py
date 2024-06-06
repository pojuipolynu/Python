import os
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

recognition_object = "plane"
plane = 2

model_dir = 'models/ssd_mobilenet_v2_coco/saved_model'
model = tf.saved_model.load(model_dir)

def detect_objects(image):
    image_np = np.array(image)
    input_tensor = tf.convert_to_tensor(image_np)
    input_tensor = input_tensor[tf.newaxis, ...]

    detections = model(input_tensor)

    for i in range(len(detections['detection_boxes'])):
        box = detections['detection_boxes'][i].numpy()
        ymin, xmin, ymax, xmax = box[0], box[1], box[2], box[3]
        image = cv2.rectangle(image, (int(xmin * image.shape[1]), int(ymin * image.shape[0])),
                              (int(xmax * image.shape[1]), int(ymax * image.shape[0])), (0, 255, 0), 2)

    return image

image_path = 'mqRUPPghetpzNQpcRwKJ4j-1200-80.jpg'
image = cv2.imread(image_path)

detected_image = detect_objects(image)

plt.imshow(cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()