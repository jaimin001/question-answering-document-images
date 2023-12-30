import pytesseract
from pytesseract import Output
import cv2
import json
import random
import os


def save_bounding_boxes(image_path, questions, save_json=True, show_img=False):
    img = cv2.imread(image_path)

    # resizing as the model is trained for 1024x1024 images only
    resized_img = cv2.resize(img, (1024, 1024))

    d = pytesseract.image_to_data(resized_img, output_type=Output.DICT)

    result = []

    image_result = {"boxes": [], "context": [], "image_id": "image.png", "qas": []}

    # Loop through the boxes and store the information
    n_boxes = len(d["level"])
    for i in range(n_boxes):
        text = d["text"][i]
        (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])

        # Add bounding box coordinates to the current image dictionary
        image_result["boxes"].append([x, y, x + w, y + h])

        # Add text to the context list
        image_result["context"].append(text)

        # Draw rectangle on the image
        cv2.rectangle(resized_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Remove image extension from the file name
    image_name = os.path.splitext(image_path)[-2]

    # Add Q&A information
    for question in questions:
        qid = f"{image_name}-{random.randint(1, 100000)}"
        qa = {
            "answer": [{"answer_end": 0, "answer_start": 0, "text": ""}],
            "qid": qid,
            "question": question,
        }
        image_result["qas"].append(qa)

    # Add the current image dictionary to the result list
    result.append(image_result)

    # Convert the result list to JSON
    json_result = json.dumps(result, indent=2)

    file_path = os.path.join(os.getcwd(), "bounding_box_outputs", f"{image_name}.json")
    if save_json:
        if not os.path.exists("bounding_box_outputs"):
            os.makedirs("bounding_box_outputs")
        with open(file_path, "w") as json_file:
            json_file.write(json_result)

    if show_img:
        cv2.imshow("resized_img", resized_img)
        cv2.waitKey(0)

    return file_path
