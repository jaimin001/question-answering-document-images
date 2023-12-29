import pytesseract
from pytesseract import Output
import cv2
import json
import random
import os

# Load the image
img = cv2.imread("ffdh0227_1.png")

# Resize the image to 1024x1024
resized_img = cv2.resize(img, (1024, 1024))

# Perform OCR and get data
d = pytesseract.image_to_data(resized_img, output_type=Output.DICT)

# Initialize the result list
result = []

# Create a dictionary for the current image
image_result = {
    "boxes": [],
    "context": [],
    "image_id": "image.png",
    "qas": []
}

# Loop through the boxes and store the information
n_boxes = len(d['level'])
for i in range(n_boxes):
    text = d['text'][i]
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])

    # Add bounding box coordinates to the current image dictionary
    image_result["boxes"].append([x, y, x + w, y + h])

    # Add text to the context list
    image_result["context"].append(text)

    # Draw rectangle on the image
    cv2.rectangle(resized_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Add Q&A information
qid = f"{image_result['image_id']}-{random.randint(1, 100000)}"
qa = {
    "answer": [{
        "answer_end": 0,
        "answer_start": 0,
        "text": ""
    }],
    "qid": qid,
    "question": "hello there"
}
image_result["qas"].append(qa)

# Add the current image dictionary to the result list
result.append(image_result)

# Remove image extension from the file name
image_name = os.path.splitext(image_result['image_id'])[0]

# Convert the result list to JSON
json_result = json.dumps(result, indent=2)

# Save the JSON result to a file
with open(f"{image_name}.json", 'w') as json_file:
    json_file.write(json_result)

# Display the resized image with bounding boxes
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)
